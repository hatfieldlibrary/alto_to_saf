
```positional arguments:
  input directory       the parent directory containing METS, ALTO, image files and PDF
  Output SAF directory  full path to the output directory that will contain the SAF subdirectories
  metadata configuration
                        Metadata configuration file: current options are collegain, bulletin

optional arguments:
  -h, --help            show this help message and exit
  -b BUNDLE, --bundle BUNDLE
                        images can be added to an alternate bundle if you do not want them included 
                        in the default (ORIGINAL) bundle
  -s STRIP, --strip STRIP
                        if provided this value will be stripped from the beginning of file names, 
                        e.g.Page_001.xml will be converted to 001.xml if the value "Page_" is provided
```
