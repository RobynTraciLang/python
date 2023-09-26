from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja_model
import pprint

db = "dojos_and_ninjas"

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def create_dojo(cls, data):
        query = """
        INSERT INTO dojos (name) VALUES (%(name)s)
        ;"""
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def get_all_dojos(cls):
        query = """
        SELECT * FROM dojos
        ;"""
        results = connectToMySQL(db).query_db(query)
        pprint.pprint(results, sort_dicts = False)
        dojos = []
        for dojo in results:
            dojo_instance = cls(dojo)
            dojos.append(dojo_instance)
        return dojos

    # won't need get all, only get one
    @classmethod
    def get_one_dojo(cls, data):
        query = """
        SELECT * FROM dojos WHERE id = %(dojo_id)s
        ;"""
        this_dojo_id = {'dojo_id': data}
        results = connectToMySQL(db).query_db(query, this_dojo_id)
        return cls(results[0])

    @classmethod
    def get_one_dojo_with_associated_ninjas(cls, data):
        query = """
        SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s
        ;"""
        # get one requires a WHERE statement
        dojo_id = {
            'id': data
        }
        results = connectToMySQL(db).query_db(query, dojo_id)
        pprint.pprint(results, sort_dicts = False)
        dojo = cls(results[0])
        pprint.pprint(dojo, sort_dicts=False)
        for db_row in results:
            ninja_data = {
                'id': db_row['ninjas.id'],
                'first_name': db_row['first_name'],
                'last_name': db_row['last_name'],
                'age': db_row['age'],
                'created_at': db_row['ninjas.created_at'],
                'updated_at': db_row['ninjas.updated_at'],
                # 'dojo_id': db_row['dojo_id']
                # you can leave out the 'dojo' attribute, because it has the default value of None, which means it won't break if you don't add anything to it.
            }
            ninja_instance = ninja_model.Ninja(ninja_data)
            dojo.ninjas.append(ninja_instance)
        return dojo

    #     @classmethod
    # def get_one_dojo_with_all_ninjas(cls, data):
    #     query = """
    #     SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s
    #     ;"""
    #     results = connectToMySQL(db).query_db(query, data)
    #     pprint.pprint(results, sort_dicts = False)
    #     dojo_instance = dojo_model.Dojo(results[0])
    #     for ninja in results:
    #         ninja_data = {
    #             'id': ninja['ninjas.id'],
    #             'first_name': ninja['first_name'],
    #             'last_name': ninja['last_name'],
    #             'age': ninja['age'],
    #             'created_at': ninja['ninjas.created_at'],
    #             'updated_at': ninja['ninjas.updated_at'],
    #             # 'dojo_id': ninja['dojo_id'],
    #             # 'dojo': ninja['dojo']
    #         }
    #         ninja_instance = cls(ninja_data)
    #         dojo_instance.ninjas.append(ninja_instance)
    #     return dojo_instance