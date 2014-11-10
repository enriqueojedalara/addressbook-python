Address book documentation
######################################

* **`Latest Update: 2014-11-10 11:15:56`

* **`Latest Version: 0.0.1`

* **`Status: Unstable`

Introduction
=============
Mini project.


API Notes
================

The protocol should be always a HTTPS interface.

"application/json" is the header sent in all web services.

For all requests **the "access token"** always have to be sent using the **"Authorization" header**.

On error, a non-2xx response code is returned and the detail in the HTTP Body.


API Reference
================

Login users
-------------------------------
Generate the access tokens to authorize the user to use all services ot addressbook


**POST /api/login**

Parameters::
        
    {
        "email": "User email",
        "passwd": "USer password"
    }

Response::

    {
        "access_token": "2YotnFZFEjr1zCsicMWpAA"
    }


Get all contacts
-------------------------------
Get all contacts for the user logged

**GET /api/contacts**

Headers::

    Authorize: access_token

Response::

    [
        {
            "cid": "Contact ID"
            "picture": "URL picture", 
            "name": "Name", , 
            "lastname": "Last name", 
            "details": {
                "phones": ["Json object"], 
                "custom": ["Json object"], 
                "emails": ["Json object"], 
                "sn": ["Json object"]
            }, 
            "address": "Address"
        }
    ]


Get tweets
-------------------------------
Get last tweets for one user 
@TODO, I think this uri should change to /api/<twitter_username_to_search>/tweets

**GET /api/tweets/<twitter_username_to_search>**

Headers::

    Authorize: access_token

Response::

    [
        "Json object"
    ]