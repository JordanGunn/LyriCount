def artist_used_most(search_word: str, artist_lyric_dict: dict) -> list:

    """
    Get top 5 artists who used word most.

    :param search_word: From input box on homepage of Flask app.
    :param artist_lyric_dict: Dictionary of artists and all their lyrics.
    :return: List of artists and word count.
    """

    # get the word counts of all artists
    word_counts = {
        artist: lyrics.count(search_word) for lyrics, artist in artist_lyric_dict.items()
    }

    # sort the dictionary for word counts
    sorted_counts = {
        k: v for k, v in sorted(word_counts.items(), key=lambda item: item[1])
    }

    # reverse and return top 5
    return list(reversed(list(sorted_counts))[0:5])

