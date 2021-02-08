from flask import Flask
import requests

app = Flask(__name__)


@app.route('/', methods=['GET'])
def chuck_norris():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url).json()
    img_url = "<img src=" + response["icon_url"] + " alt='Chuck Norris'>"

    return "<strong>Random joke from chuck norris:</strong>" + response["value"] + img_url


if __name__ == "__main__":
    app.run()





