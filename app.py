
from flask import Flask, render_template, request
import requests
import json
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired, ValidationError
from get_top_artists import get_top_artists
from form import WordSearchForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'kjhsdfkgjh345toisufg980sd7g2l34khasd987asdfk'

# @app.route('/')
# def home():
#     return render_template("base.html")


@app.route("/", methods=["GET", "POST"])
def search():
    form = WordSearchForm()
    if form.validate_on_submit():
        query = request.form['word_search']
        return render_template("base.html", data=query, form=form)
    return render_template("base.html", form=form)


if __name__ == '__main__':
    app.run()