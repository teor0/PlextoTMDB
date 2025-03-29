import requests
import json
import math
import sys
from enum import Enum
import constants

class category(Enum):
    FILM: int = 1
    TV: int  = 2
    TV_FILM: int = 99

headers = {
    'accept': 'application/json, text/plain, */*'
}

def get_totalSize(type):
    sizeParams= {
        'type': str(type),
        'sort': '1',
        'X-Plex-Client-Identifier': constants.PLEX_CLIENT_ID,
        'X-Plex-Token': constants.PLEX_API_KEY,
        'X-Plex-Text-Format': 'plain',
        'X-Plex-Language': 'en',
    }
    sizeResponse= requests.get(constants.PLEX_WATCHLIST_URL, headers=headers, params=sizeParams)
    dataSize=sizeResponse.json()
    return(dataSize['MediaContainer']['totalSize'])


def watchlistBy(type):
    totalSize=get_totalSize(type)
    start=0
    slice=100
    iteration=math.floor(totalSize/slice)
    i=0
    mediaList = {"items": []}
    print("Starting to migrate from Plex")
    while i<=iteration:
        params = {
            'type': str(type),
            'sort': '1',
            'X-Plex-Client-Identifier': constants.PLEX_CLIENT_ID,
            'X-Plex-Container-Start': str(start),
            'X-Plex-Container-Size': str(slice),
            'X-Plex-Token': constants.PLEX_API_KEY,
            'X-Plex-Text-Format': 'plain',
            'X-Plex-Language': 'en',
        }
        response = requests.get(constants.PLEX_WATCHLIST_URL, headers=headers, params=params)
        data=response.json()
        for media in data['MediaContainer']['Metadata']:
            item={
                "title": (f"{media['title']}"),
                "year": (f"{media['year']}")
            }
            mediaList["items"].append(item)
        start+=100
        i+=1
    if(type==1):
        print("Found: "+ str(len(mediaList["items"])) +" films on Plex watchlist")
    else:
        print("Found: "+ str(len(mediaList["items"]))+ " tv shows on Plex watchlist")
    return mediaList
