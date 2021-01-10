import requests


def get_song_names():
    url = f'https://itunes.apple.com/search?term=guns+and+roses&limit=5'
    data = requests.get(url)
    response = data.json()
    thing = response["results"][0]["trackName"]
    return thing


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


def get_artist_songs():
    url = 'https://itunes.apple.com/search?term=guns+and+roses&entity=musicTrack&limit=200'
    data = requests.get(url)
    response = data.json()
    songs = response["results"]
    filename = "artist_songs.json"
    with open(filename, "w+") as file_object:
        json.dump(songs, file_object)
