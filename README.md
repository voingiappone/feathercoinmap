FeatherCoinMap
=======
A fork of CoinMap().

<http://voingiappone.altervista.org/feathercoinmap/> ### Temporary installation to see the map in action ###

Map showing all the shops accepting Feathercoin around the world.

Donations welcome at:
* 71x4LXb1mseqVPW1pXncsKKy9sb1Cx4YBe (Feathercoin)
* 1BzbfqCeiJu6CNVZDSbM9jAX8HyE2Fq6FD (Bitcoin)


* Licensed under [Affero General Public License 3](http://www.gnu.org/licenses/agpl-3.0.html)
* Map Data © by [OpenStreetMap contributors](http://www.openstreetmap.org/copyright)
* Map Icons CC-0 by [Brian Quinion](http://www.sjjb.co.uk/mapicons/)
* Feathercoin logo by [NickCoin](https://bitcointalk.org/index.php?topic=196168.0)


## Installing 

Clone the repository directly inside the htdocs folder of a webserver:

    git clone https://github.com/voingiappone/feathercoinmap

##Dependencies on Ubuntu linux:

* a working web server (try [xampp](https://www.apachefriends.org/download.html) for an easy-to-install environment)
* python
* python-requests > 2.3.0
* python-crypto
* python-gevent
* python-greenlet
* python-oauthlib
* python-urllib3

## Updating the library

Once the environment is properly set-up execute the database update script:

    cd MY_INSTALL_DIR/data
    ./refresh.py
  
This will create the proper files to display the icons on the map.
Each and every new venue addition on the OSM site will take 3 to 5 minutes to be available on the map.
The refresh.py script can be executed by a properly set-up cron job to
have an always up-to-date map.

## Update scheduling

Two methods can be used to schedule a periodical update of the database:

* a script
* a Cron job

The script approach is just as easy as it is inelegant. A script is created with the preferred text
editor containing the lines:

    #!/bin/bash
    
    i=0    
    while [ $i = 0 ]
     do
      MY_INSTALL_DIR/data/refresh.py	#execute the update
      sleep 3600						#waits for 60 minutes
     done

Once you have given it the permission for execution with `chmod 777 my_auto_updater` you only have to launch it.

The cron job, on the contrary, represents the more stilistically appealing solution and is the suggested one.
First of all you need to open your crontab:

    crontab -e

You may be asked to select your default editor here. Once in just type this string, save and exit:

    * */1 * * * /MY_INSTALL_DIR/data/refresh.py
    
This will take care of running the update script every hour on your behalf.
