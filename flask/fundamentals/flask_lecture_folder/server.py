from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route("/class")
def class_names():
    return 'this is our class'

@app.route("/class/<string:name_of_students>")
# will work without the "string:", but it's a good habit to form
def hello_student(name_of_student):
    return f'Hello {name_of_student}'

@app.route("/class/<string:name_of_students>/<int:number_of_times>")
# will work without the "string:", but it's a good habit to form
def hello_student_number_of_times(name_of_student, number_of_times):
    return f'Hello {name_of_student * number_of_times}!'

@app.route("/hello")
def hello():
    return render_template('hello.html', phrase="hello!", times=5)

if __name__=="__main__":
    app.run(debug=True)
    # 5001 or 8000 for MAC. Run in port 5001 if something is in use in 5000