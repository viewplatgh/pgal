import sys
import argparse
import pgal_main


thePgal = pgal_main.PgalMainApp()
parser = argparse.ArgumentParser()
parser.add_argument('-t', '--target', 
                                help='path to the folder contains gallery resources need to be converted to web pages', 
                                required=True, 
                                metavar='')
parser.add_argument('-r', '--root-template',
                                help='path to xslt template for root folder of the gallery',
                                required=True,
                                metavar='')
parser.add_argument('-s', '--sub-template', help='xslt template for 2nd level folder of the gallery, if it\'s omitted, --root-template will be used instead', metavar='')
parser.add_argument('-l', '--tvl-template', help='xslt template for 3rd and other even lower level folder of the gallery, if it\'s omitted, will try to use --sub-template', metavar='')
parser.add_argument('-i', '--index-page-name', help='if specified, it will be used as filename to create the web page instead of the folder name', metavar='')
parser.add_argument('-j', '--js-files', help='path to javascript files(separated by \',\' if multiple) to be copied to the \'js\' folder in the target', metavar='')
parser.add_argument('-c', '--css-files', help='path to css files(separated by \',\' if multiple) to be copied to the \'css\' folder in the target', metavar='')
parser.add_argument('-o', '--home', default='home', help='home directory name of the web pages, default value is \'home\'', metavar='')

thePgal.main(parser.parse_args())