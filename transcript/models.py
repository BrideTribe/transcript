from transcript import db

class GraduateApplicant(db.Model):
    #__tablename__ = 'graduate_applicant'

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
    grad_recipient = db.relationship('GraduateRecipient', backref='graduate_applicant', lazy=True)

    def __repr__(self):
        return f"GraduateApplicant('{self.surname}', '{self.first_name}', '{self.marital_status}', '{self.matric_no}', '{self.email}', '{self.phone}', '{self.faculty}', '{self.department}', '{self.year_of_grad}', '{self.permanent_addr}')"

class GraduateRecipient(db.Model):
    #__table__ = 'gruaduate_recipient'

    id = db.Column(db.Integer, primary_key=True)
    recipient_name = db.Column(db.String(200), nullable=False)
    country = db.Column(db.String(200), nullable=False)
    address_line = db.Column(db.Text, nullable=False)
    shipping_continent = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(200), nullable=False)
    courier = db.Column(db.String(200), nullable=False)
    zip_code = db.Column(db.String(100), nullable=False)
    agree = db.Column(db.Boolean, nullable=False)
    graduate_applicant_id = db.Column(db.Integer, db.ForeignKey('graduate_applicant.id'), nullable=False)

    def __repr__(self):
        return f"GraduateRecipient('{self.recipient_name}', '{self.country}', '{self.address_line}', '{self.shipping_continent}', '{self.city}', '{self.courier}', '{self.zip_code}')"
