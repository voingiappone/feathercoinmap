function coinmap() {

  var tileOSM = L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: 'Data &copy; by <a href="http://www.openstreetmap.org/copyright">OpenStreetMap contributors</a>.',
    maxZoom: 18
  });

  var tileToner = L.tileLayer('http://{s}.tile.stamen.com/toner/{z}/{x}/{y}.png', {
    attribution: 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, under <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a>. Data &copy; by <a href="http://www.openstreetmap.org/copyright">OpenStreetMap contributors</a>.',
    maxZoom: 18
  });

  var tileWatercolor = L.tileLayer('http://{s}.tile.stamen.com/watercolor/{z}/{x}/{y}.png', {
    attribution: 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, under <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a>. Data &copy; by <a href="http://www.openstreetmap.org/copyright">OpenStreetMap contributors</a>.',
    maxZoom: 16
  });

  var tileMapQuest = L.tileLayer('http://{s}.mqcdn.com/tiles/1.0.0/map/{z}/{x}/{y}.png', {
    subdomains: ['otile1','otile2','otile3','otile4'],
    attribution: 'Map tiles by <a href="http://open.mapquestapi.com/">MapQuest</a>. Data &copy; by <a href="http://www.openstreetmap.org/copyright">OpenStreetMap contributors</a>.',
    maxZoom: 18
  });

  var tileMapQuestAerial = L.tileLayer('http://{s}.mqcdn.com/tiles/1.0.0/sat/{z}/{x}/{y}.png', {
    subdomains: ['otile1','otile2','otile3','otile4'],
    attribution: 'Portions Courtesy NASA/JPL-Caltech and U.S. Depart. of Agriculture, Farm Service Agency. Data &copy; by <a href="http://www.openstreetmap.org/copyright">OpenStreetMap contributors</a>.',
    maxZoom: 18
  });

  var map = L.map('map', { center: [0, 0], zoom: 3, layers: [tileOSM], worldCopyJump: true });

  var layers = L.control.layers({
    "OpenStreetMap": tileOSM,
    "MapQuestOpen": tileMapQuest,
    "MapQuestOpenAerial": tileMapQuestAerial,
    "Toner": tileToner,
    "Watercolor": tileWatercolor,
  }).addTo(map);

  var c_clusters = {};
  var currencies = get_currencies();
  for (var i = currencies.length - 1; i >= 0; i--) {
    c_clusters[currencies[i]] = new L.MarkerClusterGroup({showCoverageOnHover: false, maxClusterRadius: 32});
  }


  coinmap_populate_overpass(c_clusters);
//  coinmap_populate_localbitcoins(markers);
//  coinmap_populate_zipzap(markers);

  for (var i = c_clusters.length - 1; i >= 0; i--) {
    map.addLayer(c_clusters[i]);
  }

  map.on('moveend', function(e){
    if(map.getZoom() >= 13){
      document.getElementById("osm_edit_link").href = "http://www.openstreetmap.org/edit#map=" + map.getZoom() + "/" + map.getCenter().lat.toFixed(6) + "/" + map.getCenter().lng.toFixed(6);
    }
    else{
      document.getElementById("osm_edit_link").href = "http://www.openstreetmap.org/edit#map=13/" + map.getCenter().lat.toFixed(6) + "/" + map.getCenter().lng.toFixed(6);
    }
  });

  map.locate({setView: true, maxZoom: 12});

  map.addControl(new L.Control.Permalink({text: 'Permalink', layers: layers, position: "none", useLocation: true}));
}
