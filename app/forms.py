from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Email

class ContactForm(FlaskForm):
    name  = TextField("Name", validators=[DataRequired()])
    email = TextField("Email", validators=[DataRequired()])
    subject = TextField("Subject", validators=[DataRequired()])
    message = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("Send")

class RequestResumeForm(FlaskForm):
    email = TextField("Email", validators=[DataRequired(), Email()])
    email_confirmation = TextField("Confirm Email", validators=[DataRequired(), EqualTo('email')])
    submit = SubmitField("Submit Resume Request")
