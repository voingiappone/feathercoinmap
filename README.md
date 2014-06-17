FeatherCoinMap
=======
A fork of CoinMap().

<http://feathercoinmap.org/> ### temporary non-definitive address ###

Map showing all the shops accepting Feathercoin around the world.

Donations welcome at:
* 71x4LXb1mseqVPW1pXncsKKy9sb1Cx4YBe (Feathercoin)
* 1BzbfqCeiJu6CNVZDSbM9jAX8HyE2Fq6FD (Bitcoin)


* Licensed under [Affero General Public License 3](http://www.gnu.org/licenses/agpl-3.0.html)
* Map Data © by [OpenStreetMap contributors](http://www.openstreetmap.org/copyright)
* Map Icons CC-0 by [Brian Quinion](http://www.sjjb.co.uk/mapicons/)
* Feathercoin logo by [attribution](http://www.feathercoin.org/


-- Installing 

Clone the repository directly inside the htdocs folder of a webserver:

    git clone https://github.com/voingiappone/feathercoinmap

Dependencies on Ubuntu linux:

* a working web server (try xampp[https://www.apachefriends.org/download.html] for an easy-to-install environment)
* python
* python-requests > 2.3.0
* python-crypto
* python-gevent
* python-greenlet
* python-oauthlib
* python-urllib3

-- Updating the library

Once the environment execute the database update script:

    cd MY_INSTALL_DIR/data
    ./refresh.py
  
This will create the proper files to display the icons on the map.
Each OSM map update will take 3 to 5 minutes to be available on the map.
The refresh.py script can be executed by a properly set-up cron job to
have an always up-to-date map.
