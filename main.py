from flask import Flask, render_template, redirect, url_for, request, flash
from flask_bootstrap import Bootstrap5
from datetime import datetime
from forms import GuestForm, GuestForm_de, GuestForm_tw
import requests
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_KEY')
Bootstrap5(app)

BEARER_TOKEN = os.environ.get('SHEETY_BEARER_TOKEN')

sheety_endpoint = os.environ.get('SHEETY_ENDPOINT')

#Bearer Token Authentication
bearer_headers = {
    "Authorization": f'Bearer {BEARER_TOKEN}'
}

@app.route("/")
@app.route("/<lang>")
def home(lang=None):
    return render_template("index.html", lang=lang)

@app.route("/accommodations")
@app.route("/<lang>/accommodations")
def accommodations(lang=None):
    return render_template("accommodations.html", lang=lang)

@app.route("/directions")
@app.route("/<lang>/directions")
def directions(lang=None):
    return render_template("directions.html", lang=lang)

@app.route("/rsvp", methods=["GET", "POST"])
@app.route("/<lang>/rsvp", methods=["GET", "POST"])
def rsvp(lang=None):

    if lang==None or lang=='en':
        form = GuestForm()
    elif lang == 'de':
        form = GuestForm_de()
    elif lang == 'tw':
        form = GuestForm_tw()

    if form.validate_on_submit():
        response = requests.get(url=sheety_endpoint, headers=bearer_headers).json()['guests']
        data = [guest for guest in response if form.first_name.data.lower().strip() in guest['firstName'].lower().strip() and form.last_name.data.lower().strip() in guest['lastName'].lower().strip()]
        if len(data) > 0:
            return render_template("rsvp.html", form=form, data=data, double_entry=True, lang=lang)
        else:
            sheety_parameters = {
                "guest": {
                    "firstName": form.first_name.data,
                    "lastName": form.last_name.data,
                    "email": form.email.data,
                    "willYouBeAttending?": form.attendance.data,
                    "willYouBeBringingAGuest?": form.plus_one.data,
                    "guestFirstName": form.guest_first_name.data,
                    "guestLastName": form.guest_last_name.data,
                    "anyDietaryRestrictions?": form.dietary_restriction.data,
                    "questionsOrComments?": form.comment.data,
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
            }
            requests.post(url=sheety_endpoint, json=sheety_parameters, headers=bearer_headers)
            return render_template("rsvp.html", form=form, submission_successful=True, lang=lang)
    return render_template("rsvp.html", form=form, lang=lang)

@app.route("/the-wedding-day")
@app.route("/<lang>/the-wedding-day")
def the_wedding_day(lang=None):
    return render_template("the-wedding-day.html", lang=lang)

@app.route("/photos")
@app.route("/<lang>/photos")
def photos(lang=None):
    return render_template("photos.html", lang=lang)


if __name__ == '__main__':
    app.run(debug=True)