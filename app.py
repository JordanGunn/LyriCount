from flask import Flask, render_template, request
from form import WordSearchForm
from artist_used_most import analyze

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
        return render_template("base.html", data=analyze(query), form=form)
    return render_template("base.html", form=form)


if __name__ == '__main__':
    app.run()