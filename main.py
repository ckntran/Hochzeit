from flask import Flask, render_template, redirect, url_for, request, flash
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired, optional
from datetime import datetime
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

# GuestForm
class GuestForm(FlaskForm):
    first_name = StringField('First Name (required)', validators=[DataRequired()])
    last_name = StringField('Last Name (required)', validators=[DataRequired()])
    email = StringField('Email', validators=[optional()])
    attendance = SelectField('Will you be attending? (required)', choices=['Yes', 'No'])
    plus_one = SelectField('Will you be bringing a guest? (required)', choices=['Yes', 'No'])
    guest_first_name = StringField('Guest First Name', validators=[optional()])
    guest_last_name = StringField('Guest Last Name', validators=[optional()])
    dietary_restriction = StringField('Any dietary restrictions?', validators=[optional()])
    comment = TextAreaField('Questions or comments?', validators=[optional()])
    submit = SubmitField('Submit')

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/accommodations")
def accommodations():
    return render_template("accommodations.html")

@app.route("/directions")
def directions():
    return render_template("directions.html")

@app.route("/rsvp", methods=["GET", "POST"])
def rsvp():
    form = GuestForm()
    if form.validate_on_submit():
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
        return render_template("index.html", submission_successful=True)
    return render_template("rsvp.html", form=form)

@app.route("/the-wedding-day")
def the_wedding_day():
    return render_template("the-wedding-day.html")

@app.route("/photos")
def photos():
    return render_template("photos.html")


if __name__ == '__main__':
    app.run(debug=True)