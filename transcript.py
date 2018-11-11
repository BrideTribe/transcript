from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return 'Welcome to Unical'

@app.route("/graduate")
def graduate():
    return 'Graduate Application'

@app.route("/postgraduate")
def postgraduate():
    return 'Postgraduate Application'


if __name__ == '__main__':
    app.run(debug=True)