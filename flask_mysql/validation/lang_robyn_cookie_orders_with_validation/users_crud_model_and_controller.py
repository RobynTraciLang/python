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
