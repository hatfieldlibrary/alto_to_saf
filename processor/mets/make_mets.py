import time
import re


def mets_hdr_dmd_sec(config, createdate, fh):
    s1 = '''\
<?xml version="1.0" encoding="UTF-8"?>        
    <mets:mets LABEL="%s %s"
        xmlns:mets="http://www.loc.gov/METS/" 
        xmlns:mods="http://www.loc.gov/mods/v3" 
        xmlns:xlink="http://www.w3.org/1999/xlink" 
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
        xsi:schemaLocation="
        http://www.loc.gov/METS/ http://www.loc.gov/standards/mets/version17/mets.v1-7.xsd
        http://www.loc.gov/mods/v3 http://www.loc.gov/mods/v3/mods-3-4.xsd">
     <!--METS HEADER-->
     <mets:metsHdr CREATEDATE="%s">
        <mets:agent ROLE="CREATOR" TYPE="ORGANIZATION">
            <mets:name>%s</mets:name>
        </mets:agent>
    </mets:metsHdr>

    <!--DESCRIPTIVE METADATA-->
    
    <mets:dmdSec ID="DMD1">
        <mets:mdWrap MDTYPE="MODS" MIMETYPE="text/xml" LABEL="MODS Metadata">
            <mets:xmlData>
                <mods:mods>
''' % (attribute_escape(config['title']), attribute_escape(config['sub_title']), createdate, config['publisher'])

    if config['volume'] or config['issue']:
        s2 = '\t\t\t<mods:relatedItem type="host">\n\t\t\t\t<mods:part>\n'
        if (config['volume'] != ''):
            s2 = s2 + '\t\t\t\t\t<mods:detail type="volume"><mods:number>%s</mods:number></mods:detail>\n' % (config['volume'])
        if (config['issue'] != ''):
            s2 = s2 + '\t\t\t\t\t<mods:detail type="issue"><mods:number>%s</mods:number></mods:detail>\n' % (config['issue'])

        s2 = s2 + "\t\t\t\t</mods:part>\n\t\t\t</mods:relatedItem>\n"
    else:
        s2 = ''

    s3 = '''<mods:accessCondition>%s</mods:accessCondition>  
                    <mods:language>
                        <mods:languageTerm type="text">English</mods:languageTerm>
                        <mods:languageTerm type="code" authority="iso639-2b">eng</mods:languageTerm>
                    </mods:language>
                    <mods:note type="statement of responsibility">%s</mods:note>
                    <mods:originInfo>
                        <mods:dateIssued encoding="w3cdtf">%s</mods:dateIssued>
                       <mods:dateCreated qualifier="approximate">%s</mods:dateCreated>
                    </mods:originInfo>
                    <mods:titleInfo lang="English">
                        <mods:title>%s</mods:title>
                        <mods:subTitle>%s</mods:subTitle>
                    </mods:titleInfo>
                    <mods:physicalDescription>   
                          <mods:extent>%s</mods:extent>
                    </mods:physicalDescription>  
                    <mods:genre authority="att">%s</mods:genre>
                    <mods:typeOfResource>text</mods:typeOfResource>
                </mods:mods>
            </mets:xmlData>
        </mets:mdWrap>
    </mets:dmdSec>\n''' % (
        config['rights'], config['publisher'],config['date_issued'], config['date_created'], config['title'], config['sub_title'],
        config['dimensions'], config['type'])

    fh.write(s1 + s2 + s3)


