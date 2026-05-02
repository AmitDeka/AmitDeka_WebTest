from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, IntegerField, SelectField, RadioField, DateField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import DataRequired, NumberRange, ValidationError
from datetime import date

class TestForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    
    email = EmailField('Email', validators=[DataRequired()])
    def validate_email(self, field):
        email_val = field.data.lower()
        if '@' not in email_val or not email_val.endswith('@gauhati.ac.in'):
            raise ValidationError("Only valid @gauhati.ac.in addresses are allowed.")

    age = IntegerField('Age', validators=[DataRequired(), NumberRange(min=1)])
    
    gender = SelectField('Gender', choices=[
        ('M', 'Male'), ('F', 'Female'), ('O', 'Other')
    ])
    
    modeTravel = RadioField('Mode of Travel', choices=[
        ('bike','Bike'), ('car','Car')
    ], validators=[DataRequired()])
    
    date = DateField('Date of Birth', validators=[DataRequired()])
    def validate_date(self, field):
        if field.data and field.data >= date.today():
            raise ValidationError("Date must be in the past.")

    file = FileField('Upload Document', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'jpeg', 'png', 'gif', 'pdf'], 'Images and PDFs only!')
    ])
