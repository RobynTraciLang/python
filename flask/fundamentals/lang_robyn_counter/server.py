from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes
# was 'keep it secret, keep it safe'

@app.route('/')
def user_form_to_fill_out():
    if "visit_count" in session:
        session['visit_count'] += 1
    else:
        session['visit_count'] = 1
    return render_template('index.html')

@app.route('/destroy_session')
def destroy_session():
    session.clear()		# clears all keys
    # session.pop('key_name')		# clears a specific key
    return redirect('/')

@app.route('/increment_twice')
def increment_twice():
    session['visit_count'] += 2
    return render_template('index.html')

@app.route('/visit_number_user_choice')
def visit_number_user_choice():
    return render_template('index.html')

@app.route('/increment_by_user_supplied_number', methods=['POST'])
def increment_by_user_supplied_number():
    session['visit_count'] += (int(request.form['visit_number_user_choice'])-1)
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)

