from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    url = 'https://itunes.apple.com/search?term=guns+and+roses&limit=5'
    data = requests.get(url)
    response = data.json()
    thing = response["results"][0]["trackName"]
    return render_template("base.html", thing=thing)


if __name__ == '__main__':
    app.run(host="0.0.0.0")
