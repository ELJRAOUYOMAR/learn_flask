""" flask code to render html files """

from flask import Flask, render_template


flask_render = Flask(__name__)

@flask_render.route('/')
def home():
    return render_template("home.html", pagetitle="Home Template")

@flask_render.route('/about')
def about():
    return render_template("about.html", pagetitle= "About Template")

if __name__ == "__main__":
    flask_render.run(debug= True)
