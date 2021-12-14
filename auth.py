# ONLY FOR AUTH
from flask import Blueprint, render_template, request, flash, redirect, url_for, session, g
import dataset 
# this one to hash the password during signup and check has during login
from werkzeug.security import generate_password_hash, check_password_hash

# to work with database in this file
taskbook_db = dataset.connect('sqlite:///taskbook.db')

# this lines makes it possible to write some routes here and include in app.py
auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    # if user is already logged in and goes to /login, then send back to tasks.html
    if session.get('user_authenticated'):
        flash('Log out first to log back in.')
        return render_template('tasks.html')

    if(request.method == 'GET'):
        return render_template("login.html")
    
    if(request.method == 'POST'):
        email = request.form.get('user_email')
        password = request.form.get('user_password')
        user_table = taskbook_db.get_table('user_cred')
        # first check if there is someone who is a user already
        user = user_table.find_one(email=email)
        if(user):
            # check_password_has(a,b) will hash 'b' and check for equality with 'a', where 'a' is already hashed password
            if (check_password_hash(user['password'], password)):
                flash('Logged in successfully', category='success')
                # if password is correct, set sessions
                session['user_authenticated'] = True
                session['user_email'] = email
                to_go = user['view']
                # send the user to whatever their "view" column has
                return redirect(url_for(to_go))
            else:
                flash('Incorrect password. Try again!', category='error')
        else:
            # if user does not exist then:
            flash('Email not registered. Please sign up first.', category='error')

    return render_template("login.html")


@auth.route('/logout')
def logout():
    # when log out clicked, unset the session variables
    if session.get('user_authenticated'):
        session.pop('user_email', None)
        session.pop('user_authenticated', None)
    else:
        # if someone tries to go to /logout then alert and send back to login.html
        flash('Please login first', category='error')
    return redirect(url_for('auth.login'))
    


@auth.route('/register', methods=['GET', 'POST'])
def register():
    # if user tries to sign up while logged in:
    if session.get('user_authenticated'):
        flash('Log out first to sign up.')
        return render_template('tasks.html')

    if(request.method == 'GET'):
        return render_template("register.html")

    if(request.method == 'POST'):
        # server-side validation seemed better with flash. so used this one instead of longer JS code
        email = request.form.get('user_email')
        password1 = request.form.get('user_password')
        password2 = request.form.get('confirm_password')
        if(len(email)<1):
            flash('Email cannot be empty', category='error')
        elif(password1 != password2):
            flash('Password do not match', category='error')
        elif(len(password1)<8 or len(password2)<8):
            flash('Password must be at least 8 characters long', category='error')
        else:
            try:
                user_table = taskbook_db.get_table('user_cred')
                # first check if the user already exists
                user = user_table.find_one(email=email)
                if(user):
                    # flash alert and make them sign in again
                    flash('A user exists with that email address.', category='error')
                else:
                    # if new user, then hash the password, insert to table and log them in
                    hashed_password = generate_password_hash(password1, method='sha256')
                    user = dict(email=email, password=hashed_password, view='calendar')
                    user_table.insert(user)
                    flash('Sign up successful', category='success')
                    session['user_authenticated'] = True
                    session['user_email'] = email
                    # redirect to tasks page
                    return redirect(url_for('tasks'))
            except Exception as e:
                print(409, str(e))
                return ("409 Bad Request:"+str(e), 409)

    return render_template('register.html')


