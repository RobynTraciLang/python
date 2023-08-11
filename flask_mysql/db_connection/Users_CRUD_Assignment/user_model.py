from mysqlconnection import connectToMySQL

db = 'users'

class User:

    def __init__(self, data):
        self.id = data['id'],
        self.first_name = data['first_name'],
        self.last_name = data['last_name'],
        self.email = data['email'],
        self.created_at = data['created_at'],
        self.updated_at = data['updated_at'],

    @classmethod
    def create_user(data):
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
        all_users = []
        for each_user in results:
            all_users.append(cls(each_user))
        return all_users


    @classmethod
    def select_one_user(cls, user_id):
        query = """
        SELECT * FROM users
        WHERE id = %(id)s
        ;"""
        data = {'id': user_id}
        results = connectToMySQL(db).query_db(query, data)
        return cls(results[0])

    # @classmethod
    # def get_one(cls, friend_id):
    #     query  = "SELECT * FROM friends WHERE id = %(id)s;"
    #     data = {'id':friend_id}
    #     results = connectToMySQL(cls.DB).query_db(query, data)
    #     return cls(results[0])

    # @classmethod
    # def select_all_users(cls):
    #     query = "SELECT * FROM friends;"
    #     results = connectToMySQL(cls.DB).query_db(query)
    #     friends = []
    #     for friend in results:
    #         friends.append( cls(friend) )
    #     return friends

# class Friend:
#     DB = "first_flask"
#     def __init__(self, data):
#         self.id = data['id']
#         self.first_name = data['first_name']
#         self.last_name = data['last_name']
#         self.occupation = data['occupation']
#         self.created_at = data['created_at']
#         self.updated_at = data['updated_at']

#     # the save method will be used when we need to save a new friend to our database
#     @classmethod
#     def save(cls, data):
#         query = """INSERT INTO friends (first_name,last_name,occupation)
#             VALUES (%(first_name)s,%(last_name)s,%(occupation)s);
#             """
#         result = connectToMySQL(cls.DB).query_db(query,data)
#         return result