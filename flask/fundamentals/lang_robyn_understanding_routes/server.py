# localhost:5000/ - have it say "Hello World!" DONE
# localhost:5000/dojo - have it say "Dojo!" DONE
# Create one url pattern and function that can handle the following examples:
# localhost:5000/say/flask - have it say "Hi Flask!" DONE
# localhost:5000/say/michael - have it say "Hi Michael!" DONE
# localhost:5000/say/john - have it say "Hi John!" DONE
# Create one url pattern and function that can handle the following examples (HINT: path variables are by default passed as strings. How might you handle a number?):
# localhost:5000/repeat/35/hello - have it say "hello" 35 times DONE
# localhost:5000/repeat/80/bye - have it say "bye" 80 times DONE
# localhost:5000/repeat/99/dogs - have it say "dogs" 99 times

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/flask')
def say_flask():
    return 'Hi Flask!'

@app.route('/say/<string:name>')
def say_john(name):
    return f"Hi {name.capitalize()}!"

@app.route('/repeat/<int:num>/<string:word>')
def repeat_num_hello(num, word):
    return (word + " ") * num

# @app.route('/repeat/<int:num>/hello')
# def repeat_num_hello(num):
#     return 'hello ' * num

# @app.route('/repeat/<int:num>/<string:bye>')
# def repeat_num_bye(num):
#     return 'bye ' * num

# @app.route('/repeat/<int:num>/dogs')
# def repeat_num_dogs(num):
#     return 'dogs ' * num

# @app.route('/')
#     return "Sorry! No response. Try again."

if __name__=="__main__":
    app.run(debug=True)


