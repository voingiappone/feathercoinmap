#!/usr/bin/python
import os
import json
from overpass import parser as overpass_parser

scriptdir = os.path.dirname(os.path.abspath(__file__))

coins = [
    'Feathercoin'
]

parsers = {
	'overpass': overpass_parser,
}

# update data/currencies
with open(scriptdir + '/coins.js', 'w') as f:
	f.write('function get_coins() { return ["%s"]; }\n' % '", "'.join(coins))

# call individual parsers
for name, parser in parsers.iteritems():
	for coin in coins:
		coin = coin.lower()
		pts = parser.get_points(coin)
		json.dump(pts, open(scriptdir + '/data-%s-%s.json' % (name, coin), 'w'), separators = (',', ':'))
