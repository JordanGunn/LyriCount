import json


def get_lyrics():
    filename = 'artist_songs_dict.json'
    with open(filename) as file_object:
        json_obj = json.load(file_object)
    print(len(json_obj))

get_lyrics()