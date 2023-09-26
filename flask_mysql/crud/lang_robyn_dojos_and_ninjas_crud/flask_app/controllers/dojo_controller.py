from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models import dojo_model
from flask_app.models import ninja_model

@app.route('/dojo/create_dojo')
def create_dojo_form():
    dojo = dojo_model.Dojo.get_all_dojos()
    return render_template('new_dojo.html', dojo = dojo)

@app.route('/dojo/create_dojo', methods = ['POST'])
def create_dojo():
    dojo = dojo_model.Dojo.create_dojo(request.form)
    return redirect('/dojo/create_dojo')

# @app.route('/dojo/show_dojo/<int:id>')
# def show_one_dojo(id):
#     dojo = ninja_model.Ninja.get_one_dojo_with_all_ninjas(id)
#     # ninja = ninja_model.Ninja.get_all_ninjas_with_dojo()
#     return render_template('dojo_show.html', dojo = dojo)

# @app.route('/dojo/show_dojo/<int:id>')
# def show_one_dojo(id):
#     dojo = dojo_model.Dojo.get_one_dojo(id)
#     ninja = ninja_model.Ninja.get_all_ninjas_with_dojo()
#     return render_template('show_dojo.html', dojo = dojo, ninja = ninja)