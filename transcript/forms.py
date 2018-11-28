from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField, BooleanField, TextField
from wtforms.validators import DataRequired, Length, Email, ValidationError
from transcript.models import Applicant, Recipient, Alumni

class ApplicantForm(FlaskForm):
    surname = StringField('Surname', validators=[DataRequired(), Length(min=2, max=100)])
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=100)])
    marital_status = SelectField(u'Marital Status', choices=[('default', '-- Select --'), 
                                                                ('div', 'Divorced'), 
                                                                ('mar', 'Married'), 
                                                                ('sin', 'Single'), 
                                                                ('w', 'Widow'),
                                                                ('wid', 'Widower')
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

    def validate_matric_no(self, matric_no):
        applicant = Applicant.query.filter_by(matric_no=matric_no.data).first()
        if applicant:
            raise ValidationError(f'The matric number: {self.matric_no.data} already exist')
         
    def validate_email(self, email):
        applicant = Applicant.query.filter_by(email=email.data).first()
        if applicant:
            raise ValidationError(f'{self.email.data} already exist, try a different email')

    def validate_phone(self, phone):
        applicant = Applicant.query.filter_by(phone=phone.data).first()
        if applicant:
            raise ValidationError(f'{self.phone.data} already exist, try a different phone number')

class RecipientForm(FlaskForm):
    recipient_name = StringField('Institution/Organization Name', 
                                    validators=[DataRequired(), Length(min=3, max=200)])
    country = StringField('Country', validators=[DataRequired(), Length(min=2, max=200)])
    address_line = StringField('Address Line', validators=[DataRequired(), Length(min=10, max=500)])
    shipping_continent = StringField('Shipping Continent', validators=[DataRequired(), Length(min=10, max=100)])
    city = StringField('City/State/Province', validators=[DataRequired(), Length(min=10, max=500)])
    courier = StringField('Preferred Courier', validators=[DataRequired(), Length(min=10, max=500)])
    zip_code = StringField('Zip Code/Post Code', validators=[DataRequired(), Length(min=10, max=500)])
    agree = BooleanField('I agree to the terms of engagement of this transcript')

    submit = SubmitField('Make Payment')

class AlumniForm(FlaskForm):
    full_name = StringField('Full Name', validators=[DataRequired(), Length(min=2, max=200)])
    marital_status = SelectField(u'Marital Status', choices=[('default', '-- Select --'), 
                                                                ('div', 'Divorced'), 
                                                                ('mar', 'Married'), 
                                                                ('sin', 'Single'), 
                                                                ('w', 'Widow'),
                                                                ('wid', 'Widower')
    ])
    dob = StringField('Date of Birth', validators=[DataRequired(), Length(min=5, max=50)])
    year_of_grad = StringField('Year of Graduation', validators=[DataRequired(), Length(min=2, max=20)])
    faculty = StringField('Faculty', validators=[DataRequired(), Length(min=1, max=250)])
    department = StringField('Department', validators=[DataRequired(), Length(min=1, max=500)])
    degree_awarded = StringField('Degree Awarded *(Use abbreviation)*', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone Number', validators=[DataRequired(), Length(min=8, max=20)])
    home_address = StringField('Home Address', validators=[DataRequired(), Length(min=5, max=1000)])
    employment = StringField('Current Employment Status', validators=[DataRequired(), Length(min=5, max=200)])
    employment_address = StringField('Employer Address', validators=[DataRequired(), Length(min=5, max=1000)])

    submit = SubmitField('Register')

    def validate_email(self, email):
        alumni = Alumni.query.filter_by(email=email.data).first()
        if alumni:
            raise ValidationError(f'{self.email.data} already exist, try a different email')

    def validate_phone(self, phone):
        alumni = Alumni.query.filter_by(phone=phone.data).first()
        if alumni:
            raise ValidationError(f'{self.phone.data} already exist, try a different phone number')