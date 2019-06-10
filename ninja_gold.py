from flask import Flask, render_template, request, redirect, session
import random 

app = Flask(__name__)
app.secret_key = 'Shhh'

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
    if 'activity' not in session:
        session['activity'] = []
    return render_template('index.html', gold_amt = session['gold'], activity_log = session['activity'])

@app.route('/process_money', methods=['POST'])
def gold():
    farm_gold = random.randint(10,20)
    cave_gold = random.randint(5,10)
    house_gold = random.randint(2,5)
    casino_gold = random.randint(-50,50)

    if request.form['land_type'] == 'farm':
        session['gold'] += farm_gold
        session['activity'].append('You got: ' + str(farm_gold))

    if request.form['land_type'] == 'cave':
        session['gold'] += cave_gold
        session['activity'].append('You got: ' + str(cave_gold))

    if request.form['land_type'] == 'house':
        session['gold'] += house_gold
        session['activity'].append('You got: ' + str(house_gold))

    if request.form['land_type'] == 'casino':
        session['gold'] += casino_gold
        session['activity'].append('You got: ' + str(casino_gold))

    print(session['gold'])
    return redirect('/')

@app.route('/clear', methods=['POST'])
def clear():
    session['gold'] = 0
    session['activity'] = []
    return redirect('/')
    
if __name__ == '__main__':
    app.run(debug = True)
