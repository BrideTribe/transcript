from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email

class ApplicationForm(FlaskForm):
    surname = StringField('Surname', validators=[DataRequired(), Length(min=2, max=100)])
    firstname = StringField('First Name', validators=[DataRequired(), Length(min=2, max=100)])
    marital_status = SelectField(u'-- Select --', choices=[('div', 'DIVORCED'), ('mar', 'MARRIED'), 
                                                            ('sin', 'SINGLE'), ('w', 'WIDOW'),
                                                            ('wid', 'WIDOWER')
                                                            ])
    matric_no = StringField('Matriculation Number', validators=[DataRequired(), Length(min=4, max=50)])
    email = StringField('Matriculation Number', validators=[DataRequired(), Email()])
    phone = StringField('Phone Number', validators=[DataRequired(), Length(min=8, max=20)])
    department = StringField('Department', validators=[DataRequired(), Length(min=1, max=250)])
    course = StringField('Course', validators=[DataRequired(), Length(min=1, max=500)])
    year_of_grad = StringField('Year of Graduation', validators=[DataRequired(), Length(min=2, max=20)])
    permanent_addr = TextAreaField('Present Permanent Address')
    submit = SubmitField('Save & Continue')

class RecipientForm(FlaskForm):
    institution_name = StringField('Institution/Organization Name', 
                                    validators=[DataRequired(), Length(min=3, max=200)])
    country = StringField('Country', validators=[DataRequired(), Length(min=2, max=200)])
    address_line = StringField('Address Line', validators=[DataRequired(), Length(min=10, max=500)])
    shipping_continent = StringField('Shipping Continent', validators=[DataRequired(), Length(min=10, max=100)])
    city = StringField('City/State/Province', validators=[DataRequired(), Length(min=10, max=500)])
    courier = StringField('Preferred Courier', validators=[DataRequired(), Length(min=10, max=500)])
    zip_code = StringField('Zip Code/Post Code', validators=[DataRequired(), Length(min=10, max=500)])
    agree = BooleanField('I agree to the privacy policy & terms of engagement of this transcript')
    submit = SubmitField('Apply')