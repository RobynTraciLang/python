# localhost:5000/ - have it say "Hello World!" DONE
# localhost:5000/dojo - have it say "Dojo!" DONE
# Create one url pattern and function that can handle the following examples:
# localhost:5000/say/flask - have it say "Hi Flask!" DONE
# localhost:5000/say/michael - have it say "Hi Michael!" DONE
# localhost:5000/say/john - have it say "Hi John!" DONE
# Create one url pattern and function that can handle the following examples (HINT: path variables are by default passed as strings. How might you handle a number?):
# localhost:5000/repeat/35/hello - have it say "hello" 35 times DONE
# localhost:5000/repeat/80/bye - have it say "bye" 80 times DONE
# localhost:5000/repeat/99/dogs - have it say "dogs" 99 times DONE

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

# @app.route('/repeat/<int:num>/<string:word>')
# def repeat_num_word(num, word):
#     return (word + " ") * num
# original way I did it

@app.route('/repeat/<int:num>/<string:word>')
def repeat_num_word(num, word):
    output = ""

    for i in range(num):
        output += f"<p>{word}</p>"

    return output
# tried this after viewing the solution video

@app.route('/<path:invalid_route>')
def handle_invalid_route(invalid_route):
    return "Sorry! No response. Try again."

if __name__=="__main__":
    app.run(debug=False) #usually True, but has to be set to False for the invalid route app to be recognized.


