import $ from 'jquery'
import {chain, pick, omit, filter, defaults} from 'lodash'

import TmplListGroupItem from '../templates/list-group-item'
import {setContent, slugify, createDatasetFilters, collapseListGroup} from '../util'

export default class LocationFacetFilter {
    constructor(opts) {
        const locations = this._locationsWithCount(opts.datasets, opts.params)
        const locationsMarkup = locations.map(TmplListGroupItem)
        setContent(opts.el, locationsMarkup)
        collapseListGroup(opts.el)
    }


    // Given an array of datasets, returns an array of their locations with counts
    _locationsWithCount(datasets, params) {
        return chain(datasets)
            .filter('location_facet')  // Change to location_facet
            .groupBy('location_facet')  // Change to location_facet
            .map((datasetsInLoc, location) => {
                const filters = createDatasetFilters(pick(params, [
                    'category',
                    'collection_name',
                    'year',
                    'location_facet',
                    'duration_facet',
                    'data_type_facet']))  // Change to location_facet
                const filteredDatasets = filter(datasetsInLoc, filters)
                const locationSlug = slugify(location)
                const selected = params.location_facet && params.location_facet === locationSlug  // Change to location_facet
                const itemParams = selected
                    ? omit(params, 'location_facet')  // Change to location_continent_facet
                    : defaults({location_facet: locationSlug}, params)  // Change to location_facet

                return {
                    title: location,
                    url: '?' + $.param(itemParams),
                    count: filteredDatasets.length,
                    unfilteredCount: datasetsInLoc.length,
                    selected: selected
                }
            })
            .orderBy('title', 'asc')
            .value()
    }
}
