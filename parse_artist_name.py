import requests
import json
from get_top_artists import TOP_URL, get_top_artists


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
