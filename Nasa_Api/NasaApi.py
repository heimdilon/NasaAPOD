# Created by kor_a at 15 Ekim 2020
# Date: 15.10.2020
# Time: (23:25)
from flask import Flask, render_template
import requests

app = Flask(__name__)
@app.route("/")
def get_image():
    apod = requests.get("https://api.nasa.gov/planetary/apod?api_key=Your api key")
    apod_json = apod.json()
    image = apod_json['hdurl']
    title = apod_json['title']
    explanation = apod_json['explanation']
    return render_template('index.html', url=image, title=title, explanation=explanation)
@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run()
