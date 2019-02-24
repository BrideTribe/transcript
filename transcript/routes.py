import os #to capture picture extension
import secrets  #this is for the picture function
from PIL import Image #python image processing module
from flask import render_template, url_for, flash, redirect,request, abort
from transcript import app, db, bcrypt, mail
from transcript.forms import AlumniForm, LoginForm, UpdateAccountForm, PostForm, RequestResetForm, ResetPasswordForm, RecipientForm
from transcript.models import User, Post, Recipient
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Message

@app.route("/")
@app.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = AlumniForm()
    #field validation and hash password
    if form.validate_on_submit():
        h_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(surname=form.surname.data, 
                    first_name=form.first_name.data,
                    middle_name=form.middle_name.data,
                    maiden=form.maiden.data,
                    dob=form.dob.data,
                    gender=form.gender.data,
                    #nationality=form.nationality.data,
                    country=form.country.data,
                    state_of_origin=form.state_of_origin.data,
                    lga=form.lga.data,
                    marital_status=form.marital_status.data,
                    email=form.email.data, 
                    phone=form.phone.data,
                    telephone=form.telephone.data,
                    degree_awarded=form.degree_awarded.data,
                    faculty=form.faculty.data,
                    department=form.department.data,
                    year_of_grad=form.year_of_grad.data,
                    permanent_addr=form.permanent_addr.data,
                    password=h_password
        )
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for  Alumnus {form.surname.data} successfully!', 'success')
        return redirect(url_for('login'))       
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():

    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()
    
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Check your email or password and try again.', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/images', picture_fn)
    
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn

@app.route("/account", methods=['GET','POST'])
@login_required
def account():
    form = UpdateAccountForm()

    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.surname = form.surname.data
        current_user.first_name = form.first_name.data
        current_user.middle_name = form.middle_name.data 
        current_user.dob = form.dob.data
        current_user.gender = form.gender.data
        current_user.state_of_origin = form.state_of_origin.data
        current_user.marital_status = form.marital_status.data
        current_user.email = form.email.data
        current_user.phone = form.phone.data
        current_user.telephone = form.telephone.data
        current_user.degree_awarded = form.degree_awarded.data
        current_user.faculty = form.faculty.data
        current_user.department = form.department.data
        current_user.year_of_grad = form.year_of_grad.data
        current_user.permanent_addr = form.permanent_addr.data

        db.session.commit()
        #Process complete message.
        flash('Your account has been updated successfully!', 'success')

        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.surname.data = current_user.surname
        form.first_name.data = current_user.first_name
        form.middle_name.data = current_user.middle_name
        form.dob.data = current_user.dob
        form.gender.data = current_user.gender
        form.state_of_origin.data = current_user.state_of_origin
        form.marital_status.data = current_user.marital_status
        form.email.data = current_user.email
        form.phone.data = current_user.phone
        form.telephone.data = current_user.telephone
        form.degree_awarded.data = current_user.degree_awarded
        form.faculty.data = current_user.faculty
        form.department.data = current_user.department
        form.year_of_grad.data = current_user.year_of_grad
        form.permanent_addr.data = current_user.permanent_addr
    image_file = url_for('static', filename='images/'+ current_user.image_file)
    return render_template('account.html', title='Account', image_file=image_file, form=form)

@app.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()

    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('home'))
    return render_template('create_post.html', title='New Post', 
                            form=form, legend='New Post')

@app.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)

@app.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post', 
                            form=form, legend='Update Post')

@app.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted', 'success')
    return redirect(url_for('home'))


@app.route("/user/<string:surname>")
def user_posts(surname):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(surname=surname).first_or_404()
    posts = Post.query.filter_by(author=user).order_by(Post.date_posted.desc())\
            .paginate(page=page, per_page=5)
    return render_template('user_posts.html', posts=posts, user=user) 

def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request', sender='noreply@gmail.com', recipients=[user.email])
    msg.body = '''To reset your password, visit the following link:
    {url_for('reset_token', token=token, _external=True)}

    If you did not make this requrest then simply ignore this email and no changes will be made.
    '''
    mail.send(msg)

@app.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RequestResetForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An email has been sent with instructions to reset your password.', 'info')
        return redirect(url_for('login'))
    return render_template('reset_request.html', title='Reset Password', form=form) 

@app.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('home'))
         
    user = User.verify_reset_token(token)
    if user is None:
        flash('That is an invalid or expired token', 'warning')
        return redirect(url_for('reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        h_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = h_password
        db.session.commit()
        flash(f'Your password has been updated! You are now able to login.', 'success')
        return redirect(url_for('login'))
    return render_template('reset_token.html', title='Reset Password', form=form)
    
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

@app.route("/alumni_view")
def alumni_view():
    return render_template('alumni_view.html')

@app.route("/payment")
def payment():
    return render_template('payment.html')
