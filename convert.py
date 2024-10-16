import argparse

from processor.process_data import process_files

"""
The program will create a METS file and requires user metadata input. The
resulting METS file, ALTO files and images are copied to an output SAF directory
(or directories) and zip file that can be imported into DSpace.
"""

parser = argparse.ArgumentParser(description='Converts a directory of alto and image files to Simple Archive Format '
                                             'for DSpace import.')
parser.add_argument('input_dir', metavar='Input directory', type=str,
                    help='The parent directory containing ALTO, image files and PDF')
parser.add_argument('saf', metavar='Output directory', type=str,
                    help='Full path to the output directory for the processed SAF subdirectories')
parser.add_argument('-m', '--metadata',
                    help='Metadata configuration file. Current configurations are "collegian", "bulletin"')
parser.add_argument('-b',  "--bundle",
                    help='Images can be added to an alternate bundle if you do not want them included in the default '
                         '(ORIGINAL) bundle. Typically we use the "iiif" bundle.')
parser.add_argument('-s',  "--strip",
                    help='If provided this value will be stripped from the beginning of file names, e.g.'
                         'Page_001.xml will be converted to 001.xml if the value "Page_" is provided')

args = parser.parse_args()
directory = args.input_dir
saf = args.saf

process_files(directory.rstrip('/'), saf.rstrip('/'), args.metadata, args.bundle, args.strip)

