from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = "hey there billy joe bob!"

@app.route('/')
def index():
    if "random_number" not in session:
        session['random_number'] = random.randint(1,100)
        print(f"The random number is {session['random_number']}.")
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    user_guess = int(request.form['guessed_number'])
    session['guessed_number'] = user_guess
    return redirect('/')

@app.route('/play_again')
def play_again():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)