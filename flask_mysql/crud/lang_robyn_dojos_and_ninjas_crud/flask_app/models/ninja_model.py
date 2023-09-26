from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import dojo_model
import pprint

db = "dojos_and_ninjas"

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # self.dojo_id = data['dojo_id']
        self.dojo = None

    @classmethod
    def create_ninja(cls, data):
        query = """
        INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s)
        ;"""
        return connectToMySQL(db).query_db(query, data)

    # @classmethod
    # def get_all_ninjas(cls):
    #     query = """
    #     SELECT * FROM ninjas
    #     ;"""
    #     results = connectToMySQL(db).query_db(query)
    #     pprint.pprint(results, sort_dicts = False)
    #     ninjas = []
    #     for ninja in results:
    #         ninja_instance = cls(ninja)
    #         ninjas.append(ninja_instance)
    #     return ninjas

    @classmethod
    def get_one_dojo_with_all_ninjas(cls, data):
        query = """
        SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s
        ;"""
        results = connectToMySQL(db).query_db(query, data)
        pprint.pprint(results, sort_dicts = False)
        dojo_instance = dojo_model.Dojo(results[0])
        for ninja in results:
            ninja_data = {
                'id': ninja['ninjas.id'],
                'first_name': ninja['first_name'],
                'last_name': ninja['last_name'],
                'age': ninja['age'],
                'created_at': ninja['ninjas.created_at'],
                'updated_at': ninja['ninjas.updated_at'],
                # 'dojo_id': ninja['dojo_id'],
                # 'dojo': ninja['dojo']
            }
            ninja_instance = cls(ninja_data)
            dojo_instance.ninjas.append(ninja_instance)
        return dojo_instance

        # results = connectToMySQL(db).query_db(query, data)
        # pprint.pprint(results, sort_dicts = False)
        # ninja = cls(results[0])
        # pprint.pprint(ninja, sort_dicts=False)
        # for db_row in results:
        #     dojo_data = {
        #         'id': db_row['dojos.id'],
        #         'name': db_row['name'],
        #         'created_at': db_row['dojos.created_at'],
        #         'updated_at': db_row['dojos.updated_at'],
        #         'ninjas': db_row['dojos.ninjas'],
        #     }
        #     ninja.ninjas.append(dojo_model.Dojo(dojo_data))
        # return ninja


    @classmethod
    def get_all_ninjas_with_dojo(cls):
        query = """
        SELECT * FROM ninjas LEFT JOIN dojos ON dojos.id = ninjas.dojo_id
        ;"""
        results = connectToMySQL(db).query_db(query)
        ninjas = []
        for ninja in results:
            ninja_instance = cls(ninja)
            dojo_dictionary = {
                'id': ninja['dojos.id'],
                'name': ninja['name'],
                'updated_at': ninja['dojos.updated_at'],
                'created_at': ninja['dojos.created_at']
            }
            dojo_instance = dojo_model.Dojo(dojo_dictionary)
            ninja_instance.dojo = dojo_instance
            ninjas.append(ninja_instance)
        return ninjas


    # @classmethod
    # def get_one_ninja(cls, data):
    #     query = """
    #     SELECT * FROM ninjas WHERE id = %(ninja_id)s
    #     ;"""
    #     this_ninja_id = {'ninja_id': data}
    #     results = connectToMySQL(db).query_db(query, this_ninja_id)
    #     return cls(results[0])


    @classmethod
    def update_ninja(cls, data):
        query = """
        UPDATE ninjas SET first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s WHERE id = %(id)s
        ;"""
        return connectToMySQL(db).query_db(query, data)


    @classmethod
    def delete_ninja(cls, data):
        query = """
        DELETE FROM ninjas WHERE id = %(id)s
        ;"""
        data = {"id": id}
        return connectToMySQL(db).query_db(query, data)

    #  Could also do:
    # @classmethod
    # def delete_ninja(cls, id):
    #     query = """
    #     DELETE FROM ninjas WHERE id = %(id)s
    #     ;"""
    #     return connectToMySQL(db).query_db(query, {"id": id})