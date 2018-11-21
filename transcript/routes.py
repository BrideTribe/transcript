from flask import render_template, url_for, request, flash, redirect
from transcript import app
from transcript.forms import GraduateApplicantForm, GraduateRecipientForm 
from transcript.models import GraduateApplicant, GraduateRecipient

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/graduate", methods=['POST', 'GET'])
def graduate():
    form = GraduateApplicantForm()
    
    if form.validate_on_submit():
        flash(f'Account created for {form.surname.data}', 'success')
       
    return render_template('graduate.html', title='Graduate Application', form=form)


@app.route("/grad_recipient", methods=['POST', 'GET'])
def grad_recipient():
    form = GraduateRecipientForm()

    return render_template('grad_recipient.html', title='Recipient Information', form=form)

@app.route("/alumni")
def alumni():
    return render_template('alumni.html')