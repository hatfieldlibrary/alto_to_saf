import argparse

from processor.process_data import process_files

parser = argparse.ArgumentParser(description='Process METS/ALTO data for DSpace simple archive format import.')
parser.add_argument('input_dir', metavar='input directory', type=str,
                    help='the parent directory containing METS, ALTO, image files and PDF')
parser.add_argument('saf', metavar='Output SAF directory', type=str,
                    help='full path to the output directory that will contain the SAF subdirectories')
parser.add_argument('config', metavar='metadata configuration', type=str,
                    help='Metadata configuration file: current options are collegain, bulletin')
parser.add_argument('-b',  "--bundle",
                    help='images can be added to an alternate bundle if you do not want them included in the default '
                         '(ORIGINAL) bundle')
parser.add_argument('-s',  "--strip",
                    help='if provided this value will be stripped from the beginning of file names, e.g.'
                         'Page_001.xml will be converted to 001.xml if the value "Page_" is provided')

args = parser.parse_args()
directory = args.input_dir
saf = args.saf

process_files(directory.rstrip('/'), saf.rstrip('/'), args.config, args.bundle, args.strip)

