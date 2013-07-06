import os
from lxml import etree

class PgalXhtmlCreator:
    def createXhtml(self, xmlFilePath, xslFilePath):
        xslFileObj = etree.parse(xslFilePath, etree.XMLParser(remove_blank_text=True))
        xslTransform = etree.XSLT(xslFileObj)
        xmlFileObj = etree.parse(xmlFilePath)
        result = xslTransform(xmlFileObj)
        pathPair = os.path.split(xmlFilePath)

        with open(os.path.join(pathPair[0], ('%s.html' % (os.path.splitext(pathPair[1])[0]))), 'w', encoding='utf-8') as resultFile:
            resultFile.write(str(result))