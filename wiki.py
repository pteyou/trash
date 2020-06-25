#! /home/pat/anaconda3/bin/python3.7

import requests
import json
import wikipedia

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"


PARAMS = {
    "action": "query",
    "format": "json",
    "cmprop": "title|ids",
    "cmtitle" : "Category:2010 films",
    "cmlimit" : 2,
    "list" : "categorymembers"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

#print(json.dumps(DATA, indent=4))

id = 39353874
PARAMS = {
    "action": "query",
    "format": "json",
    "pageids" : id,
    "prop" : "revisions",
    "rvprop" : "content"

}
film = S.get(url=URL, params=PARAMS)
DATA = film.json()

#print(json.dumps(DATA, indent=4))
print(wikipedia.page(pageid=id).content)