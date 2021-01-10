import json
# from form import WordSearchForm
# from flask import Flask, render_template, request


def artist_used_most(search_word: str, artist_lyric_list: list):

    """
    Get top 5 artists who used word most.

    :param search_word: From input box on homepage of Flask app.
    :param artist_lyric_list: List of dictionaries of artists and all their lyrics.
    :return: List of artists and word count.
    """

    # get the word counts of all artists
    word_count_list = []
    for index in range(len(artist_lyric_list)):
        try:
            word_counts = {'Artist': artist_lyric_list[index]['Artist'],
                           'Lyrics count': artist_lyric_list[index]['Lyrics'].lower().count(search_word)}
            word_count_list.append(word_counts)
        except KeyError:
            continue
    word_count_list = sorted(word_count_list, key=lambda item: item['Lyrics count'], reverse=True)

    return word_count_list[0:5]


def open_file():
    filename = 'artist_lyrics.json'
    with open(filename) as file_object:
        json_obj = json.load(file_object)
    return json_obj


def analyze(query):
    search_word = query.lower()
    artist_lyric_dict = open_file()
    artist_used_most(search_word, artist_lyric_dict)


def main():
    search_word = "Home".lower()
    artist_lyric_dict = open_file()
    artist_used_most(search_word, artist_lyric_dict)


if __name__ == '__main__':
    main()
