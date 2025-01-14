import $ from 'jquery'
import {isEmpty} from 'lodash'

export function queryByHook(hook, container) {
    return $(`[data-hook~=${hook}]`, container)
}

export function queryByComponent(component, container) {
    return $(`[data-component~=${component}]`, container)
}

export function setContent(container, content) {
    return container.empty().append(content)
}

export function setParams(params) {
    let newUrl = window.location.href.split('?')[0]
    if (!isEmpty(params)) newUrl += '?' + $.param(params)
    window.history.replaceState(null, null, newUrl)
}

// Meant to mimic Jekyll's slugify function
// https://github.com/jekyll/jekyll/blob/master/lib/jekyll/utils.rb#L142
export function slugify(text) {
    return text.toString().toLowerCase().trim()
        .replace(/[^a-zA-Z0-9]/g, '-')  // Replace non-alphanumeric chars with -
        .replace(/\-\-+/g, '-')         // Replace multiple - with single -
        .replace(/^\-|\-$/i, '')        // Remove leading/trailing hyphen
}


// Given an object of filters to use, returns a function to be used by _.filter()
export function createDatasetFilters(filters) {
    return function (dataset) {
        const conditions = []
        if (filters.organization) {
            conditions.push(dataset.organization && slugify(dataset.organization) === filters.organization)
        }
        if (filters.category) {
            conditions.push(dataset.category && slugify(dataset.category) === filters.category)
        }
        if (filters.location) {
            conditions.push(dataset.location && slugify(dataset.location).indexOf(filters.location) !== -1)
        }
        if (filters.domain) {
            conditions.push(dataset.domain && slugify(dataset.domain).indexOf(filters.domain) !== -1)
        }
        if (filters.collection_name) {
            conditions.push(dataset.collection_name && slugify(dataset.collection_name).indexOf(filters.collection_name) !== -1)
        }
        if (filters.year) {
            const yearFromTitleMatch = dataset.title.match(/^\d{4}/); // Match the year at the start of the title
            const yearFromTitle = yearFromTitleMatch ? yearFromTitleMatch[0] : null; // Extract the year or set to null
            conditions.push(yearFromTitle && yearFromTitle === filters.year); // Include datasets that start with the specified year
        }
        if (filters.location_continent_facet) {
            conditions.push(dataset.location_continent_facet && slugify(dataset.location_continent_facet).indexOf(filters.location_continent_facet) !== -1)
        }

        if (filters.data_type_facet) {
            if(dataset.data_type_facet){
                console.log("filter data_type_facet-15:05")
                console.log(slugify(dataset.data_type_facet))
                console.log(filters.data_type_facet)
                conditions.push(dataset.data_type_facet && slugify(dataset.data_type_facet).indexOf(filters.data_type_facet) !== -1)}
            else{
                console.log("Invalid data_type_facet:", dataset.data_type_facet); // Handle invalid or null data_type_facet
                conditions.push("");
            }
        }

        if (filters.duration_facet) {
            conditions.push(dataset.duration_facet && slugify(dataset.duration_facet) === (filters.duration_facet))
        }


        return conditions.every(function (value) {
            return !!value
        })
    }
}

// Collapses a bootstrap list-group to only show a few items by default
// Number of items to show can be specified in [data-show] attribute or passed as param
export function collapseListGroup(container, show) {
    if (!show) show = container.data('show') || 5

    const itemsToHide = $('.list-group-item:gt(' + (show - 1) + '):not(.active)', container)
    if (itemsToHide.length) {
        itemsToHide.hide()

        const showMoreButton = $('<a href="#" class="list-group-item">Show ' + itemsToHide.length + ' more...</a>')
        showMoreButton.on('click', function (e) {
            itemsToHide.show()
            $(this).off('click')
            $(this).remove()
            e.preventDefault()
        })
        container.append(showMoreButton)
    }
}

// Applies a basic regex replace on a YAML string for each property in a data object
export function updateYamlString(yamlString, updateObject) {
    for (let key in updateObject) {
        const regex = new RegExp(`^( *${key}: +?).*`, 'm')
        const match = yamlString.match(regex)
        if (match) {
            yamlString = yamlString.replace(regex, match[1] + updateObject[key])
        } else {
            yamlString += `\n${key}: ${updateObject[key]}`
        }
    }
    return yamlString
}
