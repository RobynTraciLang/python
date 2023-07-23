from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def checkerboard1():
    return render_template('index_copy.html')
# , row=8, column=8, color1="black", color2="red"

@app.route('/<int:row>')
def checkerboard2(row):
    return render_template('index.html', row=row, column=8, color1="black", color2="red")

@app.route('/<int:row>/<int:column>/')
def checkerboard3(row, column):
    return render_template('index.html', row=row, column=column, color1="black", color2="red")

@app.route('/<int:row>/<int:column>/<string:color1>')
def checkerboard4(row, column, color1):
    return render_template('index.html', row=row, column=column, color1=color1, color2="red")

@app.route('/<int:row>/<int:column>/<string:color1>/<string:color2>')
def checkerboard5(row, column, color1, color2):
    return render_template('index.html', row=row, column=column, color1=color1, color2=color2)

if __name__=="__main__":
    app.run(debug=True)