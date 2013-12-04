import requests

usa_cities = 'zipzap/usa_cities.csv'
merchantIDs = {
    'bitcoin': 946,
    'litecoin': 946
}

def get_usa_cities():
    cities = []
    with open(usa_cities, 'rb') as cities_file:
        for line in cities_file:
            cities.append(line.strip())
    return cities

def call_zipzap(location, merchantid):
    json = requests.get('https://www.cashpayment.com/API/PaymentCenter',
                        params = {'searchAddress': location, 'MerchantID': merchantid}).json()
    return json

def convert_to_coinmap(data, currency):
    j = {
        'id': data['ID'],
        'name': data['PaymentCenterName'],
        'lat': data['GeoLat'],
        'lon': data['GeoLong'],
        'type': 'node',
        'tags': {
            'zipzap': 'zipzap',
            'addr:city': data['City'],
            'add:country': 'USA',
        },
        'website': 'http://zipzapinc.com'
    }
    j['tags']['payment:' + currency] = 'yes'
    return j

def get_points():
    cities = get_usa_cities()
    result = {}
    for c in cities:
        for currency,i in merchantIDs.iteritems():
            data = call_zipzap(c, i)
            for point in data:
                zipzap_loc = convert_to_coinmap(point, currency)
                if zipzap_loc['id'] not in result:
                    result[zipzap_loc['id']] = zipzap_loc
                else:
                    # id in results, so if it supports multiple currencies, add this one
                    if "payment:"+currency not in result[zipzap_loc['id']]['tags']:
                        result[zipzap_loc['id']]['tags']['payment:'+currency] = 'yes'
    return result.values()
