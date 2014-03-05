import shutil
import os
from os import listdir
from os import path
from lxml import etree
from pgal_xhtml_creator import PgalXhtmlCreator
import imghdr

class PgalTargetBuilder:
    def recursiveBuildTarget(self, targetPath, xsltPath, subXsltPath, tvlXsltPath, location, jsFiles, idxPageName, cssFiles):
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
            urlFileName = idxPageName if idxPageName is not None else ('%s.html' % locationItem)
            etree.SubElement(folderNode, 'url').text = str(os.path.join(dotPath, locationPath, urlFileName)).replace('\\', '/')

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
            self.recursiveBuildTarget(subTargetPath, xsltPath, subXsltPath, tvlXsltPath, location + [item], jsFiles, idxPageName, cssFiles)
            dirNode = etree.SubElement(rootNode, 'folder')
            etree.SubElement(dirNode, 'name').text = item
            urlFileName = idxPageName if idxPageName is not None else ('%s.html' % item)
            etree.SubElement(dirNode, 'url').text = str(os.path.join('./', item, urlFileName)).replace('\\', '/')
    
        # create sub file nodes
        for item in fileList:
            subTargetPath = path.join(targetPath, item)
            if imghdr.what(subTargetPath) is not None: 
                fileNode = etree.SubElement(rootNode, 'file')
                etree.SubElement(fileNode, 'name').text = item
                etree.SubElement(fileNode, 'url').text = str(os.path.join('./', item)).replace('\\', '/')

        # save the xml dir structure file
        targetXmlPath = path.join(targetPath, '%s.xml' % (location[-1]))
        with open(targetXmlPath, 'wb') as xmlFile:
            xmlFile.write(etree.tostring(rootNode, pretty_print=True, xml_declaration=True, encoding='utf-8'))
        
        # copy the xslt template to taget folder
        xhtmlCreator = PgalXhtmlCreator()
        targetXsltPath = path.join(targetPath, '%s.xsl' % format(location[-1])) 
        
        xsltPathToUse = xsltPath if len(location) == 1 else subXsltPath if len(location) == 2 else tvlXsltPath
        shutil.copy2(xsltPathToUse, targetXsltPath)
        
        # generate .html web pages
        xhtmlCreator.createXhtml(targetXmlPath, targetXsltPath, idxPageName)

    def preBuildTarget(self, targetPath, xsltPath, subXsltPath, tvlXsltPath, location, jsFiles, idxPageName, cssFiles):
        pass

    def postBuildTarget(self, targetPath, xsltPath, subXsltPath, tvlXsltPath, location, jsFiles, idxPageName, cssFiles):
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

    def buildTarget(self, args):
        targetPath = args.target
        xsltPath = args.root_template
        subXsltPath = args.sub_template if args.sub_template is not None else xsltPath
        tvlXsltPath = args.tvl_template if args.tvl_template is not None else subXsltPath
        idxPageName = args.index_page_name
        location = [args.home]
        jsFiles = args.js_files.split(',')
        cssFiles = args.css_files.split(',')
        self.preBuildTarget(targetPath, xsltPath, subXsltPath, tvlXsltPath, location, jsFiles, idxPageName, cssFiles)
        self.recursiveBuildTarget(targetPath, xsltPath, subXsltPath, tvlXsltPath, location, jsFiles, idxPageName, cssFiles)
        self.postBuildTarget(targetPath, xsltPath, subXsltPath, tvlXsltPath, location, jsFiles, idxPageName, cssFiles)