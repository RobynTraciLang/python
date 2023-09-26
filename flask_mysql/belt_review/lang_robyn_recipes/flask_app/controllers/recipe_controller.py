from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models import user_model
from flask_app.models import recipe_model
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/recipes')
def dashboard():
    if 'user_id' not in session:
        flash('You need to log in to access this page.', 'not_logged_in')
        return redirect('/')
    data = {
        'id': session['user_id']
    }
    recipes = recipe_model.Recipe.get_all_recipes_with_user()

    return render_template('2_dashboard.html', user = user_model.User.get_user_by_id(data), recipes = recipes)
# this works

@app.route('/recipes/new')
def display_create_recipe_form():
    return render_template('3_add_new_recipe.html')
# this works

@app.route('/recipes/new', methods = ['POST'])
def create_recipe():
    if not user_model.User.validate_recipe(request.form):
        return redirect('/recipes/new')
    data = {
            'name': request.form['name'],
            'description': request.form['description'],
            'instructions': request.form['instructions'],
            'date_made': request.form['date_made'],
            'under_30_minutes': request.form['under_30_minutes'],
            'user_id': session['user_id'],
        }
    recipe_model.Recipe.create_recipe(data)
    return redirect('/recipes')
# this works

@app.route('/recipes/<int:id>')
def display_one_recipe_of_a_user(id):
    recipe = recipe_model.Recipe.get_recipe_by_id(id)
    return render_template('4_display_one_recipe.html', recipe = recipe)

@app.route('/recipes/edit/<int:id>')
def display_edit_recipe_page(id):
    recipe = recipe_model.Recipe.get_recipe_by_id(id)
    return render_template('5_edit_recipe.html', recipe = recipe)

@app.route('/recipes/edit/<int:id>', methods = ['POST'])
def edit_one_recipe(id):
    if not user_model.User.validate_recipe(request.form):
        return redirect(f'/recipes/edit/{id}')
    data = {
        'id': id,
        'name': request.form['name'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'date_made': request.form['date_made'],
        'under_30_minutes': request.form['under_30_minutes'],
    }
    recipe_model.Recipe.edit_recipe(data)
    return redirect('/recipes')

@app.route('/recipes/delete/<int:id>')
def delete_recipe(id):
    recipe_model.Recipe.delete_recipe(id)
    return redirect('/recipes')