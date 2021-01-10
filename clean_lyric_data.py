from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import json


def GENDER_WORDS():

    gender_words = (
        "her",  "him", "his", "he", "she", "himself", "herself"
    )

    return " ".join(gender_words)


def filter_lyrics(lyrics):

    stop_words = set(stopwords.words("english"))
    special_chars = {"'", ",", "-", "!", "/", "\\", "?", ":", ";"}
    stopwords.update(special_chars)
    word_tokens = word_tokenize(lyrics)
    filtered_lyrics = [lyric for lyric in word_tokens if lyric not in stop_words]

    return " ".join(filtered_lyrics)


def dump_filtered_lyrics(filtered_lyrics):

    file = "artist_lyrics_filtered.json"
    with open(file, "w+") as fp:
        json.dump(filtered_lyrics, fp)


# lyrics = []

with open("artist_lyrics.json", "r", errors="ignore") as fp:
    lyrics = json.load(fp)
    filtered = {
        artist: filter_lyrics(words) for words, artist in lyrics.items()
    }

# dump_filtered_lyrics(filtered)

