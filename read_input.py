import argparse

from processor.process_data import process_files

parser = argparse.ArgumentParser(description='Process METS/ALTO data for DSpace simple archive format import.')
parser.add_argument('input_dir', metavar='Input directory', type=str,
                    help='The parent directory containing METS, ALTO, image files and PDF')
parser.add_argument('saf', metavar='Output directory', type=str,
                    help='Full path to the output directory for the processed SAF subdirectories')
parser.add_argument('config', metavar='Metadata configuration', nargs='?', type=str, default='default',
                    help='Metadata configuration file (optional). Current configurations are "collegian", "bulletin"')
parser.add_argument('-b',  "--bundle",
                    help='Images can be added to an alternate bundle if you do not want them included in the default '
                         '(ORIGINAL) bundle')
parser.add_argument('-s',  "--strip",
                    help='If provided this value will be stripped from the beginning of file names, e.g.'
                         'Page_001.xml will be converted to 001.xml if the value "Page_" is provided')

args = parser.parse_args()
directory = args.input_dir
saf = args.saf

process_files(directory.rstrip('/'), saf.rstrip('/'), args.config, args.bundle, args.strip)

