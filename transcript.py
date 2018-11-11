from flask import Flask, render_template, url_for

app = Flask(__name__)

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