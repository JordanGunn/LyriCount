
def artist_used_most(search_word: str, artist_lyric_dict: dict):

    word_counts = {
        artist: lyrics.count(search_word) for lyrics, artist in artist_lyric_dict.items()
    }

    sorted_counts = {k: v for k, v in sorted(word_counts.items(), key=lambda item: item[1])}

    return reversed(list(sorted_counts))[0:5]

