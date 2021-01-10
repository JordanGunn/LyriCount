import requests
import json
from get_top_artists import TOP_URL, get_top_artists


def get_song_names():
    url = f'https://itunes.apple.com/search?term=guns+and+roses&limit=5'
    data = requests.get(url)
    response = data.json()
    thing = response["results"][0]["trackName"]
    return thing


def parse_artist_name(artist_name):
    pass


"guns+and+roses"


if __name__ == '__main__':
    main()
