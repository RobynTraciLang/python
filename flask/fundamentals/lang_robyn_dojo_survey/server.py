from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "love is the more excellent way"

@app.route('/')
def index():
    print("homepage accessed.")
    print(session)
    session.clear()
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    print("processing...")
    print(request.form)
    session['name'] = request.form['name']
    session['dojo_location'] = request.form['dojo_location']
    session['favorite_programming_language'] = request.form['favorite_programming_language']
    session['comments'] = request.form['comments']
    print(session)
    return redirect('/result')

@app.route('/result')
def result():
    print("displaying results.")
    return render_template('result.html')

if __name__=="__main__":
    app.run(debug=True)