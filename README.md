Screenly-manager
=======

A simple manager for the screenly OSE software


Screenshots
============
Install x11-apps and imagemagick on clients:

    $ sudo apt-get install x11-apps imagemagick -y

Download screenshot script:

    $ wget https://github.com/svdgraaf/screenly-manager/raw/master/bin/screenshot.sh -O /home/pi/screenshot.sh

Edit crontab
    $ crontab -e

Add this line (this will take a screenshot every 5 minutes):
    */5 * * * * /home/pi/screenshot.sh


Register
========
$ python ./register.py Screeny web._tcp 80

Browse
======
$ python browse.py _test._tcp

