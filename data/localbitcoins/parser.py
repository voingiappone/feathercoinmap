import requests

def page(uri, data):
    json = requests.get(uri).json()
    next_uri = json['pagination'].get('next', None)
    for ad in json['data']['ad_list']:
        data.append(ad)
    return next_uri

def get_points():
    data = []

    uri = 'https://localbitcoins.com/buy-bitcoins-online/.json'
    while uri:
        print uri
        uri = page(uri, data)

    uri = 'https://localbitcoins.com/sell-bitcoins-online/.json'
    while uri:
        print uri
        uri = page(uri, data)

    return data

def write_elements(f, e):
    e = e.get('data')

    lat = e.get('lat', None)
    lon = e.get('lon', None)
    if not lat or not lon:
        return

    ide = str(e.get('ad_id'))
    profile = e.get('profile', None)
    if profile:
        name = profile.get('name', '?')
    else:
        name = '?'
    icon = 'localbitcoins'
    popup = '<b>%s</b><hr/>' % name
    popup += 'address: %s' % e.get('location_string', '')
    popup += 'website: <a href=\\"https://localbitcoins.com/ad/%s\\" target=\\"_blank\\">https://localbitcoins.com/ad/%s</a>' % (ide, ide)
    f.write('  L.marker([%s, %s], {"title": "%s", icon: icon_%s}).bindPopup("%s").addTo(markers);\n' % (lat, lon, name.encode('utf-8'), icon, popup.encode('utf-8')))

def write_markers(f):
    for p in get_points():
        write_elements(f, p)
