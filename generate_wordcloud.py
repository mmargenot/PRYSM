import history
import re
import urllib

import matplotlib.pyplot as plt
from optparse import OptionParser

from exceptions import ValueError


parser = OptionParser()
parser.add_option("-d", "--dir", dest="dir", help="Location of the search history DB")
parser.add_option

options, arguments = parser.parse_args()

data_dir = arguments.dir

history =
