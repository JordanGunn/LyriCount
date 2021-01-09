from bs4 import BeautifulSoup
import requests


def TOP_URL():

    """
    Return the constant TOP_URL

    Location of top 200 artists from rolling stone.
    """

    return r"https://www.rollingstone.com/charts/artists/"


def get_top_artists(url):

    """
    Submit get request to server and get top 200 artists.

    :param url:     Url location of top artists.
    :return:        List of artists.
    """

    with requests.get(url) as top200:
        # Create BeautifulSoup object from
        data = BeautifulSoup(top200.text, "html.parser")
        # get divs by class
        divs = data.findAll("div", {"class": "c-chart__table--title"})
        # get the artist tags in the div
        artists = [div.findAll("p")[0].text for div in divs]

    return artists
