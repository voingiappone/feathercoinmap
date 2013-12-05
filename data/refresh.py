#!/usr/bin/python
import os
from localbitcoins import parser as localbitcoins_parser
from overpass import parser as overpass_parser
from zipzap import parser as zipzap_parser

scriptdir = os.path.dirname(os.path.abspath(__file__))

currencies = [
    'bitcoin',
    'litecoin'
]

parsers = {
  'overpass': overpass_parser,
#  'localbitcoins': localbitcoins_parser,
#  'zipzap': zipzap_parser,
}

cnt = 0
for name, parser in parsers.iteritems():
    with open(scriptdir + '/data-%s.js' % name, 'w') as f:
        f.write('function coinmap_populate_%s(cluster) {\n' % name)
        for currency in currencies:
            if currency in parser.supports():
                cnt = parser.write_markers(f, currency, cnt)

        f.write('}\n')

# Update data/currencies
with open(scriptdir + '/currencies.js', 'w') as f:
    currency_str = "function get_currencies() {\n return ["
    for currency in currencies:
        currency_str += "'%s'," % currency

    currency_str = currency_str[:-1]
    currency_str += "];\n}\n"
    f.write(currency_str)