#!/usr/bin/env python


class DBFields:
    """This class manages field names used by DSpace and METS.

    Dictionaries define field names used for mods, mets strucutral metadata, and dspace dublin core.
    """
    def __init__(self):
        pass

    # Mods elements
    mets_mods_elements = {
        'identifier_element': 'mods:identifier',
        'identifier_element_doi': 'mods:identifier',
        'item_details_element': 'mods:detail',
        'date_issued_element': 'mods:dateIssued',
        'date_created_element': 'mods:dateCreated',
        'abstract_element': 'mods:abstract',
        'note_element': 'mods:note',
        'access_conditions_element': 'mods:accessCondition',
        'language_element': 'mods:languageTerm',
        'title_element': 'mods:title',
        'sub_title_element': 'mods:subTitle',
        'physical_description_element': 'mods:physicalDescription',
        'physical_extent_element': 'mods:extent',
        'resource_type_element': 'mods:typeOfResource',
        'resource_genre_element': 'mods:genre',
        'statement_responsibility_element': 'mods:note'
    }

    # Mods attributes
    mets_mods_element_attrs = {
        'doi_type_attr': 'doi',
        'type_attr': 'type',
        'encoding_attr': 'encoding',
        'qualifier_attr': 'qualifier',
        'code_attr': 'code',
        'authority_attr': 'authority',
        'display_attr': 'displayLabel'
    }

    # Mets structural elements and attributes
    mets_structural_elements = {
        'mets_root_element': 'mets',
        'label_attr': 'LABEL',
        'mets_header_element': 'mets:metsHdr',
        'mets_agent_element': 'mets:agent',
        'mets_agent_name_element': 'mets:name',
        'descriptive_metadata_section': 'mets:dmdSec',
        'mods_section_element': 'mods:mods',
        'file_section': 'mets:fileSec',
        'file_group': 'mets:fileGrp',
        'file': 'mets:file',
        'file_location': 'mets:FLocat',
        'file_href': '{http://www.w3.org/1999/xlink}href'
    }

    # For subsequent processing it's convenient to have a dictionary that excludes the namespace.
    processor_mods_elements = {
        'identifier_element': 'identifier',
        'identifier_element_doi': 'identifier',
        'item_details_element': 'detail',
        'item_number_element': 'number',
        'date_issued_element': 'dateIssued',
        'date_created_element': 'dateCreated',
        'description_element': 'abstract',
        'note_element': 'note',
        'statement_responsibility_element': 'note',
        'access_conditions_element': 'accessCondition',
        'language_element': 'languageTerm',
        'sub_title_element': 'subTitle',
        'physical_description_element': 'physicalDescription',
        'physical_extent_element': 'extent',
        'resource_type_element': 'typeOfResource',
        'resource_genre_element': 'genre'
    }

    # The elements and attributes to read from the mets file.
    mets_fields = {

        mets_structural_elements['mets_root_element']: {
            'element': mets_structural_elements['mets_root_element'],
            'attr': mets_structural_elements['label_attr'],
            'attr_val': None
        },
        mets_mods_elements['identifier_element']: {
            'element': mets_mods_elements['identifier_element'],
            'attr': mets_mods_element_attrs['type_attr'],
            'attr_val': None
        },
        mets_mods_elements['identifier_element_doi']: {
            'element': mets_mods_elements['identifier_element'],
            'attr': mets_mods_element_attrs['type_attr'],
            'attr_val': ['doi']
        },
        mets_mods_elements['item_details_element']: {
            'element': mets_mods_elements['item_details_element'],
            'attr': mets_mods_element_attrs['type_attr'],
            'attr_val': ['volume', 'issue', 'edition']
        },
        mets_mods_elements['access_conditions_element']: {
            'element': mets_mods_elements['access_conditions_element'],
            'attr': None,
            'attr_val': None
        },
        mets_mods_elements['language_element']: {
            'element': mets_mods_elements['language_element'],
            'attr': mets_mods_element_attrs['type_attr'],
            'attr_val': ['text', 'code']
        },
        mets_mods_elements['abstract_element']: {
            'element': mets_mods_elements['abstract_element'],
            'attr': None,
            'attr_val': None
        },
        mets_mods_elements['note_element']: {
            'element': mets_mods_elements['note_element'],
            'attr': mets_mods_element_attrs['type_attr'],
            'attr_val': ['statement of responsibility']
        },
        mets_mods_elements['date_issued_element']: {
            'element': mets_mods_elements['date_issued_element'],
            'attr': mets_mods_element_attrs['encoding_attr'],
            'attr_val': ['w3cdtf', 'temper', None]
        },
        mets_mods_elements['date_created_element']: {
            'element': mets_mods_elements['date_created_element'],
            'attr': mets_mods_element_attrs['qualifier_attr'],
            'attr_val': ['approximate']
        },
        mets_mods_elements['resource_type_element']: {
            'element': mets_mods_elements['resource_type_element'],
            'attr': None,
            'attr_val': None
        },
        mets_mods_elements['resource_genre_element']: {
            'element': mets_mods_elements['resource_genre_element'],
            'attr': mets_mods_element_attrs['authority_attr'],
            'attr_val': ['att']
        },
        mets_mods_elements['physical_extent_element']: {
            'element': mets_mods_elements['physical_extent_element'],
            'attr': None,
            'attr_val': None
        }
    }

    # Fields used for DSpace dublin core import. Not all are used
    # for mets metadata, but good to include all since that allows
    # for revising the mapping strategy.
    dspace_dc_field = {
        'title': 'title',
        'title_alt_qualifier': 'alternative',
        'creator': 'creator',
        'description': 'description',
        'abstract': 'abstract',
        'description_statement_of_responsibility': 'description',
        'description_provenance_qualifier': 'provenance',
        'description_statement_responsibility_qualifier': 'statementofresponsibility',
        'date': 'date',
        'date_created_qualifier': 'created',
        'date_issued_qualifier': 'issued',
        'subject': 'subject',
        'source': 'source',
        'relation': 'relation',
        'relation_requires': 'requires',
        'relation_uri_qualifier': 'uri',
        'relation_ispartof_qualifier': 'ispartof',
        'relation_isformatof_qualifier': 'isformatof',
        'coverage': 'coverage',
        'coverage_spatial_qualifier': 'spatial',
        'language': 'language',
        'language_iso_qualifier': 'iso',
        'identifier': 'identifier',
        'identifier_doi_attr': 'other',
        'citation_qualifier': 'citation',
        'publisher': 'publisher',
        'type': 'type',
        'format': 'format',
        'format_medium_qualifier': 'medium',
        'format_extent_qualifier': 'extent',
        'rights': 'rights'

    }



