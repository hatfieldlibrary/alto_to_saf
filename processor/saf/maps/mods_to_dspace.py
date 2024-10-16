#!/usr/bin/env python

from processor.saf.maps.field_maps import DBFields


class DBFieldMaps:
    """Mapping for existdb to DSpace dublin core and local fields.
    """

    def __init__(self):
        pass

    mets_structural_elements = DBFields.mets_structural_elements
    processor_field = DBFields.processor_mods_elements
    dspace_dc_field = DBFields.dspace_dc_field

    # Dspace mapping keys can be mets elements (e.g. dateIssued) or unique
    # keys defined below.
    switch_tag = {
        'identifier_other': {
            # Apply this to identifier elements that need the "other" qualifier.
            'id': 'identifier_other'
        },
        'statement_of_responsibility': {
            # Use this key to lookup DC mapping for statement of responsibility.
            # This is read from the mods:note element in the mets file. It maps
            # to description:statementofresponsibility in dspace.
            'id': 'statement_of_responsibility'
        },
        'resource_genre_element': {
            # Use this key to lookup DC mapping for genre.
            # This is read from the mods:genre element in the mets file. It maps
            # to dc.type in dspace.
            'id': 'genre'
        },
        # 'date_created_element': {
        #     # Use this key to look up DC dspace mapping for the item id.
        #     'id': 'dateIssued'
        # },
        'exist_db_id': {
            # Use this key to look up DC dspace mapping for the item id.
            # This value is either derived for the publication date or taken
            # directly from the mets:LABEL attribute.
            'id': 'exist_db_id'
        },
        'database_relation': {
            # This field does not exist in the mets file. We add it to all
            # items as relation:requires with the value 'existdb'. It
            # will be used to tell the dspace angular client where item
            # can be found.  (We could also embed the base or full url here.)
            'id': 'uses_exist_db_relation'
        },
        'language_iso': {
            'id': 'language_iso_qualifier'
        }
    }

    # Defines how to map mets metadata values to dspace dublin core.
    ds_field_map = {

        mets_structural_elements['label_attr']: {
            'element': dspace_dc_field['title'],
            'qualifier': None
        },
        processor_field['date_issued_element']: {
            'element': dspace_dc_field['date'],
            'qualifier': dspace_dc_field['date_issued_qualifier']
        },
        processor_field['date_created_element']: {
            'element': dspace_dc_field['date'],
            'qualifier': dspace_dc_field['date_created_qualifier']
        },
        processor_field['description_element']: {
            'element': dspace_dc_field['description'],
            'qualifier': dspace_dc_field['abstract']
        },
        # Maps the database id (existdb) to relation:requires.
        switch_tag['database_relation'].get('id'): {
            'element': dspace_dc_field['relation'],
            'qualifier': dspace_dc_field['relation_requires']
        },
        switch_tag['identifier_other'].get('id'): {
            'element': 'identifier',
            'qualifier': dspace_dc_field['identifier_doi_attr']
        },
        processor_field['identifier_element']: {
            'element': 'identifier',
            'qualifier': None
        },
        # Maps item identifier to identifier:other (for the exist item id).
        switch_tag['exist_db_id'].get('id'): {
            'element': dspace_dc_field['identifier'],
            'qualifier': None
        },
        processor_field['resource_type_element']: {
            'element': dspace_dc_field['type'],
            'qualifier': None
        },
        switch_tag['resource_genre_element'].get('id'): {
            'element': dspace_dc_field['type'],
            'qualifier': None
        },
        processor_field['access_conditions_element']: {
            'element': dspace_dc_field['rights'],
            'qualifier': None
        },
        processor_field['language_element']: {
            'element': dspace_dc_field['language'],
            'qualifier': None
        },
        switch_tag['language_iso'].get('id'): {
            'element': dspace_dc_field['language'],
            'qualifier': dspace_dc_field['language_iso_qualifier']
        },
        processor_field['physical_extent_element']: {
            'element': dspace_dc_field['format'],
            'qualifier': dspace_dc_field['format_extent_qualifier'],
        },
        # Maps mets "note" with type "statement of responsibility" to dc.publisher
        switch_tag['statement_of_responsibility'].get('id'): {
            'element': dspace_dc_field['publisher'],
            'qualifier': None
        },
        processor_field['item_details_element']: {
            'element': 'identifier',
            'qualifier': 'citation'
        }
    }


