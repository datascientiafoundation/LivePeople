import paramiko
import os
import pandas as pd
from collections import defaultdict
import argparse
import time

def get_child_dirs(client, target_directory):
    # Run find command for each level separately (5th, 6th, and 7th level)

    # Get 5th level directories
    command = f"find {target_directory} -mindepth 1 -maxdepth 12"
    stdin, stdout, stderr = client.exec_command(command)
    all_dirs = stdout.read().decode().splitlines()

    print(time.strftime("%Y-%m-%d %H:%M:%S"), " ✅ Dirs read successful! :" + str(len(all_dirs)))

    parquet_dirs = [dir for dir in all_dirs if
                    sum(1 for part in dir.split('/') if '.parquet' in part) == 1 and dir.endswith('parquet')]

    print(time.strftime("%Y-%m-%d %H:%M:%S"), " ✅ Parquet filtered successful! :" + str(len(parquet_dirs)))
    return parquet_dirs


def filter_latest_versions(client, target_directory):
    versioned_collections = defaultdict(list)
    unversioned_collections = defaultdict(list)

    command = f"find {target_directory} -mindepth 2 -maxdepth 2 -type d"
    stdin, stdout, stderr = client.exec_command(command)
    collections = stdout.read().decode().splitlines()

    for collection in collections:
        parts = collection.split('/')
        if parts[-1].startswith('v') and parts[-1][1:].isdigit():  # Check if last part is 'vX'
            base_path = '/'.join(parts[:-1])  # Everything before '/vX'
            versioned_collections[base_path].append(collection)
        elif parts[-1] not in ['Collection_Documentation']:
            base_path = '/'.join(parts[:-1])
            unversioned_collections[base_path].append(collection)

    # Get max version for each base path
    latest_collections = [max(versions, key=lambda x: int(x.split('/')[-1][1:])) for versions in
                          versioned_collections.values()]

    x = latest_collections + list(unversioned_collections.keys())

    print('active collections:')
    for xx in x:
        print(xx)
    return x


def filter(parquet_dirs, active_collections):
    filtered_parquets = [
        parquet for parquet in parquet_dirs
        if any(parquet.startswith(collection) for collection in active_collections)
    ]
    return sorted(filtered_parquets)


def load_dataset_mapping(excel_path):
    """Load dataset name and identifier mapping from Excel."""
    catalog_ds = pd.read_excel(excel_path, sheet_name='Dataset')

    catalog_ds = catalog_ds[['ds:DatName', 'ds:DatIdentifier']]
    dataset_mapping = {
        row['ds:DatName']: row['ds:DatIdentifier']
        for _, row in catalog_ds.iterrows()}

    return dataset_mapping


def map_directory_to_dataset(dataset_dirs, dataset_mapping):
    """Match dataset directories with their corresponding identifiers/names."""
    mapped_data = []
    existing_names = set()

    for dir_path in dataset_dirs:
        name = extract_name_from_path(dir_path)
        identifier = dataset_mapping.get(name, 'Unknown')

        ## MANUALS
        # for the special case where 'Questionnaire' is 'Questionnaire Exit Survey'
        if identifier == 'Unknown' and name.split('-')[-1] == 'Questionnaire':
            exit_survey_name = '-'.join(name.split('-')[:-1]) + '-' + 'Questionnaire Exit Survey'
            identifier = dataset_mapping.get(exit_survey_name, 'Unknown')
            name = name if identifier == 'Unknown' else exit_survey_name

        if identifier == 'Unknown' and name.split('-')[1] == 'ChatApplication2':
            if name.split('-')[-1] == 'Questionnaire':
                exit_survey_name = '2021-' + '-'.join(name.split('-')[1:-1]) + '-Questionnaire Exit Survey'
                identifier = dataset_mapping.get(temp_name, 'Unknown')
                name = name if identifier == 'Unknown' else exit_survey_name
            else:
                temp_name = '2021'+ '-' + '-'.join(name.split('-')[1:])
                identifier = dataset_mapping.get(temp_name, 'Unknown')
                name = name if identifier == 'Unknown' else temp_name

        mapped_data.append({ 'dataset_name': name, 'identifier': identifier, 'directory': dir_path})

        # Track names to check which ones exist in dataset_dirs
        existing_names.add(name)

        if "None" in name:
            print(f"none in name: {dir_path}")

    # Ensure all keys in dataset_mapping are included in mapped_data
    for key in dataset_mapping.keys():
        if key not in existing_names:
            # Add a new entry with `None` or an appropriate default value for the missing keys
            mapped_data.append(
                {'dataset_name': key, 'identifier': dataset_mapping[key], 'directory': None})

    return pd.DataFrame(mapped_data)


