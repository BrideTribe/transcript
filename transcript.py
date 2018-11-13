from flask import Flask, render_template, url_for, request, flash, redirect
from forms import (GraduateApplicationForm, PostGraduateApplicationForm, 
                    GraduateRecipientForm, PostGraduateRecipientForm, 
                    ReturningGraduateUserForm)

app = Flask(__name__)

app.config['SECRET_KEY'] = '8b245eb98f56f7c909adbe0fada726b32e29a28f'
#app.config['']

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/graduate", methods=['POST', 'GET'])
def graduate():
    form = GraduateApplicationForm()
    
    if form.validate_on_submit():
        flash(f'Account created for {form.surname.data}', 'success')
        return redirect(url_for('grad_recipient'))
    return render_template('graduate.html', title='Graduate Application', form=form)

@app.route("/postgraduate", methods=['POST', 'GET'])
def postgraduate():
    form = PostGraduateApplicationForm()

    return render_template('postgraduate.html', title='Post Graduate Application', form=form)

@app.route("/grad_recipient", methods=['POST', 'GET'])
def grad_recipient():
    form = GraduateRecipientForm()

    return render_template('grad_recipient.html', title='Recipient Information', form=form)

@app.route("/postgrad_recipient", methods=['POST', 'GET'])
def postgrad_recipient():
    form = PostGraduateRecipientForm()

    return render_template('recipient.html', title='Recipient Information', form=form)

if __name__ == '__main__':
    app.run(debug=True)