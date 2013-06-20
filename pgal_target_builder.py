import shutil
from os import listdir
from os import path
from lxml import etree
from pgal_xhtml_creator import PgalXhtmlCreator
import imghdr

class PgalTargetBuilder:


    def buildTarget(self, targetPath, xsltPath, location=[]):
        rootNode = etree.Element('root')
        locationNode = etree.SubElement(rootNode, 'location')
        for locationItem in location:
            etree.SubElement(locationNode, 'folder').text = str(locationItem)

        fileList = []
        dirList = []
        for diritem in listdir(targetPath):
            subTargetPath = path.join(targetPath, diritem)
            if path.isfile(subTargetPath):
                fileList.append(diritem)
            if path.isdir(subTargetPath):
                dirList.append(diritem)

        for item in dirList:
            subTargetPath = path.join(targetPath, item)
            self.buildTarget(subTargetPath, xsltPath, location + [item])
            dirNode = etree.SubElement(rootNode, 'folder')
            etree.SubElement(dirNode, 'name').text = item
    
        for item in fileList:
            subTargetPath = path.join(targetPath, item)
            if imghdr.what(subTargetPath) is not None: 
                fileNode = etree.SubElement(rootNode, 'file')
                etree.SubElement(fileNode, 'name').text = item

        targetXmlPath = path.join(targetPath, '%s.xml' % (location[-1]))
        with open(targetXmlPath, 'wb') as xmlFile:
            xmlFile.write(etree.tostring(rootNode, pretty_print=True, xml_declaration=True, encoding='utf-8'))
        
        xhtmlCreator = PgalXhtmlCreator()
        targetXsltPath = path.join(targetPath, '%s.xsl' % format(location[-1])) 
        shutil.copy2(xsltPath, targetXsltPath)
        xhtmlCreator.createXhtml(targetXmlPath, targetXsltPath)    
         