def mets_file_group(filenames, filetype, fh):
    struct_map = ""
    fh.write('<!--FILE SECTION-->\n    <mets:fileSec>\n')

    file_group_number = 0
    skip = 0
    # iterate over list of root file names in integer order
    for count, my_file in enumerate(filenames):
        if skip:  # skip iterating foldouts again - they were done in previous group
            # skip = 0
            skip -= 1
            continue
        else:
            file_group_number += 1
        s = '        <mets:fileGrp ID="pageFileGrp%d">\n' % (file_group_number)

        insertre = re.compile('.*insert.*')  # 007_inserta   - determine if type 'page' or 'insert'
        if (insertre.search(my_file)):
            pageType = 'insert'
        else:
            pageType = 'page'

        struct_map += '          <mets:div TYPE="%s" DMDID="pageFileGrp%d" LABEL="Page %s">\n' % (
            pageType, file_group_number, file_group_number)
        fh.write(s)

        # printing the mets filegroup and loading up the structMap all in one to keep consistent naming/structure and
        # dry
        struct_map = print_mets_file(file_group_number, filetype, my_file, 0, fh,
                                    struct_map)  # note that foldout is always 0 (no) here

        #### check here for if next is a foldout then write those files here and increment count
        foldout = re.compile('(foldout)(.*)')  # 007_foldouta => foldout, a
        localcount = count
        while (len(filenames) != localcount + 1) and foldout.search(
                filenames[localcount + 1]):  # not at end of list and next thing is a foldout
            # print ('NEXT FILE IS A FOLDOUT: ', filenames[count+1] )
            fileGroupNumberFoldout = str(file_group_number) + foldout.search(filenames[localcount + 1]).group(
                2)  # append 'a', etc to fileGroupNumber
            struct_map = print_mets_file(fileGroupNumberFoldout, filetype, filenames[localcount + 1], 1, fh,
                                        struct_map)  # foldout always 1 (yes) here
            skip += 1  # skip this one which is next up in loop
            localcount += 1

        fh.write('        </mets:fileGrp>\n')
        struct_map += '          </mets:div>\n'
    fh.write('    </mets:fileSec>\n')
    return struct_map


def print_mets_file(file_group_number, filetype, the_file, foldout, fh, struct_map):
    for extension in filetype:  # write out a line for each type of file in the filetype list
        if extension == "jp2":
            use = "service"
        elif extension == "pdf":
            use = "pdf"
        elif extension == "xml":
            use = "ocr"

        if foldout:  # special use fields for foldouts
            if use == "ocr":
                use = "foldoutocr"
            else:
                use = "foldout"

        struct_map += '               <mets:fptr FILEID="%sFile%s" />\n' % (use, file_group_number)
        fh.write('              <mets:file ID="%sFile%s" USE="%s" >\n' % (use, file_group_number, use))
        fh.write('                   <mets:FLocat LOCTYPE="OTHER" OTHERLOCTYPE="file" xlink:href="%s.%s" /> \n' % (
            the_file, extension))
        fh.write('              </mets:file>\n')
    return struct_map


def mets_struct_map(metsstructMapdivs, bt, bst, fh):
    fh.write('<!--STRUCTURAL MAP-->\n')
    fh.write('  <mets:structMap TYPE="physical">\n')
    fh.write('     <mets:div TYPE="book" LABEL="%s %s" DMDID="DMD1"> \n' % (attribute_escape(bt), attribute_escape(bst)))
    fh.write(metsstructMapdivs)
    fh.write('     </mets:div> \n')
    fh.write('</mets:structMap>\n')


def get_int(file):
    partsd = file.split(".")  # page007.xml page016_a.xml
    parts = partsd[0].split("_")
    return int(parts[0])


def create_mets_file(output_dir, config, file_names):
    """
    Creates a mets file using the provided metadata configuration and root file names.

    :param output_dir: the full path to the output directory for the item being processed
    :param config: metadata values to be added to mods section
    :param file_names: ordered list of the base file names without extensions
    :return:
    """
    config = sanitize_metadata(config)
    fh = open(output_dir + '/mets.xml', 'wt')
    filetype = ['jp2', 'xml']  # types of files that will end up in METS file
    createdate = time.strftime("%Y-%m-%dT%H:%M:%S")
    mets_hdr_dmd_sec(config, createdate, fh)
    mets_struct_map_divs = mets_file_group(file_names, filetype, fh)
    mets_struct_map(mets_struct_map_divs, config['title'], config['sub_title'], fh)
    fh.write('</mets:mets>\n')
    print(f'\nMETS file created for directory: {output_dir}')
    fh.close()


def sanitize_metadata(config):
    """
    Basic escape for all metadata inputs
    :param config: dictionary of metadata
    :return:
    """
    try:
        for key in config.keys():
            config[key] = config[key].replace("&", "&amp;")
            config[key] = config[key].replace("<", "&lt;")
            config[key] = config[key].replace(">", "&gt;")
    except Exception as error:
        print(error)

    return config


def attribute_escape(value):
    """
    Additional escaping for attribute values
    :param value: the attribute value
    :return:
    """
    value = value.replace("\"", "&quot;")
    value = value.replace("\'", "&apos;")
    return value