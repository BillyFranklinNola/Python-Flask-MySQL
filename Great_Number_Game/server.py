from flask import Flask, render_template, redirect, request, session
import random

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def random_number():
    if 'num' not in session:
        session['num'] = random.randint(1,100)
    if 'number_of_guesses' not in session:
        session['number_of_guesses'] = 0
        
    print(session['num'])
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess_feedback():
    session['number_of_guesses'] += 1   
    session['guess'] = int(request.form['guess'])
    if session['guess'] > session['num']:
        session['answer'] = "Too high, try again..."
    elif session['guess'] < session['num']:
        session['answer'] = "Too low, try again..."
    elif session['guess'] == session['num']:
        session['answer'] = "Hot Diggity Dog, you're a Weener!!!"
    return redirect('/')

@app.route('/destroy_session')
def clear_data():
    session.clear()
    return redirect('/')
        
if __name__=="__main__":
    app.run(debug=True)  
    