from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')
def play1():
    return render_template('index.html', number=3, color="#a0c4fc")

@app.route('/play/<int:number>')
def play2(number):
    return render_template('index.html', number=number, color="#a0c4fc")

@app.route('/play/<int:number>/<string:color>')
def play3(number, color):
    return render_template('index.html', number=number, color=color)

if __name__=="__main__":
    app.run(debug=True)