import shutil
import os
from os import listdir
from os import path
from lxml import etree
from pgal_xhtml_creator import PgalXhtmlCreator
import imghdr

class PgalTargetBuilder:
    def recursiveBuildTarget(self, targetPath, xsltPath, location, jsFiles, cssFiles):
        rootNode = etree.Element('root')

        # process name node, is to declare the node's name
        rootNameNode = etree.SubElement(rootNode, 'name')
        rootNameNode.text = os.path.basename(os.path.normpath(targetPath))
        if len(location) == 0:
            location.append(rootNameNode.text)
        
        # process location node
        locationNode = etree.SubElement(rootNode, 'location')
        dotPath = './'
        for item in location[1:]:
            dotPath += '../'
        locationPath = ''
        for locationItem in location:
            folderNode = etree.SubElement(locationNode, 'folder')
            etree.SubElement(folderNode, 'name').text = str(locationItem)
            # skip the first location, as it's url should be './'
            if locationItem != location[0]:
                locationPath = os.path.join(locationPath, str(locationItem))                       
            etree.SubElement(folderNode, 'url').text = str(os.path.join(dotPath, locationPath)).replace('\\', '/')

        # process js node
        jsNode = etree.SubElement(rootNode, 'js')
        for jsItem in jsFiles:
            jsFileName = os.path.basename(os.path.normpath(jsItem))
            etree.SubElement(jsNode, 'url').text = str(os.path.join(dotPath, 'js', jsFileName)).replace('\\', '/')
        
        #process css node
        cssNode = etree.SubElement(rootNode, 'css')
        for cssItem in cssFiles:
            cssFileName = os.path.basename(os.path.normpath(cssItem))
            etree.SubElement(cssNode, 'url').text = str(os.path.join(dotPath, 'css', cssFileName)).replace('\\', '/')
        
        fileList = []
        dirList = []
        # get files and dirs in targetPath
        for diritem in os.listdir(targetPath):
            subTargetPath = path.join(targetPath, diritem)
            if path.isfile(subTargetPath):
                fileList.append(diritem)
            if path.isdir(subTargetPath):
                dirList.append(diritem)

        # create sub dir nodes
        for item in dirList:
            subTargetPath = path.join(targetPath, item)
            self.recursiveBuildTarget(subTargetPath, xsltPath, location + [item], jsFiles, cssFiles)
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

    def preBuildTarget(self, targetPath, xsltPath, location, jsFiles, cssFiles):
        pass

    def postBuildTarget(self, targetPath, xsltPath, location, jsFiles, cssFiles):
        def buildIncludeFiles(fileslist, subdirname):
            for onefile in fileslist:
                fileName = os.path.basename(os.path.normpath(onefile))
                subTargetPath = str(os.path.join(targetPath, subdirname, fileName)).replace('\\', '/')
                subTargetDir = os.path.dirname(subTargetPath)
                if not os.path.exists(subTargetDir):
                    os.makedirs(subTargetDir)
                shutil.copy2(onefile, subTargetPath)
        
        buildIncludeFiles(jsFiles, 'js')
        buildIncludeFiles(cssFiles, 'css')

    def buildTarget(self, targetPath, xsltPath, location=[], jsFiles=[], cssFiles=[]): 
        self.preBuildTarget(targetPath, xsltPath, location, jsFiles, cssFiles)
        self.recursiveBuildTarget(targetPath, xsltPath, location, jsFiles, cssFiles)
        self.postBuildTarget(targetPath, xsltPath, location, jsFiles, cssFiles)