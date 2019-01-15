from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import (StringField, SelectField, TextAreaField, SubmitField, BooleanField, 
                    TextField, PasswordField)
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from transcript.models import User, Post

class AlumniForm(FlaskForm):
    surname = StringField('Surname', validators=[DataRequired(), Length(min=2, max=100)])
    other_names = StringField('Other Names', validators=[DataRequired(), Length(min=2, max=100)])
    dob = StringField('Date of Birth', validators=[DataRequired()])
    gender = SelectField(u'Gender', choices=[('f', 'Female'), ('m', 'Male')])
    state_of_origin = SelectField(u'State of Origin', choices=[('ls', 'List')])
    marital_status = SelectField(u'Marital Status', choices=[('mar', 'Married'), ('sin', 'Single')])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone Number', validators=[DataRequired(), Length(min=8, max=20)])
    degree_awarded = StringField('Degree Awarded *(Use abbreviation)*', validators=[DataRequired(), Length(min=2, max=20)])
    faculty = StringField('Faculty', validators=[DataRequired(), Length(min=1, max=250)])
    department = StringField('Department', validators=[DataRequired(), Length(min=1, max=500)])
    year_of_grad = StringField('Year of Graduation', validators=[DataRequired(), Length(min=2, max=20)])
    permanent_addr = TextAreaField('Present Permanent Address')
    password = PasswordField('Password', validators=[DataRequired(), Length(min=3)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), Length(min=3), EqualTo('password')])

    submit = SubmitField('Register')

    #fields input validation
    def validate_email(self, email):
        alumni = User.query.filter_by(email=email.data).first()
        if alumni:
            raise ValidationError(f'{self.email.data} already exist, try a different email address')

    def validate_phone(self, phone):
        alumni = User.query.filter_by(phone=phone.data).first()
        if alumni:
            raise ValidationError(f'{self.phone.data} already exist, try a different phone number')

class LoginForm(FlaskForm) :
    email = StringField('E-Mail', validators=[DataRequired(), Email(), Length(max=200)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=4)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login') 

class UpdateAccountForm(FlaskForm):
    surname = StringField('Surname', validators=[DataRequired(), Length(min=2, max=100)])
    other_names = StringField('Other Names', validators=[DataRequired(), Length(min=2, max=100)])
    dob = StringField('Date of Birth', validators=[DataRequired()])
    gender = SelectField(u'Gender', choices=[('f', 'Female'), ('m', 'Male')])
    state_of_origin = SelectField(u'State of Origin', choices=[('ls', 'List')])
    marital_status = SelectField(u'Marital Status', choices=[('mar', 'Married'), ('sin', 'Single')])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone Number', validators=[DataRequired(), Length(min=8, max=20)])
    degree_awarded = StringField('Degree Awarded *(Use abbreviation)*', validators=[DataRequired(), Length(min=2, max=20)])
    faculty = StringField('Faculty', validators=[DataRequired(), Length(min=1, max=250)])
    department = StringField('Department', validators=[DataRequired(), Length(min=1, max=500)])
    year_of_grad = StringField('Year of Graduation', validators=[DataRequired(), Length(min=2, max=20)])
    permanent_addr = TextAreaField('Present Permanent Address')
    
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    #Fields input validation
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError(f'{self.email.data} already exist, try a different email address')

    def validate_phone(self, phone):
        if phone.data != current_user.phone:
            user = User.query.filter_by(phone=phone.data).first()
            if user:
                raise ValidationError(f'{self.phone} already exist, try a different phone address')

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')

class RequestResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')
    
    #validates email address
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError(f'There is no account with email: {self.email}. You must register first.')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired(), Length(min=4)]) 
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), Length(min=4), EqualTo('password')])
    
    submit = SubmitField('Reset Password')

class RecipientForm(FlaskForm):
    
    matric_no = StringField('Matriculation Number', validators=[DataRequired(), Length(min=4, max=50)])
    transcript_type = SelectField(u'Transcript Type', choices=[('grad', 'Graduate'), ('post', 'Post-Graduate')])
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