def get_sensor_key(value_to_check, sensor_mapping):

    # Loop through sensor_mapping to check if the value exists in any list
    for key, values in sensor_mapping.items():
        if value_to_check in values:
            return key

    # If not found, return None or an appropriate message
    return None


def extract_name_from_path(path):
    """Extract dataset name from directory path (customize as needed)."""

    collection_mapping = {
        'ChatApplication1': 'ChatApplication1',
        'ChatApplication2': 'ChatApplication2',
        'Diversity1': 'DiversityOne',
        'Mak': 'Makerere',
        'OC-FPT': 'OpenCalls',
        'OC-UTH': 'OpenCalls',
        'QROWD': 'QROWD',
        'SmartUnitn2': 'SmartUnitn2',
        'SmartUnitn2OSM': 'SmartUnitn2OSM',

        # non catalog
        'SmartUnitn1': 'SmartUnitn1',
        'SmartUnitn2_KGE_2024': 'SmartUnitn2_KGE_2024',
        'Diversity2': 'Diversity2',
        'Skel': 'Skel',
        'SmartUnitn2Pseudo': 'SmartUnitn2Pseudo',
        'Test_Opera': 'Test_Opera',
    }

    city_mapping = {
        'Site_Amrita_IN': 'Amrita',
        'Site_Asuncion_PY': 'Asunción',
        'Site_Copenhagen_DK': 'Copenhagen',
        'Site_Jilin_CN': 'Jilin',
        'Site_Kampala_UG': 'Kampala',
        'Site_London_UK': 'London',
        'Site_San-Luis-Potosi_MX': 'San Luis Potosí',
        'Site_Trento_IT': 'Trento',
        'Site_Ulan-Bator_MN': 'Ulaanbaatar',
        'Site_Hanoi_VN': 'Hanoi',
        'Site_Thessaloniki_GR': 'Thessaloniki',
    }
    sensor_mapping = {
        'Accelerometer': ['accelerometer', 'accelerometerevent'],
        'Accelerometer Uncalibrated': ['accelerometeruncalibrated'],
        'Airplane Mode': ['airplanemode', 'airplanemodeevent'],
        'Ambient Temperature': ['ambienttemperature'],
        'Application': ['application', 'applicationevent', 'applications'],
        'Activities': ['activities', 'activitiespertime'],
        'Battery Charge': ['batterycharge', 'batterychargeevent'],
        'Battery Monitoring Log': ['batterylevel', 'batterymonitoringlog'],
        'Bluetooth': ['bluetooth'],
        'Cellular Network': ['cellularnetwork'],
        'Chat': ['chat'],
        'Doze': ['dozemode', 'doze', 'dozeevent'],
        'Geomagnetic Rotation Vector': ['geomagneticrotationvector'],
        'Gravity': ['gravity', 'gravityevent'],
        'Gyroscope': ['gyroscope', 'gyroscopeevent'],
        'Gyroscope Uncalibrated': ['gyroscopeuncalibrated'],
        'Headset Plug': ['headsetplug', 'headsetplugevent'],
        'Light': ['light', 'lightevent'],
        'Location POI': ['location_poi'],
        'Location RD': ['location_rd', 'location', 'locationeventpertime_rd'],
        'Linear Acceleration': ['linearacceleration', 'linearaccelerationevent'],
        'Magnetic Field': ['magneticfield', 'magneticfieldevent'],
        'Magnetic Field Uncalibrated': ['magneticfielduncalibrated'],
        'Music': ['music', 'musicevent'],
        'Notification': ['notification', 'notificationevent'],
        'Orientation': ['orientation', 'orientationevent'],
        'Pressure': ['pressure', 'pressureevent'],
        'Proximity': ['proximity', 'proximityevent'],
        'Questionnaire': ['questionnaire', 'survey'],
        'Questionnaire Part 1' : ['survey1'],
        'Questionnaire Part 2' : ['survey2'],
        'Questionnaire Part 3' : ['survey3'],

        'Ring Mode': ['ringmode', 'ringmodeevent'],
        'Relative Humidity': ['relativehumidity', 'relativehumidityevent'],
        'Rotation Vector': ['rotationvector', 'rotationvectorevent'],
        'Screen': ['screen', 'screenevent'],
        'Step Counter': ['stepcounter'],
        'Step Detector': ['stepdetector'],
        'Time Diaries': ['timediaries', 'contributionsanswers', 'contributionsconfirmations', 'contributionsquestions',
                         'timediaries_processed', 'timediariesanswers', 'timediariesquestions', 'timediary'],
        'Touch': ['touch', 'touchevent'],
        'User Presence': ['userpresence'],
        'Wifi': ['wifi', 'wifievent'],
        'Wifi Networks': ['wifinetworks', 'wifinetworksevent'],

        'Ambient Temperature': ['ambienttemperature'],

        # followings have no catalog wp
        #     /datascientia_repository/CREP/Collection/2018.04.14-2018.06.06_SmartUnitn2/v3/Location/Site_Trento_IT/Sensors/Environment/ambienttemperature.parquet
        #     /datascientia_repository/CREP/Collection/2018.04.14-2018.06.06_SmartUnitn2_KGE_2024/Sensors/Environment/ambienttemperatureevent.parquet

        # no catalog, no wip
        # /datascientia_repository/CREP/Collection/2020.07.09-2020.07.09_QROWD/Location/Site_Trento_IT/Bundled/big_poi/2019-Qrowd2-poi/profile.parquet
    }


    parts = path.split('/')

    year = parts[4].split('.')[0]
    collection = collection_mapping.get('_'.join(parts[4].split('_')[1:]), "None")
    city = city_mapping.get(next((part for part in parts if part.startswith('Site')), None), "None")
    sensor = get_sensor_key(parts[-1].split('.parquet')[0], sensor_mapping)
    return f'{year}-{collection}-{city}-{sensor}'


