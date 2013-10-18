#!/usr/bin/python
import os
from localbitcoins import parser as localbitcoins_parser
from overpass import parser as overpass_parser
from zipzap import parser as zipzap_parser

scriptdir = os.path.dirname(os.path.abspath(__file__))

with open(scriptdir + '/data-overpass.js', 'w') as f:
  f.write('function coinmap_populate_overpass(markers) {\n')
  overpass_parser.write_markers(f)
  f.write('}\n')

"""
with open(scriptdir + '/data-localbitcoins.js', 'w') as f:
  f.write('function coinmap_populate_localbitcoins(markers) {\n')
  localbitcoins_parser.write_markers(f)
  f.write('}\n')
"""

"""
with open(scriptdir + '/data-zipzap.js', 'w') as f:
  f.write('function coinmap_populate_zipzap(markers) {\n')
  zipzap_parser.write_markers(f)
  f.write('}\n')
"""
