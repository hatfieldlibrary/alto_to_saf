The input to this program is a directory of subdirectories that contain ALTO files 
and corresponding images. It produces two output directories, one for METS/ALTO and 
image files and a second for Simple Archive Format directories that are used for 
DSpace import. The SAF files are written to a zip archive.

```Convert METS/ALTO data to Simple Archive Format for DSpace import.

positional arguments:
  Input directory       The parent directory containing METS, ALTO, image files 
                        and PDF
  Output directory      Full path to the output directory for the processed SAF 
                        subdirectories

optional arguments:
  -h, --help            show this help message and exit
  -m METADATA, --metadata METADATA
                        Metadata configuration file. Current configurations are 
                        "collegian", "bulletin"
  -b BUNDLE, --bundle BUNDLE
                        Images can be added to an alternate bundle if you do not 
                        want them included in the default (ORIGINAL) bundle. 
                        Typically we use the "iiif" bundle.
  -s STRIP, --strip STRIP
                        If provided this value will be stripped from the beginning 
                        of file names, e.g.Page_001.xml will be converted to 001.xml 
                        if the value "Page_" is provided

```
