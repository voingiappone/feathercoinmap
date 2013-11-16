#!/usr/bin/python
import os
from localbitcoins import parser as localbitcoins_parser
from overpass import parser as overpass_parser
from zipzap import parser as zipzap_parser

scriptdir = os.path.dirname(os.path.abspath(__file__))

parsers = {
  'overpass': overpass_parser,
#  'localbitcoins': localbitcoins_parser,
#  'zipzap': zipzap_parser,
}

for name, parser in parsers.iteritems():
  with open(scriptdir + '/data-%s.js' % name, 'w') as f:
    f.write('function coinmap_populate_%s(markers) {\n' % name)
    parser.write_markers(f)
    f.write('}\n')
