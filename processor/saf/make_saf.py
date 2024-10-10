import os
import shutil
import xml.etree.ElementTree as ET
from pathlib import Path

from processor.saf.utils.extract_metadata import ExtractMetadata

# This assures that IIIF is enabled for the item.
dspace_metadata_schema = ('<dublin_core schema="dspace">'
                          '<dcvalue element="iiif" qualifier="enabled">true</dcvalue>'
                          '</dublin_core>')


def mets_to_saf(input_dir: str, saf_dir: str, bundle: str):
    """

    :param input_dir: input directory containing mets/alto files
    :param saf_dir: output directory for saf
    :param bundle: the dspace bundle for image files -- optional
    :return: void
    """
    if not os.path.exists(saf_dir):
        os.makedirs(saf_dir)

    mets_tree = ET.parse(input_dir + '/mets.xml' )
    root = mets_tree.getroot()

    metadata_extractor = ExtractMetadata()
    dc_metadata = metadata_extractor.extract_metadata(root)
    dc_tree = ET.ElementTree(dc_metadata)
    dc_tree.write(saf_dir + '/dublin_core.xml', encoding="UTF-8", xml_declaration="True")
    path = Path(input_dir)
    process_files(path, saf_dir, bundle)

    with open(saf_dir + '/metadata_dspace.xml', 'w') as dspace_meta:
        dspace_meta.write(dspace_metadata_schema)


def process_files(path: Path, saf_dir: str, bundle: str):
    """

    :param path:
    :param saf_dir:
    :param bundle:
    :return:
    """
    for file in path.glob('*'):
        if file.is_file():
            if file.name.startswith('.') or file.name.startswith('Thumbs'):  # skip . files,e.g. .DS_Store, Thumbs.db
                continue

            shutil.copy(file, saf_dir + '/' + file.name)

            if file.suffix == '.xml':
                write_contents_other_bundle(saf_dir, file.name)

            if file.suffix == '.jp2':
                write_contents_image_bundle(saf_dir, file.name, bundle)


def write_contents_other_bundle(saf_dir, file):
    with open(saf_dir + '/contents', 'a') as content:
        content.write(file + '\tbundle:OtherContent\n')


def write_contents_image_bundle(saf_dir, file, bundle):
    fh = open(saf_dir + '/contents', 'a')
    if bundle:
        fh.write(file + '\tbundle:' + bundle + '\n')
    else:
        fh.write(file + '\n')

    fh.close()

