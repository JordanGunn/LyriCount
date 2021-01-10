from get_top_artists import TOP_URL, get_top_artists
import requests
import json


def get_song_name():
    artists = get_top_artists(TOP_URL())
    SIZE = 200
    song_list = []
    song_dict = {}
    for artist_name in artists:
        url = f'https://itunes.apple.com/search?term={artist_name}&entity=musicTrack&limit={SIZE}'
        for number in range(SIZE):
            data = requests.get(url)
            response = data.json()
            songs = response["results"][number]["trackName"]
            song_list.append(songs)
        song_dict[artist_name.title().replace('+', ' ')] = song_list

    filename = "artist_songs_dict.json"
    with open(filename, "w+") as file_object:
        json.dump(song_dict, file_object)


get_song_name()