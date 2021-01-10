from bs4 import BeautifulSoup
import requests


def TOP_URL():

    """
    Return the constant TOP_URL

    Location of top 200 artists from rolling stone.
    """

    return r"https://www.billboard.com/charts/artist-100"


def get_top_artists():

    """
    Submit get request to server and get top 200 artists.

    :return:        List of artists.
    """

    with requests.get(TOP_URL()) as top200:
        # Create BeautifulSoup object from
        data = BeautifulSoup(top200.text, "html.parser")
        # get divs by class
        divs = data.findAll("div", {"class": "item-details__title"})
        # get the artist tags in the div
        artists = [div.text for div in divs]

    return artists


if __name__ == "__main__":

    print(get_top_artists())
