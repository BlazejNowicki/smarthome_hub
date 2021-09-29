from flask import Flask, render_template, redirect, request
from flask.helpers import url_for
from forms import EditFrom
from alarm_modules import Alarms

app = Flask(__name__)

app.config['SECRET_KEY'] = 'c3d17f2a195908b3fec6919d413d622a'
alarms = Alarms('db.json')

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', alarms=alarms.to_dictionary())

@app.route('/delete/<id>')
def delete(id):
    print(f"Delete alarm: {id}")
    alarms.remove(int(id))
    return redirect( url_for('home') )



# TODO Przy każdym alarmie przycisk active
# TODO Dodawanie nowych alarmów od zera
# TODO Przycisk zapisz

@app.route("/edit", methods=['GET', 'POST'])
def edit():
    form = EditFrom()
    if form.validate_on_submit():
        print(form.time.data, type(form.time.data), form.active.data)
        return redirect( url_for('home') )
    return render_template('edit.html', title='Edit', form=form)


if __name__ == "__main__":
    # app.run(debug=True)
    app.run(debug=True, host="0.0.0.0", port=5000)
