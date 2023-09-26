from flask_app.config.mysqlconnection import connectToMySQL
import pprint

db = 'users'

class User:

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_user(cls, data):
        query = """
        INSERT INTO users (first_name, last_name, email)
        VALUES (%(first_name)s, %(last_name)s, %(email)s)
        ;"""
        results = connectToMySQL(db).query_db(query, data)
        return results

    @classmethod
    def select_all_users(cls):
        query = """
        SELECT * FROM users
        ;"""
        results = connectToMySQL(db).query_db(query)
        #data field is optional. don't need it for the "get all" methods
        pprint.pprint(results, sort_dicts=False)
        all_users = []
        for each_user in results:
            user_instance = cls(each_user)
            all_users.append(user_instance)
        return all_users


    @classmethod
    def select_one_user(cls, data):
        query = """
        SELECT * FROM users
        WHERE id = %(user_id)s
        ;"""
        this_user_id = {'user_id': data}
        results = connectToMySQL(db).query_db(query, this_user_id)
        pprint.pprint(results, sort_dicts=False)
        # pprint.pprint(cls(results[0]).__dict__)
        return cls(results[0])
    # this one works! Success!

    @classmethod
    def update_user(cls, data):
        query = """
        UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s
        WHERE id = %(id)s
        ;"""
        results = connectToMySQL(db).query_db(query, data)
        return results

    @classmethod
    def delete_user(cls, user_id):
        query = """
        DELETE FROM users WHERE id = %(id)s
        ;"""
        data = {
            'id': user_id
        }
        results = connectToMySQL(db).query_db(query, data)
        return results