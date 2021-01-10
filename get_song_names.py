import requests
import json


def parse_artist_name(artist_name: str) -> str:

    """
    Parse artist name for url insertion.

    :param artist_name:
    :return:
    """

    split_artist_name = artist_name.split(" ")
    if len(split_artist_name) > 1:
        parsed_artist_name = "+".join(split_artist_name)
        return parsed_artist_name
    else:
        return artist_name


def get_artist_songs(artist_name):

    """
    Get all songs by an artist.

    :param artist_name: The artist name
    :return:
    """

    url = f'https://itunes.apple.com/search?term={artist_name}&entity=musicTrack&limit=200'
    data = requests.get(url)
    response = data.json()
    artist = response["results"]
    songs = [song["trackName"] for song in artist]
    artist_songs = {"artistName": songs}
    filename = "artist_songs.json"
    with open(filename, "w+") as file_object:
        json.dump(artist_songs, file_object)


def main():

    artist = parse_artist_name("")
    get_artist_songs(None)


if __name__ == '__main__':
    main()
