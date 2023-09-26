from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user_model import User

@app.route('/create')
def display_create_page():
    return render_template('create.html')

@app.route('/create', methods=['POST'])
def create_user():
    this_user = User.create_user(request.form)
    return redirect('/read_all')

@app.route('/read_all')
def display_read_page():
    user_list = User.select_all_users()
    return render_template('read_all.html', users = user_list)

@app.route('/read_all', methods = ['POST'])
def read_all():
    all_users = User.select_all_users()
    return redirect('/create', all_users = all_users)

@app.route('/read_one/<int:id>')
def display_read_one_page(id):
    this_user = User.select_one_user(id)
    return render_template('read_one.html', user = this_user)

@app.route('/read_one/<int:id>', methods=['POST'])
def read_one(id):
    User.select_one_user(id)
    return redirect('/read_one/<int:id>')

@app.route('/update/<int:id>')
def display_update_user_page(id):
    update_this_user = User.select_one_user(id)
    return render_template('edit.html', user = update_this_user)

@app.route('/update/<int:id>', methods=['POST'])
def update_user(id):
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'id': id
    }
    User.update_user(data)
    return redirect(f'/read_one/{id}')

@app.route('/delete/<int:id>')
def delete_user(id):
    User.delete_user(id)
    return redirect('/read_all')