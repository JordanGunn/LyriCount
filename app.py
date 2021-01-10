from flask import Flask, render_template
import requests
import json

app = Flask(__name__)


def get_artist_songs():
    url = 'https://itunes.apple.com/search?term=guns+and+roses&entity=musicTrack&limit=200'
    data = requests.get(url)
    response = data.json()
    songs = response["results"]
    filename = "artist_songs.json"
    with open(filename, "w+") as file_object:
        json.dump(songs, file_object)


@app.route('/')
def home():
    return render_template("base.html", thing=thing)


if __name__ == '__main__':
    get_artist_songs()
    app.run()

