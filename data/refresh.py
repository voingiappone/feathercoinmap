#!/usr/bin/python
import os
import json
# from localbitcoins import parser as localbitcoins_parser
from overpass import parser as overpass_parser
# from zipzap import parser as zipzap_parser

scriptdir = os.path.dirname(os.path.abspath(__file__))

parsers = {
    'overpass': overpass_parser,
#    'localbitcoins': localbitcoins_parser,
#    'zipzap': zipzap_parser,
}

for name, parser in parsers.iteritems():
    pts = parser.get_points()
    json.dump(pts, open(scriptdir + '/data-%s.json' % name, 'w'), separators = (',', ':'))
