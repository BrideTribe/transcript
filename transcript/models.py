from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from transcript import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    surname = db.Column(db.String(100), nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    middle_name = db.Column(db.String(100), nullable=False)
    maiden = db.Column(db.String(100), nullable=False)
    dob = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(20), nullable=False)
    #nationality = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(100), nullable=False)    
    state_of_origin = db.Column(db.String(100), nullable=False)
    lga = db.Column(db.String(100), nullable=False)
    marital_status = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    phone = db.Column(db.String(20), unique=True, nullable=False)
    telephone = db.Column(db.String(20), unique=True, nullable=True)
    degree_awarded = db.Column(db.String(50), nullable=False)
    faculty = db.Column(db.String(250), nullable=False)
    department = db.Column(db.String(250), nullable=False)
    year_of_grad = db.Column(db.String(50), nullable=False)
    permanent_addr = db.Column(db.Text, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    recipient = db.relationship('Recipient', backref='user', lazy=True)
    post = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.surname}', '{self.first_name}', '{self.middle_name}', '{self.maiden}' , '{self.dob}', '{self.gender}', '{self.country}', {self.state_of_origin}', '{self.lga}' , '{self.marital_status}','{self.email}', '{self.phone}', '{self.telephone}', '{self.faculty}', '{self.department}', '{self.year_of_grad}', '{self.permanent_addr}', '{self.password}', '{self.image_file}')"

    #create email and password reset method
    def get_reset_token(self, expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')
    
    #token verification method
    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

class Post(db.Model):
    
    __tablename__ = 'posts'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}', '{self.content}')"

class Recipient(db.Model):
    __tablename__ = 'recipient'

    id = db.Column(db.Integer, primary_key=True)
    transcript_type = db.Column(db.String(100), nullable=False)
    matric_no = db.Column(db.String(50), unique=True, nullable=False)
    recipient_name = db.Column(db.String(200), nullable=False)
    country = db.Column(db.String(200), nullable=False)
    address_line = db.Column(db.Text, nullable=False)
    shipping_continent = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(200), nullable=False)
    courier = db.Column(db.String(200), nullable=False)
    zip_code = db.Column(db.String(100), nullable=False)
    agree = db.Column(db.Boolean, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Recipient('{self.transcript_type}','{self.matric_no}','{self.recipient_name}', '{self.country}', '{self.address_line}', '{self.shipping_continent}', '{self.city}', '{self.courier}', '{self.zip_code}')"
