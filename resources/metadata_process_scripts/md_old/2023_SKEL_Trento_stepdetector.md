---
schema: default
title: 2023-Skel-Trento-Step Detector
organization: Unitn  # Copyright Holders in the config file
notes: Android API that counts (incrementally) the number of steps since the devices
  booted. The step detector sensor collects an event each time a step is taken by
  the user. The value reported by the sensor is always one, the fractional part being
  always zero, and the event timestamp is the time when the user’s foot hit the ground.
resources:
- name: codebook
      # URL must link to the corresponding codebook
  url: >-
    https://datascientiafoundation.github.io/LivePeople-Documentation/codebooks/2023_SKEL_Trento_stepdetector.html
  format: html
license: >-
  ./../../resources/2023LivePeopleLicense.html
dataset_name: Stepdetector
location: Trento (IT)
latitude_map: 46.04
longitude_map: 11.07
start_date: 2023-05-12 02:15:00
end_date: 2023-06-12 02:15:00
dataset_type: Sensors
sensor_type: Motion
size: 9.07 MB
dataset_format: parquet
other_format: csv
number_participants: 53
language: Not Applicable
collection_name: SKEL
project_url: <a href="https://ds.datascientia.eu/community/public/projects/">Datascientia
  community project</a>
5_stars: 3  # Fixed value
publication_date: 2024-11-16 14:15:08  # Current timestamp
identifier: 008.AAAQ.AAA.BI  # Generated based on the defined rules
request_contact: datadistribution.knowdive@unitn.it
maintainer: Andrea Bontempelli  # Maintainer based on authors
maintainer_email: datadistribution.knowdive@unitn.it
category:
- Dataset
domain: Digital University
---