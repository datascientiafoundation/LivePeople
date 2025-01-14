import $ from 'jquery'
import { chain, pick, omit, filter, defaults } from 'lodash'

import TmplListGroupItem from '../templates/list-group-item'
import { setContent, slugify, createDatasetFilters, collapseListGroup } from '../util'

export default class LocationContinentFilter {
  constructor(opts) {
    const locations = this._locationsWithCount(opts.datasets, opts.params)
    const locationsMarkup = locations.map(TmplListGroupItem)
    setContent(opts.el, locationsMarkup)
    collapseListGroup(opts.el)
  }

  // Given an array of datasets, returns an array of their locations with counts
  _locationsWithCount(datasets, params) {
    return chain(datasets)
      .filter('location_continent_facet')  // Change to location_continent_facet
      .groupBy('location_continent_facet')  // Change to location_continent_facet
      .map((datasetsInLoc, location) => {
        console.log("Processing location:", location);
        const filters = createDatasetFilters(pick(params, ['category', 'collection_name', 'location', 'location_continent_facet', 'year']))  // Change to location_continent_facet
        const filteredDatasets = filter(datasetsInLoc, filters)
        const locationSlug = slugify(location)
        const selected = params.location_continent_facet && params.location_continent_facet === locationSlug  // Change to location_continent_facet
        const itemParams = selected
          ? omit(params, 'location_continent_facet')  // Change to location_continent_facet
          : defaults({ location_continent_facet: locationSlug }, params)  // Change to location_continent_facet

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
