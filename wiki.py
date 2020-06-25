#! /home/pat/anaconda3/bin/python3.7

import requests
import json
import wikipedia

KEY = 19780537
S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "cmprop": "title|ids",
    "cmtitle": "Category:2010 films",
    "cmlimit": 2,
    "list": "categorymembers"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(json.dumps(DATA, indent=4))

continueStr = DATA["continue"]["cmcontinue"]

PARAMS["cmcontinue"] = continueStr

R = S.get(url=URL, params=PARAMS)
DATA = R.json()


# print(json.dumps(DATA, indent=4))
# print(wikipedia.page(pageid=29952113).content)


def findOmdbPlot(title, year, key):
    PARAMS = {
        "apikey": key,
        "t": title,
        "y": year,
        "plot": "full"
    }
    URL = "http://www.omdbapi.com"
    R = S.get(url=URL, params=PARAMS)
    DATA = R.json()
    if DATA["Response"] == "True":
        return DATA["Plot"], DATA["Actors"].split(", ")
    else:
        return None, None


plot, actors = findOmdbPlot("3 backyards", 2010, KEY)
if plot:
    print("houraa")
else:
    print("daccord")
