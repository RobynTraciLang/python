from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models import ninja_model
from flask_app.models import dojo_model

@app.route('/')
def index():
    pass
    return render_template('index.html')

@app.route('/ninja/create_ninja')
def display_ninja_form():
    dojo = dojo_model.Dojo.get_all_dojos()
    # ninja = ninja_model.Ninja.get_all_ninjas()
    return render_template('new_ninja.html', dojo = dojo)
# ninja = ninja

@app.route('/ninja/create_ninja', methods = ['POST'])
def create_ninja():
    ninja_model.Ninja.create_ninja(request.form)
    return redirect('/dojo/create_dojo')

# @app.route('/ninja/create_ninja', methods = ['POST'])
# def create_ninja():
#     data = {
#         "first_name":request.form['first_name'],
#         "last_name":request.form['last_name'],
#         "age":request.form['age'],
#         "dojo_id":request.form['dojo_id'],
#     }
#     ninja = ninja_model.Ninja(data)
#     return redirect('/', ninja = ninja)

@app.route('/ninja/show_dojo_with_ninjas/<int:id>')
def show_dojo_with_ninjas_page(id):
    data = {
            'id': id
        }
    dojo = ninja_model.Ninja.get_one_dojo_with_all_ninjas(data)
    return render_template('dojo_show.html', dojo = dojo)

# @app.route('/ninja/show_ninjas', methods = ['POST'])
# def show_ninjas():

#     return redirect('/')


#     from flask_app.models.burger import Burger
# @app.route('/create/burger',methods=['POST'])
# def create_burger():
# 	data = {
#         	"name" : request.form['name'],
#         	"bun" : request.form['bun'],
#         	"meat" : request.form['meat'],
#         	"calories" : request.form['calories']
# 	}
# 	Burger.save(data)
# 	return redirect('/burgers')


# @app.route('/ninjas')
# def display_ninjas_page():
# 	return render_template('results.html', ninjas = ninja_model.Ninja.get_all_ninjas())