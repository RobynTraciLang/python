from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'aravind krishnaswamy'

@app.route('/')
def index():
    if "gold" not in session:
        session['gold'] = 0
    return render_template('/index_rename_1.html')

@app.route('/process_money', methods = ['POST'])
def process_money():
    print(request.form)

    # if "player_name" not in session:
    #     session['player_name'] = request.form['player_name']
    # player_name = session['player_name']

    session['building_choice'] = request.form['building']
    print(request.form['building'])
    print(session['building_choice'])

    random_number_farm = random.randint(10,20)
    random_number_cave = random.randint(5,10)
    random_number_house = random.randint(2,5)
    random_number_casino = random.randint(-50,50)
    random_wild_card = random.randint(500,2000)

    looper_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]

    for i in looper_list:
        if session['building_choice'] == "farm":
            session['gold'] += random_number_farm
            print(f"You just mined {random_number_farm} golds from the farm!")
        if session['building_choice'] == "cave":
            session['gold'] += random_number_cave
            print(f"You just mined {random_number_cave} golds from the cave!")
        if session['building_choice'] == "house":
            session['gold'] += random_number_house
            print(f"You just mined {random_number_house} golds from the house!")
        if session['building_choice'] == "casino":
            session['gold'] += random_number_casino
            if random_number_casino < 0:
                verb = "lost"
            else:
                verb = "mined"
            print(f"You just {verb} {random_number_casino} golds from the casino!")
        if (i == 25) or (i == 50):
            session['gold'] += random_wild_card
            print(f"OMG!!! You found a wild card!!! You just got {{random_wild_card}} golds richer!!!")

    if session['gold'] <= 0:
        session['you_lose'] = f"{{player_name}}, you have no more money!! YOU LOSE"
    if session['gold'] >= 100:
        session['level_two'] = f"Congratulations, {{player_name}}!! You have reached Level 2!"
    if session['gold'] >= 500:
        session['level_three'] = f"Congratulations, {{player_name}}!! You have reached Level 3!"
    if session['gold'] >= 1000:
        session['level_four'] = f"Congratulations, {{player_name}}!! You have reached Level 4!"
    if session['gold'] >= 5000:
        session['level_five'] = f"Congratulations, {{player_name}}!! You have reached Level 3!"
    if session['gold'] >= 10000:
        session['level_two'] = f"AMAZING!!! You have found all the gold in town!!! Now you can retire and never work another day in your life. Congratulations {{player_name}}!!"

    message = f"The amount of gold is now {session['gold']}!"

    print(message)
    return redirect('/', player_name = session['player_name'])

@app.route('/clear_session')
def clear_session():
    session.clear()
    return render_template('index_rename_1.html')

if __name__=='__main__':
    app.run(debug=True)

"""
Create a simple game to test your understanding of Flask, and implement the functionality below.

For this assignment, you're going to create a mini game that helps a ninja make some money! When you start the game, your ninja should have 0 gold. The ninja can go to different places (farm, cave, house, casino) and earn different amounts of gold. In the case of a casino, your ninja can earn or lose up to 50 gold. Your job is to create a web app that allows this ninja to earn gold and to display their past activities.

The root route should display the wireframe below. There should be 4 forms on the HTML page. As an example, the farm form might look something like this:

<form action="/process_money" method="post">
    <input type="hidden" name="building" value="farm" />
    <input type="submit" value="Find Gold!"/>
</form>

There should be a method that handles the POST request, determining how much gold the user should now have depending on their visit.

Note: You should only have 2 routes for this assignment -- '/' and '/process_money'
"""


"""
@app.route('/process_money', methods = ['POST'])
def process_money():
    print(request.form)

    # if "player_name" not in session:
    #     session['player_name'] = request.form['player_name']
    # player_name = session['player_name']

    session['building_choice'] = request.form['building']
    print(request.form['building'])
    print(session['building_choice'])

    random_number_farm = random.randint(10,20)
    random_number_cave = random.randint(5,10)
    random_number_house = random.randint(2,5)
    random_number_casino = random.randint(-50,50)
    random_wild_card = random.randint(500,2000)

    looper_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]

    for i in looper_list:
        if session['building_choice'] == "farm":
            if (i ==25) or (i == 50):
                continue
            if (i >= 1) or (i <=24) or (i >=26) or (i<=49):
                session['gold'] += random_number_farm
                print(f"You just mined {random_number_farm} golds from the farm!")
        if session['building_choice'] == "cave":
            if (i == 25) or (i == 50):
                continue
            else:
                session['gold'] += random_number_cave
                print(f"You just mined {random_number_cave} golds from the cave!")
        if session['building_choice'] == "house":
            if (i ==25) or (i == 50):
                continue
            else:
                session['gold'] += random_number_house
                print(f"You just mined {random_number_house} golds from the house!")
        if session['building_choice'] == "casino":
            if (i ==25) or (i == 50):
                continue
            else:
                session['gold'] += random_number_casino
                if random_number_casino < 0:
                    verb = "lost"
                else:
                    verb = "mined"
                print(f"You just {verb} {random_number_casino} golds from the casino!")
        if (i == 25) or (i == 50):
            session['gold'] += random_wild_card
            print(f"OMG!!! You found a wild card!!! You just got {{random_wild_card}} golds richer!!!")

    if session['gold'] <= 0:
        session['you_lose'] = "You have no more money!! YOU LOSE"
    if session['gold'] >= 100:
        session['level_two'] = "Congratulations!! You have reached Level 2!"
    if session['gold'] >= 500:
        session['level_three'] = "Congratulations!! You have reached Level 3!"
    if session['gold'] >= 1000:
        session['level_four'] = "Congratulations!! You have reached Level 4!"
    if session['gold'] >= 5000:
        session['level_five'] = "Congratulations!! You have reached Level 3!"
    if session['gold'] >= 10000:
        session['level_two'] = "AMAZING!!! You have found all the gold in town!!! Now you can retire and never work another day in your life. Congratulations!!!"

    message = f"The amount of gold is now {session['gold']}!"

    print(message)
    return redirect('/')
"""