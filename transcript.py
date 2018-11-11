from flask import Flask, render_template, url_for 
from forms import ApplicationForm, RecipientForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '8b245eb98f56f7c909adbe0fada726b32e29a28f'
app.config['']

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/graduate")
def graduate():
    return render_template('graduate.html', title='Graduate')

@app.route("/postgraduate")
def postgraduate():
    return render_template('postgraduate.html', title='PostGraduate')


if __name__ == '__main__':
    app.run(debug=True)