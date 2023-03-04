from flask import Flask, render_template, redirect, session, request  

app = Flask(__name__)
app.secret_key = "secret"   

@app.route('/')
def actual_visits():
    if 'actual_visits' not in session:
        session['actual_visits'] = 0
    else:
        session['actual_visits'] += 1    
        
    if 'added_visits' not in session:        
        session['added_visits'] = 0
    else:
        session['added_visits'] += 0
        
    if 'total_visits' not in session:        
        session['total_visits'] = 0
    else:
        session['total_visits'] += 1
    return render_template('index.html')
    
@app.route('/destroy_session')
def clear_data():
    session.clear()
    return redirect('/')

@app.route('/add_two')
def plus_two():
    session['total_visits'] += 1
    session['added_visits'] += 2  
    session['actual_visits'] -= 1
    return redirect('/')

@app.route('/add_custom', methods=['POST'])
def add_custom():   
    session['number'] = int(request.form['number']) - 1
    session['total_visits'] += session['number']
    session['added_visits'] += session['number']
    session['actual_visits'] -= 1
    return redirect('/')
    
    
    
    

if __name__=="__main__":
    app.run(debug=True)  