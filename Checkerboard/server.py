from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def standard():
    return render_template('index.html',x=8)

@app.route('/<int:x>')
def custom(x):
    return render_template('index.html',x=x)

if __name__=="__main__":      
    app.run(debug=True)  