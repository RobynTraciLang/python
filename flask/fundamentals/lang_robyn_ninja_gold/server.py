from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'aravind krishnaswamy'






@app.route('/')
def index():
    if "gold" not in session:
        session['gold'] = 0
        session['count_of_times_played'] = 0
        session['level'] = 0
    if "message" not in session:
        session['message'] = "Click any button to play!"
    if "remaining_plays" not in session:
        session['remaining_plays'] = 50

    return render_template('index_rename_1.html')





@app.route('/process_money', methods = ['POST'])
def process_money():
    print(request.form)
    print(session)

    session['building_choice'] = request.form['building']
    print(request.form['building'])
    print(session['building_choice'])

    # random_number_farm = random.randint(10,20)
    # random_number_cave = random.randint(5,10)
    # random_number_house = random.randint(2,5)
    # random_number_casino = random.randint(-50,50)
    # random_wild_card = random.randint(75,150)
    # random_number = random.randint(5,15)

    # print(random_number_farm)
    # print(random_number_cave)
    # print(random_number_house)
    # print(random_number_casino)
    # print(random_wild_card)
    # print(random_number)


    building_gold = {
        "farm": random.randint(10,20),
        "cave": random.randint(5,10),
        "house": random.randint(2,5),
        "casino": random.randint(-50,50),
        "random_wild_card": random.randint(75,150),
        "random_number": random.randint(6,10),
    }

    if "activities" not in session:
        session['activities'] = []


    if session['count_of_times_played'] % building_gold['random_number'] == 7:
        session['gold'] += building_gold['random_wild_card']
        print(f"OMG!!! You found a wild card!!! You just got {building_gold['random_wild_card']} golds richer!!!")
        session['activities'].append({'color': 'fuchsia', 'message': f"OMG!!! You found a wild card!!! You just got {building_gold['random_wild_card']} golds richer!!!"})
        print(session['activities'])
    else:
        session['gold'] += building_gold[request.form['building']]
        if request.form['building'] == "casino":

            if building_gold['casino'] < 0:
                verb = "lost"
                session['activities'].append({'color': 'red', 'message': f"You just {verb} {building_gold['casino']} golds from the casino!"})
            else:
                verb = "mined"
                session['activities'].append({'color': 'green', 'message': f"You just {verb} {building_gold['casino']} golds from the casino!"})
            print(f"You just {verb} {building_gold['casino']} golds from the casino!")
            print(session['gold'])
            print(session['count_of_times_played'])
        else:
            session['activities'].append({'color': 'green', 'message': f"You just mined {building_gold[request.form['building']]} golds from the {request.form['building']}!"})

    session['count_of_times_played'] += 1

    session['remaining_plays'] -= 1


    # if session['building_choice'] == "farm":
    #     session['gold'] += random_number_farm
    #     # message.append(f"You just mined {random_number_farm} golds from the farm!")
    #     print(f"You just mined {random_number_farm} golds from the farm!")
    #     session['count_of_times_played'] += 1
    #     print(session['gold'])
    #     print(session['count_of_times_played'])
    #     session['activities'].append({'color': 'green', 'message': f"You just mined {random_number_farm} golds from the farm!"})
    # if session['building_choice'] == "cave":
    #     session['gold'] += random_number_cave
    #     # message.append(f"You just mined {random_number_cave} golds from the cave!")
    #     print(f"You just mined {random_number_cave} golds from the cave!")
    #     session['count_of_times_played'] += 1
    #     print(session['gold'])
    #     print(session['count_of_times_played'])
    #     session['activities'].append({'color': 'green', 'message': f"You just mined {random_number_cave} golds from the cave!"})
    # if session['building_choice'] == "house":
    #     session['gold'] += random_number_house
    #     # message.append(f"You just mined {random_number_house} golds from the house!")
    #     print(f"You just mined {random_number_house} golds from the house!")
    #     session['count_of_times_played'] += 1
    #     print(session['gold'])
    #     print(session['count_of_times_played'])
    #     session['activities'].append({'color': 'green', 'message': f"You just mined {building_gold['house']} golds from the house!"})


    if session['gold'] <= 0:
        session['you_lose'] = "YOU LOSE!!!"
        return redirect('/')
    if (session['gold'] > 0) and (session['gold'] <= 99):
        session['level_announcement'] = "You are on Level 0!"
        session['level'] = 0
    if (session['gold'] >= 100) and (session['gold'] <= 199):
        session['level_announcement'] = "You have reached Level 1!"
        session['level'] = 1
    if (session['gold'] >= 200) and (session['gold'] <= 299):
        session['level_announcement'] = "You have reached Level 2!"
        session['level'] = 2
    if (session['gold'] >= 300) and (session['gold'] <= 399):
        session['level_announcement'] = "You have reached Level 3!"
        session['level'] = 3
    if (session['gold'] >= 400) and (session['gold'] <= 499):
        session['level_announcement'] = "You have reached Level 4!"
        session['level'] = 4
    if session['gold'] >= 500 and session['remaining_plays'] >= 1:
        session['level_announcement'] = "AMAZING!!! You have found all the gold in town!!! Now you can retire and never work another day in your life. Congratulations!!!"
        session['level'] = 5
        session['you_win'] = "you won!!!"

    # message.append(f"The amount of gold is now {session['gold']}!")


    return redirect('/')






@app.route('/clear_session')
def clear_session():
    session.clear()
    return redirect('/')







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