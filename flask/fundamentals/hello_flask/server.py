from flask import Flask, render_template  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

# The "@" decorator associates this route with the function immediately following
@app.route('/')
def hello_world():
    return render_template("index.html") # Return the string 'Hello World!' as a response.

@app.route('/success')
def success():
    return "success"

# @app.route('/hello/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
# def hello(name):
#     print(name)
#     return "Hello, " + name

@app.route('/users/<string:username>/<string:id>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id

@app.route('/hello/<string:name>/<int:num>')
def hello(name, num):
    # return f"Hello, {name * num}"
    return render_template("hello.html", name=name, num=num)


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
        # app.run(debug=True) should be the very last statement!

