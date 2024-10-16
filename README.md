The input to this program is a directory of subdirectories that contain ALTO files 
and corresponding images. It produces two output directories: one that contains a
newly minted METS file along with the original image files (optionally renamed) and
the ALTO files, and a second directory for Simple Archive Format subdirectories. The  
SAF directories are written to a zip archive for easy DSpace import.

```
usage: convert.py [-h] [-m METADATA] [-b BUNDLE] [-s STRIP] Input directory Output directory

Converts a directory of alto and image files to Simple Archive Format for DSpace import.

positional arguments:
  Input directory       The parent directory containing ALTO, image files and PDF
  Output directory      Full path to the output directory for the processed SAF subdirectories

optional arguments:
  -h, --help            show this help message and exit
  -m METADATA, --metadata METADATA
                        Metadata configuration file. Current configurations are "collegian", "bulletin"
  -b BUNDLE, --bundle BUNDLE
                        Images can be added to an alternate bundle if you do not want them 
                        included in the default (ORIGINAL) bundle. Typically we use the "iiif" bundle.
  -s STRIP, --strip STRIP
                        If provided this value will be stripped from the beginning of file names, 
                        e.g.Page_001.xml will be converted to 001.xml if the value "Page_" is provided


```
