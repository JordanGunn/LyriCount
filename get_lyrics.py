import json
import requests
import re
from bs4 import BeautifulSoup


def open_json_file() -> dict:
    """
    Open the JSON file that includes the information of artists and the title of songs.

    :return: a JSON object
    """
    filename = 'artist_songs_dict.json'
    with open(filename) as file_object:
        json_obj = json.load(file_object)
    return json_obj


def get_lyrics() -> None:
    """
    Get the whole lyrics from the API

    :return: None
    """
    json_obj = open_json_file()
    artist_lyrics_list = []
    for key, value in json_obj.items():
        artist_lyrics_dict = {'Artist': key}
        key = key.replace(' ', '%20')
        whole_lyrics = ''
        for index in range(len(value)):
            value[index] = value[index].replace(' ', '%20')
            value[index] = re.sub(r'\(.*?\)', '', value[index])
            url = f'http://api.chartlyrics.com/apiv1.asmx/SearchLyricDirect?artist={key}&song={value[index]}'
            response = requests.get(url).text.encode('utf-8')
            xml_obj = BeautifulSoup(response, 'lxml-xml')
            lyrics = str(xml_obj.findAll('Lyric'))
            lyrics = re.sub(r'<.*?>|\[|]', '', lyrics)
            if len(lyrics) > 0:
                whole_lyrics += lyrics.replace('\n', ' ')
                artist_lyrics_dict['Lyrics'] = whole_lyrics
        artist_lyrics_list.append(artist_lyrics_dict)

    write_json_file(artist_lyrics_list)


def write_json_file(artist_lyrics_list: list) -> None:
    """
    Write a new JSON file that includes the information of artists and lyrics.

    :param artist_lyrics_list: a list of dictionaries that includes the information of artists and lyrics
    :return: None
    """
    filename = "artist_lyrics.json"
    with open(filename, "w+") as file_object:
        for length in range(len(artist_lyrics_list)):
            json.dump(artist_lyrics_list[length], file_object)


def main():
    get_lyrics()


if __name__ == '__main__':
    main()
