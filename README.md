# About PlextoTMDB
Script used to migrate plex watchlist to TMDB

---

# Requirements
- Python version 3.10+
- make (for linux users)
- Python3-venv
---

# Installation for Linux
Download or clone the repository, then inside the `constants.py` file put your plex `client id` and `token` that you need to [extract with a browser](https://www.plexopedia.com/plex-media-server/general/plex-token/#getcurrentusertoken)
For the `client id` you need the `X-Plex-Client-Identifier` value.
For your TMDB API Read Access Token, API KEY you can find them in the [API Subscription tab](https://www.themoviedb.org/settings/api) and your designed list id.
The `list id` is the id used in the URL of a list inside the `Lists`, section of your account.
For example `https://www.themoviedb.org/list/1234567` the list id is 1234567
Then just run `make install` and a ptmdb folder will be created on your Desktop with everything set to run the script
Simple run the script with `python script.py`

---

# Installation for Windows
Download or clone the repository, then inside the `constants.py` file put your plex `client id` and `token` that you need to [extract with a browser](https://www.plexopedia.com/plex-media-server/general/plex-token/#getcurrentusertoken)
For the `client id` you need the `X-Plex-Client-Identifier` value.
For your TMDB API Read Access Token, API KEY you can find them in the [API Subscription tab](https://www.themoviedb.org/settings/api) and your designed list id.
The `list id` is the id used in the URL of a list inside the `Lists`, section of your account.
For example `https://www.themoviedb.org/list/1234567` in this case the list id is 1234567
Then create a python virtual environment where you want, activate it and run `pip install -r requirements.txt` to install the required packages.
Simply run the script with `python script.py`

---