def main(target_directory, output_dir, hostname, username, private_key_path, excel_path):
    output_file = os.path.join(output_dir, "dataset_dir.txt")
    output_mapping_file = os.path.join(output_dir, "dataset_dir_mapping.csv")
    dataset_mapping = load_dataset_mapping(excel_path)

    # Create SSH client
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.RejectPolicy())  # Secure: reject unknown hosts

    try:
        # Load the private key and connect using SSH key
        # private_key = paramiko.RSAKey.from_private_key_file(private_key_path)
        # client.connect(hostname, username=username, pkey=private_key)
        #
        # print(time.strftime("%Y-%m-%d %H:%M:%S"), " ✅ SSH connection successful!")
        #
        # # Get all child directories of the given path
        # parquet_dirs = get_child_dirs(client, target_directory)
        # active_collections = filter_latest_versions(client, target_directory)
        # active_dirs = filter(parquet_dirs, active_collections)
        # print(time.strftime("%Y-%m-%d %H:%M:%S"), " ✅ Filtered active dir - successful! :" + str(len(active_dirs)))

        # active_dirs = pd.DataFrame(active_dirs, columns=['dataset_dirs'])
        # active_dirs.to_csv(output_file, index=False)

        active_dirs = pd.read_csv(output_file)
        # active_dirs['k'] = active_dirs['dataset_dirs'].str.split('/').str[-1].str.split('.').str[0]
        active_dirs = active_dirs['dataset_dirs'].tolist()

        df = map_directory_to_dataset(active_dirs, dataset_mapping)

        df = df.sort_values(by=['dataset_name'])
        df.to_csv(output_mapping_file, index=False)


    finally:
        client.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch and filter parquet directories over SSH.")
    parser.add_argument("--target_directory", type=str, default="/datascientia_repository/CREP/Collection",
                        help="Target directory to search for parquet files.")
    parser.add_argument("--output_dir", type=str,
                        default="/Users/munkhdelger/Knowdive/LivePeople/resources/metadata_process_scripts/sources",
                        help="Output directory to save results.")
    parser.add_argument("--hostname", type=str, default="streambase3.disi.unitn.it", help="SSH hostname.")
    parser.add_argument("--username", type=str, default="m.bayanjargal", help="SSH username.")
    parser.add_argument("--private_key_path", type=str, default="/Users/munkhdelger/.ssh/id_rsa_streambase",
                        help="Path to SSH private key file.")
    parser.add_argument("--excel_path", type=str,
                        default="/Users/munkhdelger/Knowdive/LivePeople/resources/metadata_process_scripts/sources/catalog.xlsx")

    args = parser.parse_args()
    main(args.target_directory, args.output_dir, args.hostname, args.username, args.private_key_path, args.excel_path)

    # TODO - only works for single dataset, bundle?
