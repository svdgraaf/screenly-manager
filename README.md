Screenly-manager
=======

A simple manager for the screenly OSE software

Installation
============
Donwload the zip file, and extract. Init the database:

	./application/manage.py syncdb
	./application/manage.py migrate

(this will initialize a database in your /tmp folder) 

From the root, start the management server with Foreman:
	
	foreman start

Or start a devserver:

	./application/manage.py runserver 0.0.0.0:8000

Screenshots Setup
=================
Install x11-apps and imagemagick on your screenly clients:

    sudo apt-get install x11-apps imagemagick -y

Download screenshot script:

    wget -O /home/pi/screenshot.sh https://github.com/svdgraaf/screenly-manager/raw/master/bin/screenshot.sh
    chmod +x /home/pi/screenshot.sh

Edit crontab (eg: ``crontab -e``) and add this line (this will take a screenshot every 5 minutes):

    */5 * * * * /home/pi/screenshot.sh


Register
========

    python ./register.py Screeny web._tcp 80

Browse
======

    python browse.py _test._tcp

(optional) Bonjour
======
You can install bonjour on your instances wich the manager will query.

    curl -sL https://raw2.github.com/svdgraaf/screenly-manager/master/install_bonjour.sh | bash