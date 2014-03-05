import sys
import argparse
from pgal_xhtml_creator import PgalXhtmlCreator
from pgal_target_builder import PgalTargetBuilder

class PgalMainApp:    
    def unit_test0(self):
        xhtmlCreator = PgalXhtmlCreator()
        xhtmlCreator.createXhtml('./sample0.xml', './sample0.xsl')

    def unit_test1(self):
        xtb = PgalTargetBuilder()
        xtb.buildTarget('./sample0', './sample0.xsl', ['home'])

    def unit_test2(self):
        xtb = PgalTargetBuilder()
        xtb.buildTarget('./sample0', './sample0.xsl', [])

    def unit_test3(self):
        xtb = PgalTargetBuilder()
        xtb.buildTarget('./sample0', './lightbox.xsl', [], ['./js/jquery.js', './js/slimbox2.js'], ['./css/slimbox2.css'])
           
    def main(self, args):
        PgalTargetBuilder().buildTarget(args)
        print('built successfully')