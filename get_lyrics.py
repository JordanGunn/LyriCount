import json


def get_lyrics():
    filename = 'artist_songs_dict.json'
    with open(filename) as file_object:
        json_obj = json.load(file_object)
    print(len(json_obj))


def main():
    get_lyrics()


if __name__ == '__main__':
    main()
