from flask import Flask, render_template

app = Flask(__name__)

alarms = [
    {
        'time': '5:50',
        'playlist': 'Linkin Park'
    },
    {
        'time': '8:00',
        'playlist': 'Random Access Memories'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', alarms=alarms)


if __name__ == "__main__":
    app.run(debug=True)
