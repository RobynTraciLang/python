from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user_model
from flask import flash
import pprint
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


db = 'recipes'

#the many
class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.under_30_minutes = data['under_30_minutes']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = None

    @classmethod
    def create_recipe(cls, data):
        query = '''
        INSERT INTO recipes (name, description, instructions, date_made, under_30_minutes, user_id) VALUES (%(name)s, %(description)s, %(instructions)s, %(date_made)s, %(under_30_minutes)s, %(user_id)s)
        ;'''
        return connectToMySQL(db).query_db(query, data)
    # this works

    # takes data dictionary from request.form
    # validates data
    # return id? or False if the validations fail

    @classmethod
    def get_all_recipes_with_user(cls):
        query = '''
        SELECT * FROM recipes LEFT JOIN users ON recipes.user_id = users.id
        ;'''
        results = connectToMySQL(db).query_db(query)
        recipes = []
        for db_row in results:
            recipe_instance = cls(db_row)
            user_data = {
                'id': db_row['users.id'],
                'first_name': db_row['first_name'],
                'last_name': db_row['last_name'],
                'email': db_row['email'],
                'password': None,
                'created_at': db_row['users.created_at'],
                'updated_at': db_row['users.updated_at'],
            }
            recipe_instance.user = user_model.User(user_data)
            recipes.append(recipe_instance)
        pprint.pprint(results, sort_dicts = False)
        return recipes
    # this works

    # get all recipes, and the user info for the creators
    # make a list to hold recipe objects to return
    # return the list of class instances
    # whenever we are sending back data, we want it to be in the form of a class instance
    # a class instance is a way to keep all of your data organized, and attributes can be added on

    @classmethod
    def get_recipe_by_id(cls, data):
        query = '''
        SELECT * from recipes LEFT JOIN users on recipes.user_id = users.id WHERE recipes.id = %(id)s
        ;'''
        recipe_id = {
            'id': data
        }
        result = connectToMySQL(db).query_db(query, recipe_id)
        pprint.pprint(result, sort_dicts=False)
        recipe_instance = cls(result[0])
        for recipe in result:
            user_data = {
                'id': recipe['users.id'],
                'first_name': recipe['first_name'],
                'last_name': recipe['last_name'],
                'email': recipe['email'],
                'password': None,
                'created_at': recipe['users.created_at'],
                'updated_at': recipe['users.updated_at'],
            }
            user_instance = user_model.User(user_data)
            recipe_instance.user = user_instance
        return recipe_instance
    # get recipe data with user data who created it
    # make a recipe object from the data
    # associate user with recipe
    # return recipe


    @classmethod
    def edit_recipe(cls, data):
        query = '''
        UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, date_made = %(date_made)s, under_30_minutes = %(under_30_minutes)s WHERE id = %(id)s
        ;'''
        return connectToMySQL(db).query_db(query, data)
    # takes data dictionary from request.form


    @classmethod
    def delete_recipe(cls, recipe_id):
        query = '''
        DELETE FROM recipes WHERE id = %(id)s
        ;'''
        data = {'id': recipe_id}
        return connectToMySQL(db).query_db(query, data)
    # delete recipe using the id