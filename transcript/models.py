from transcript import db, login_manager



class Applicant(db.Model):
    __tablename__ = 'applicant'

    id = db.Column(db.Integer, primary_key=True)
    surname = db.Column(db.String(100), nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    marital_status = db.Column(db.String(100), nullable=False)
    matric_no = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    phone = db.Column(db.String(20), unique=True, nullable=False)
    transcript_type = db.Column(db.String(100), nullable=False)
    degree_awarded = db.Column(db.String(50), nullable=False)
    faculty = db.Column(db.String(250), nullable=False)
    department = db.Column(db.String(250), nullable=False)
    year_of_grad = db.Column(db.String(50), nullable=False)
    permanent_addr = db.Column(db.Text, nullable=False)
    recipient = db.relationship('Recipient', backref='applicant', lazy=True)

    def __repr__(self):
        return f"Applicant('{self.surname}', '{self.first_name}', '{self.marital_status}', '{self.matric_no}', '{self.email}', '{self.phone}', '{self.faculty}', '{self.department}', '{self.year_of_grad}', '{self.permanent_addr}')"

class Recipient(db.Model):
    __tablename__ = 'recipient'

    id = db.Column(db.Integer, primary_key=True)
    recipient_name = db.Column(db.String(200), nullable=False)
    country = db.Column(db.String(200), nullable=False)
    address_line = db.Column(db.Text, nullable=False)
    shipping_continent = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(200), nullable=False)
    courier = db.Column(db.String(200), nullable=False)
    zip_code = db.Column(db.String(100), nullable=False)
    agree = db.Column(db.Boolean, nullable=False)
    applicant_id = db.Column(db.Integer, db.ForeignKey('applicant.id'), nullable=False)

    def __repr__(self):
        return f"Recipient('{self.recipient_name}', '{self.country}', '{self.address_line}', '{self.shipping_continent}', '{self.city}', '{self.courier}', '{self.zip_code}')"

class Alumni(db.Model):
    __tablename__ = 'alumni'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    marital_status = db.Column(db.String(100), nullable=False)
    dob = db.Column(db.String(50), nullable=False)
    year_of_grad = db.Column(db.String(50), nullable=False)
    faculty = db.Column(db.String(250), nullable=False)
    department = db.Column(db.String(250), nullable=False)
    degree_awarded = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    phone = db.Column(db.String(20), unique=True, nullable=False)
    home_address = db.Column(db.String(1000), nullable=False)
    employment = db.Column(db.String(200), nullable=False)
    employment_address = db.Column(db.String(1000), nullable=False)

    def __repr__(self):
        return f"Alumni('{self.full_name}', '{self.marital_status}', '{self.dob}', '{self.year_of_grad}', '{self.faculty}', '{self.department}', '{self.degree_awarded}', '{self.email}', '{self.phone}', '{self.home_address}', '{self.employment}', '{self.employer_address}')"
    