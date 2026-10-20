import csv
import os

from shared_python.Args import Args
from shared_python.Common import recursive_story_listdir
from shared_python.Logging import logger
#from shared_python.Parsers import LinkParser
from shared_python.Requests import RequestHandler

# initialize log
# initialize arguments
#   need to add in the domain of the original site to the arguments file
# initialize requests and headers
# initialize csv
# parse files as html; how to parse if they are .txt files?
# return list of hrefs
# for list of hrefs:
# send head request
# write resulting dict rows to csv, using working directory from the ODAP