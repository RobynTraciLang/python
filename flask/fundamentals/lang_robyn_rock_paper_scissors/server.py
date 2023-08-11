from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'aravind krishnaswamy'

@app.route('/')
def index():
    if "draw" not in session:
        session['win'] = 0
        session['lose'] = 0
        session['draw'] = 0
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    if 'outcomes' not in session:
        session['outcomes'] = []
    print(request.form)
    session['user_choice'] = request.form['user_choice']
    print(f"The user's choice is {session['user_choice']}")
    random_number = random.randint(0,2)
    print(f"The random number between 0 and 2 is {random_number}. This will be the index.")
    choices = ["Rock","Paper","Scissors"]
    opponents_choice = choices[random_number]
    print(f"The opponent's choice is {opponents_choice}.")
    session['opponents_choice'] = opponents_choice

    if session['user_choice'] == opponents_choice:
        session['draw'] += 1
        session['last_result'] = "draw"
        color = "blue"

    elif (session['user_choice'] == "Paper" and session['opponents_choice'] == "Scissors") or (session['user_choice'] == "Rock" and session['opponents_choice'] == "Paper") or (session['user_choice'] == "Scissors" and session['opponents_choice'] == "Rock"):
        session['lose'] += 1
        session['last_result'] = "lose"
        color = "red"

    elif (session['user_choice'] == "Paper" and session['opponents_choice'] == "Rock") or (session['user_choice'] == "Rock" and session['opponents_choice'] == "Scissors") or (session['user_choice'] == "Scissors" and session['opponents_choice'] == "Paper"):
        session['win'] += 1
        session['last_result'] = "win"
        color = "green"

    session['outcomes'].append({"message": f'You chose {session["user_choice"]}. Your opponent chose {session["opponents_choice"]}. You {session["last_result"]}.', "color": color})

    return redirect('/')

@app.route('/clear_session')
def clear_session():
    session.clear()
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)

# rock beats scissors
# scissors beat paper
# paper covers rock
# choose the same, it's a draw