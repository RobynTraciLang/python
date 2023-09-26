from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models import user_model, recipe_model
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
import pprint


@app.route('/')
def display_login_page():
    return render_template('1_login_or_register.html')
# this works


@app.route('/register', methods = ['POST'])
def register_new_user():
    if not user_model.User.validate_user_registration(request.form):
        return redirect('/')
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': bcrypt.generate_password_hash(request.form['password'])
    }
    id = user_model.User.create_user(data)
    session['user_id'] = id
    return redirect('/recipes')
# this works


@app.route('/login', methods = ['POST'])
def login():
    data = {
        'email': request.form['email']
    }
    user = user_model.User.get_user_by_email(data)
    if not user:
        flash('Invalid Email/Password', 'login')
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash('Invalid Email/Password', 'login')
        return redirect('/')
    session['user_id'] = user.id
    pprint.pprint(f"The id of the logged in user is {session['user_id']}")
    return redirect('/recipes')
# this works


@app.route('/logout')
def logout():
    session.clear()
    print('Session has been cleared.')
    return redirect('/')
# this works

# EXAM TIP: copy everything but pipfiles and mwb, just flask_app and server.py, make a folder called exam, right click on flask_app to copy it, paste it in the exam folder, then do same for server.py


