import json
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string


def artist_used_most(search_word: str, clean_artist_lyric_list: list):

    """
    Get top 5 artists who used word most.

    :param search_word: From input box on homepage of Flask app.
    :param clean_artist_lyric_list: List of dictionaries of artists and all their lyrics.
    :return: List of artists and word count.
    """

    # get the word counts of all artists
    word_count_list = []
    for index in range(len(clean_artist_lyric_list)):
        try:
            word_counts = {'Artist': clean_artist_lyric_list[index]['Artist'],
                           'Lyrics count': clean_artist_lyric_list[index]['Lyrics'].lower().count(search_word)}
            word_count_list.append(word_counts)
        except KeyError:
            continue
    word_count_list = sorted(word_count_list, key=lambda item: item['Lyrics count'], reverse=True)

    return word_count_list[0:5]


def clean_data():
    """"
    Takes the original json and cleans it using NLTK. Take out punctuation and most stop words.

    Currently not working 100% correctly.
    """

    file = 'artist_lyrics.json'
    with open(file) as file_object:
        json_object = json.load(file_object)

    stop_words = set(stopwords.words('english'))
    more_to_remove = ['', '`', 'nt', 'gon', '’']
    stop_words.update(more_to_remove)
    punctuation_table = str.maketrans('', '', string.punctuation)

    for artist in json_object:
        if len(artist) > 1:
            split_lyrics = word_tokenize(artist['Lyrics'].lower().strip())
            no_punctuation = [words.translate(punctuation_table) for words in split_lyrics]
            cleaned = [word for word in no_punctuation if word not in stop_words]
            artist['Lyrics'] = " ".join(cleaned)

        else:
            continue

    with open(file, 'w+') as file_object:
        json.dump(json_object, file_object)


def open_file():
    filename = 'artist_lyrics.json'
    with open(filename) as file_object:
        json_obj = json.load(file_object)
    return json_obj


def main():
    search_word = "Home".lower()
    artist_lyric_dict = open_file()
    artist_used_most(search_word, artist_lyric_dict)
    clean_data()


if __name__ == '__main__':
    main()
