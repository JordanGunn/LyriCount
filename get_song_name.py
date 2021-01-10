from get_top_artists import get_top_artists
import requests
import json


def get_song_name() -> None:
    """
    Get the name of songs by artist's name from the Itunes API.

    :return: None
    """
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

    write_json_file(song_dict)


def write_json_file(song_dict: dict) -> None:
    """
    Write a new JSON file that includes the information of artists and the title of songs

    :return: None
    """
    filename = "artist_songs_dict_test.json"
    with open(filename, "w+") as file_object:
        json.dump(song_dict, file_object)


def main():
    get_song_name()


if __name__ == '__main__':
    main()
