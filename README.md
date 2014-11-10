Description
==================
This is an address book project, the project is divided in back-end and front-end. 

The back-end manage and process all data and is designed to be an horizontal 
scale-out application, also only "speaks" JSON.

The fron-end will manage all interactions with user (UI) and uses the back-end to
consume/provide data, for this I use Angular (Why?, just google a little and 
you will know why I choose it)

More info about the project you can read the "REQUIREMENTS" file.


Configuration
================
Some comments about the configuration.

Generate SSL
--------------
One of the non-functional requirements is *Security* so, all services on this
project are running on SSL, to configure the certificates you have to::

1) Generate a private key::
	openssl genrsa -des3 -out server.key 1024

2) Generate a CSR::
	openssl req -new -key server.key -out server.csr

3) Remove Passphrase from Key
	cp cp server.key server.key.orig && openssl rsa -in server.key.orig -out server.key

4) Generating a Self-Signed Certificate
	openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt

You can find files inside the directory conf/ and are used in this project (Used to run
tornado over SSL).


Setup
---------
1. If you will not install de python module it is necesary configure the PYTHONPATH.

E.g
	export PYTHONPATH=$PYTHONPATH:/home/enrique/projects/addressbook/python

2. Execute the addressbook start script

E.g
	/home/enrique/projects/addressbook/python/addressbookd --port 18831

3. Got to https://localhost:18831/index

NOTE: The web also was added into the tornado server, but the idea is use nginx as front and tornado
as back (It should manage all services)

Any doubt free feel to contact me.

Notes
---------
Unittests were not added because of time; I will return to complete them (Also de smoke tests)