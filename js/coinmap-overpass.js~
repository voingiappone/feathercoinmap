function coinmap_populate_overpass(cluster, coin) {
	coin = coin.toLowerCase();
	$.getJSON('data/data-overpass-' + coin + '.json', function(data) {
        $.each(data, function(key, val) {
			var lat = val['lat'];
			var lon = val['lon'];
			var title = val['title'];
			var icon = window.coinmap_icons[val['icon']];
			var popup = '<b>' + val['title'] + '</b> <a href="http://openstreetmap.org/browse/' + val['type'] + '/' + val['id'] + '" target="_blank">*</a><hr/>';
			if (val['addr']) {
				popup += val['addr'] + '<br/>';
			}
			if (val['city']) {
				popup += val['city'] + '<br/>';
			}
			if (val['country']) {
				popup += val['country'] + '<br/>';
			}
			popup += '<hr/>';
			if (val['web']) {
				popup += '<span data-l10n="website-">website</span>: <a href="' + val['web'] + '" target="_blank">' + val['web'] + '</a><br/>';
			}
			if (val['email']) {
				popup += '<span data-l10n="email">e-mail</span>: <a href="mailto:' + val['email'] + '" target="_blank">' + val['email'] + '</a><br/>';
			}
			if (val['phone']) {
				popup += '<span data-l10n="phone-">phone</span>: ' + val['phone'] + '<br/>';
			}
			if (val['desc']) {
				popup += val['desc'] + '<br/>';
			}
            popup='<div class="mydoge">'+popup+'</div>';
			L.marker([lat, lon], {"title": title, icon: icon}).bindPopup(popup).addTo(cluster);
		});
        if (coin=="dogecoin") {
		    document.getElementById(coin + "_count").innerHTML = data.length;
	    }
    });
}
