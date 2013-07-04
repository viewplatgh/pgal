import shutil
from os import listdir
from os import path
from lxml import etree
from pgal_xhtml_creator import PgalXhtmlCreator
import imghdr

class PgalTargetBuilder:


    def buildTarget(self, targetPath, xsltPath, location=[]):
        rootNode = etree.Element('root')
        rootNameNode = etree.SubElement(rootNode, 'name')
        rootNameNode.text = path.basename(path.normpath(targetPath))
        locationNode = etree.SubElement(rootNode, 'location')

        # create location node
        #if len(location) > 0:
        #    folderNode = etree.SubElement(locationNode, 'folder')            
        #    dotPath = './'
        #    for item in location[1:]:
        #        dotPath += '../'
        #    etree.SubElement(folderNode, 'name').text = str(location[0])
        #    etree.SubElement(folderNode, 'url').text = dotPath

        dotPath = './'
        for item in location[1:]:
            dotPath += '../'
        locationPath = ''
        for locationItem in location:
            folderNode = etree.SubElement(locationNode, 'folder')
            etree.SubElement(folderNode, 'name').text = str(locationItem)
            # skip the 'home' location
            if locationItem != location[0]:
                locationPath = path.join(locationPath, str(locationItem))                       
            etree.SubElement(folderNode, 'url').text = str(path.join(dotPath, locationPath)).replace('\\', '/')

        fileList = []
        dirList = []
        # get files and dirs in targetPath
        for diritem in listdir(targetPath):
            subTargetPath = path.join(targetPath, diritem)
            if path.isfile(subTargetPath):
                fileList.append(diritem)
            if path.isdir(subTargetPath):
                dirList.append(diritem)

        # create sub dir nodes
        for item in dirList:
            subTargetPath = path.join(targetPath, item)
            self.buildTarget(subTargetPath, xsltPath, location + [item])
            dirNode = etree.SubElement(rootNode, 'folder')
            etree.SubElement(dirNode, 'name').text = item
    
        # create sub file nodes
        for item in fileList:
            subTargetPath = path.join(targetPath, item)
            if imghdr.what(subTargetPath) is not None: 
                fileNode = etree.SubElement(rootNode, 'file')
                etree.SubElement(fileNode, 'name').text = item

        # save the xml dir structure file
        targetXmlPath = path.join(targetPath, '%s.xml' % (location[-1]))
        with open(targetXmlPath, 'wb') as xmlFile:
            xmlFile.write(etree.tostring(rootNode, pretty_print=True, xml_declaration=True, encoding='utf-8'))
        
        # copy the xslt template to taget folder
        xhtmlCreator = PgalXhtmlCreator()
        targetXsltPath = path.join(targetPath, '%s.xsl' % format(location[-1])) 
        shutil.copy2(xsltPath, targetXsltPath)
        
        # generate .html web pages
        xhtmlCreator.createXhtml(targetXmlPath, targetXsltPath)    
         


