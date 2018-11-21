from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email

class GraduateApplicantForm(FlaskForm):
    surname = StringField('Surname', validators=[DataRequired(), Length(min=2, max=100)])
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=100)])
    marital_status = SelectField(u'Marital Status', choices=[('default', '-- Select --'), ('div', 'DIVORCED'), ('mar', 'MARRIED'), 
                                                            ('sin', 'SINGLE'), ('w', 'WIDOW'),
                                                            ('wid', 'WIDOWER')
                                                            ])
    matric_no = StringField('Matriculation Number', validators=[DataRequired(), Length(min=4, max=50)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone Number', validators=[DataRequired(), Length(min=8, max=20)])
    transcript_type = SelectField(u'Transcript Type', choices=[('default', '-- Select --'), ('grad', 'Graduate'), ('post', 'Post-Graduate')])
    degree_awarded = StringField('Degree Awarded *(Use abbreviation)*', validators=[DataRequired(), Length(min=2, max=20)])
    faculty = StringField('Faculty', validators=[DataRequired(), Length(min=1, max=250)])
    department = StringField('Department', validators=[DataRequired(), Length(min=1, max=500)])
    year_of_grad = StringField('Year of Graduation', validators=[DataRequired(), Length(min=2, max=20)])
    permanent_addr = TextAreaField('Present Permanent Address')
    submit = SubmitField('Save & Continue')

class GraduateRecipientForm(FlaskForm):
    recipient_name = StringField('Institution/Organization Name', 
                                    validators=[DataRequired(), Length(min=3, max=200)])
    country = StringField('Country', validators=[DataRequired(), Length(min=2, max=200)])
    address_line = StringField('Address Line', validators=[DataRequired(), Length(min=10, max=500)])
    shipping_continent = StringField('Shipping Continent', validators=[DataRequired(), Length(min=10, max=100)])
    city = StringField('City/State/Province', validators=[DataRequired(), Length(min=10, max=500)])
    courier = StringField('Preferred Courier', validators=[DataRequired(), Length(min=10, max=500)])
    zip_code = StringField('Zip Code/Post Code', validators=[DataRequired(), Length(min=10, max=500)])
    agree = BooleanField('I agree to the privacy policy & terms of engagement of this transcript')
    submit = SubmitField('Apply')

