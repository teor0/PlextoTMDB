import tmdbsimple as tmdbs
import constants
import json
import requests
import plex
from tmdbapis import TMDbAPIs

tmdbs.API_KEY=constants.TMDB_API_KEY

def getToken():
    tmdb = TMDbAPIs(constants.TMDB_API_KEY,v4_access_token=constants.TMDB_TOKEN)
    print(tmdb.v4_authenticate())
    input("Navigate to the URL and then hit enter when Authenticated to continue")
    tmdb.v4_approved()
    return tmdb.v4_access_token

def searchFilm(filmName, year):
    search = tmdbs.Search()
    try:
        response = search.movie(query=filmName, year=year)
        if(len(search.results)==0):
            return -1
        return search.results[0]['id']
    except request.exceptions.RequestException as e:
        print("Can't find the film: " + filmName)
        return -1

def searchTV(tvName, year):
    search = tmdbs.Search()
    try:
        response = search.tv(query=tvName, year=year)
        if(len(search.results)==0):
            return -1
        return search.results[0]['id']
    except request.exceptions.RequestException as e:
        print("Can't find the TV show: " + tvName)
        return -1

def createIdList(category):
    watchlist=plex.watchlistBy(plex.category(int(category)).value)
    mediaList={"items":[]}
    print("starting to migrate the list")
    if(category=='1'):
        for movie in watchlist["items"]:
            id=searchFilm(movie['title'],movie['year'])
            if(id=='-1'):
                continue
            else:
                item={
                    "media_type": "movie",
                    "media_id": id
                }
                mediaList["items"].append(item)
    elif(category=='2'):
        for tv in watchlist["items"]:
            id=searchTV(tv['title'],tv['year'])
            if(id=='-1'):
                continue
            else:
                item={
                    "media_type": "tv",
                    "media_id": id
                }
                mediaList["items"].append(item)
    print("Migrated successfully: " + str(len(mediaList["items"])) +" films/TV shows")
    return mediaList


def addToList(filmList):
    write_token=getToken()
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": "Bearer "+ write_token
    }
    try:
        response = requests.post(constants.TMDB_LIST_URL, json=filmList, headers=headers)
        print('Script is done!')
    except request.exceptions.RequestException as e:
        print("Something went wrong please retry")

def migrateList(category):
    addToList(createIdList(category))
