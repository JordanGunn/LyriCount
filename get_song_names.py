import requests
import json


def get_song_names():
    url = f'https://itunes.apple.com/search?term=guns+and+roses&limit=5'
    data = requests.get(url)
    response = data.json()
    thing = response["results"][0]["trackName"]
    return thing


def parse_artist_name(artist_name):
    pass


"guns+and+roses"


def get_artist_songs():
    url = 'https://itunes.apple.com/search?term=guns+and+roses&entity=musicTrack&limit=200'
    data = requests.get(url)
    response = data.json()
    artist = response["results"]
    songs = [song["trackName"] for song in artist]
    artist_songs = {"artistName": songs}
    filename = "artist_songs.json"
    with open(filename, "w+") as file_object:
        json.dump(artist_songs, file_object)


def main():
    get_artist_songs()


if __name__ == '__main__':
    main()
