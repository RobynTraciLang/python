from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
# from flask_app.models import cookie_order_model
import pprint
import re

db = 'cookie_orders'

class Cookie_order:
    def __init__(self, data):
        self.id = data['id']
        self.customer_name = data['customer_name']
        self.cookie_type = data['cookie_type']
        self.number_of_boxes = data['number_of_boxes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_cookie_order(cls, data):
        query = '''
        INSERT INTO cookie_orders (customer_name, cookie_type, number_of_boxes) VALUES (%(customer_name)s, %(cookie_type)s, %(number_of_boxes)s)
        ;'''
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def get_all_cookie_orders(cls):
        query = '''
        SELECT * FROM cookie_orders
        ;'''
        results = connectToMySQL(db).query_db(query)
        pprint.pprint(results, sort_dicts = False)
        return results


    @classmethod
    def get_one_cookie_order(cls, data):
        query = '''
       SELECT * FROM cookie_orders WHERE id = %(id)s
        ;'''
        this_cookie_order_id = {'id': data}
        results = connectToMySQL(db).query_db(query, this_cookie_order_id)
        return cls(results[0])


    @classmethod
    def update_cookie_order(cls, data):
        query = '''
        UPDATE cookie_orders SET customer_name = %(customer_name)s, cookie_type = %(cookie_type)s, number_of_boxes = %(number_of_boxes)s WHERE id = %(id)s
        ;'''
        # data = {'id': id}
        return connectToMySQL(db).query_db(query, data)


    @classmethod
    def delete_cookie_order(cls, data):
        query = '''
        DELETE FROM cookie_orders WHERE id = %(id)s
        ;'''
        data = {'id': id}
        return connectToMySQL(db).query_db(query, data)

    @staticmethod
    def validate_cookie_order(data):
        is_valid = True
        if len(data['customer_name']) < 2:
            flash('Customer Name must be at least 2 characters.')
            is_valid = False
        if len(data['cookie_type']) < 2:
            flash('Cookie Type must be at least 2 characters.')
            is_valid = False
        if len(data['number_of_boxes']) == 0:
            flash('Number of Boxes cannot be blank.')
            is_valid = False
        elif int(float(data['number_of_boxes'])) < 0:
            flash('Number of Boxes cannot be a negative number.')
            is_valid = False
        return is_valid