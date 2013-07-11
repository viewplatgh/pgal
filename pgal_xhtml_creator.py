import os
from lxml import etree

class PgalXhtmlCreator:
    def createXhtml(self, xmlFilePath, xslFilePath, idxPageName):
        try:
            xslFileObj = etree.parse(xslFilePath, etree.XMLParser(remove_blank_text=True))
            xslTransform = etree.XSLT(xslFileObj)
            xmlFileObj = etree.parse(xmlFilePath)
            result = xslTransform(xmlFileObj)
            pathPair = os.path.split(xmlFilePath)

            pageFileName = idxPageName if idxPageName is not None else ('%s.html' % (os.path.splitext(pathPair[1])[0]))
            with open(os.path.join(pathPair[0], pageFileName), 'w') as resultFile:
                resultFile.write(str(result))
        except:
            pass
        finally:
            pass