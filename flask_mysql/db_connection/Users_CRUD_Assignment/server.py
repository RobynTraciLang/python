from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'aravind krishnaswamy'

from user_model import User

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/create_user', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        User.create_user(request.form)
        return redirect('/')
    else:

    return redirect('read_all.html')

@app.route('/read_all')
def read_all():
    all_users = User.select_all_users()
    return render_template('index.html')

# @app.route('/')
# def index():
#     # calling the get_all method from the friends.py
#     all_friends=Friend.get_all()
#     # passing all friends to our template so we can display them there
#     return render_template("index.html",friends=all_friends)
# @app.route('/friend/show/<int:friend_id>')
# def show(friend_id):
#     # calling the get_one method and supplying it with the id of the friend we want to get
#     friend=Friend.get_one(friend_id)
#     return render_template("show_friend.html",friend=friend)

if __name__=='__main__':
    app.run(debug=True)