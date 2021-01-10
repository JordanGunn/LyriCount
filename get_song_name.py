from get_top_artists import get_top_artists
import requests
import json


def get_song_name():
    artists = get_top_artists()
    SIZE = 200
    song_dict = {}
    for artist_name in artists:
        url = f'https://itunes.apple.com/search?term={artist_name}&entity=musicTrack&limit={SIZE}'
        song_list = set()
        for number in range(SIZE):
            data = requests.get(url)
            response = data.json()
            try:
                songs = response["results"][number]["trackName"]
                song_list.add(songs)
            except IndexError:
                pass
        song_dict[artist_name.title().replace('+', ' ')] = list(song_list)

    filename = "artist_songs_dict.json"
    with open(filename, "w+") as file_object:
        json.dump(song_dict, file_object)


def main():
    get_song_name()


if __name__ == '__main__':
    main()
