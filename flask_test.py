# Flask hello-world app that is avaliable on local network
from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello, world'


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
