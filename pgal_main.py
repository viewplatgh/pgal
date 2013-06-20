import sys
import getopt
from pgal_folder_parser import PgalFolderParser
from pgal_xhtml_creator import PgalXhtmlCreator
from pgal_target_builder import PgalTargetBuilder

class PgalMainApp:

    argv = sys.argv[1:]
    targetPath = ''
    rootTemplate = ''
    subTemplate = ''
    tvlTemplate = ''

    def unit_test0(self):
        xhtmlCreator = PgalXhtmlCreator()
        xhtmlCreator.createXhtml('./sample0.xml', './sample0.xsl')

    def unit_test1(self):
        xtb = PgalTargetBuilder()
        xtb.buildTarget('./sample0', './sample0.xsl', ['home'])

    def main(self):
#        self.unit_test()
        self.unit_test1()

        print(len(sys.argv))
        print(sys.argv)
        parser = PgalFolderParser()
        print(type(parser))
        try:
            opts, args = getopt.getopt(self.argv, 'ht:r:s:l:', ['help=','target', 'root-template', 'sub-template', 'tvl-template'])
            for opt, arg in opts:
                if opt in ('-h', '--help'):
                    raise getopt.GetoptError;
                elif opt in ('-t', '--target'):
                    self.targetPath = arg
                elif opt in ('-r', '--root-template'):
                    self.rootTemplate = arg
                elif opt in ('-s', '--sub-template'):
                    self.subTemplate = arg
                elif opt in ('-l', '--tvl-template'):
                    self.tvlTemplate = arg
        except getopt.GetoptError:
            print('pgal.py')
            return

thePgal = PgalMainApp()
thePgal.main()