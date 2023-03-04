from flask import Flask, render_template, request, redirect

from user import User

app = Flask(__name__)

@app.route('/read')
def user_list():
    users = User.get_all()
    print(users)
    return render_template('read.html', all_users = users)

@app.route('/user/add', methods={"POST"})
def add_user():
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    User.save(data)
    return redirect('/read')

@app.route('/create')
def new_user():
    return render_template('create.html')


if __name__ == "__main__":
    app.run(debug=True)