from flask import render_template, url_for, request, flash, redirect
from transcript import app, db
from transcript.forms import ApplicantForm, RecipientForm, AlumniForm
from transcript.models import Applicant, Recipient, Alumni

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/graduate", methods=['POST', 'GET'])
def graduate():
    form = ApplicantForm()
    
    if form.validate_on_submit():
        applicant = Applicant(surname=form.surname.data, 
                                first_name=form.first_name.data,
                                marital_status=form.marital_status.data, 
                                matric_no=form.matric_no.data,
                                email=form.email.data, 
                                phone=form.phone.data, 
                                transcript_type=form.transcript_type.data,
                                degree_awarded=form.degree_awarded.data,
                                faculty=form.faculty.data,
                                department=form.department.data,
                                year_of_grad=form.year_of_grad.data,
                                permanent_addr=form.permanent_addr.data
        )
        db.session.add(applicant)
        db.session.commit()
        flash(f'Data captured successfully for {form.surname.data}, proceed to next stage', 'success')
        return redirect(url_for('grad_recipient'))       
    return render_template('graduate.html', title='Graduate Application', form=form)


@app.route("/grad_recipient", methods=['POST', 'GET'])
def grad_recipient():
    form = RecipientForm()

    if form.validate_on_submit():
        recipient = Recipient(recipient_name=form.recipient_name.data,
                                country=form.country.data,
                                address_line=form.address_line.data,
                                shipping_continent=form.shipping_continent.data,
                                city=form.city.data,
                                courier=form.courier.data,
                                zip_code=form.zip_code.data
        )
        db.session.add(recipient)
        db.session.commit()
        return redirect(url_for('payment'))
    return render_template('grad_recipient.html', title='Recipient Information', form=form)

@app.route("/payment")
def payment():
    return render_template('payment.html')


@app.route("/alumni", methods=['POST', 'GET'])
def alumni():
    form = AlumniForm()

    if form.validate_on_submit():
        alumni = Alumni(full_name=form.full_name.data,
                        marital_status=form.marital_status.data, 
                        dob=form.dob.data,
                        year_of_grad=form.year_of_grad.data,
                        faculty=form.faculty.data,
                        department=form.department.data,
                        degree_awarded=form.degree_awarded.data,
                        email=form.email.data,
                        phone=form.phone.data,
                        home_address=form.home_address.data,
                        employment=form.employment.data,
                        employment_address=form.employment_address.data
        )
        db.session.add(alumni)
        db.session.commit()
        flash(f'Alumnus, {form.full_name.data} registered successfully!', 'success')
        return redirect(url_for('home'))
    return render_template('alumni.html', title='Alumni', form=form)