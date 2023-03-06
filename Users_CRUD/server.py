from flask import Flask, render_template, request, redirect

from user import User

app = Flask(__name__)

@app.route('/read')
def user_list():
    users = User.get_all()
    print(users)
    return render_template('read.html', all_users = users)

@app.route('/user/show/<int:id>')
def user_info(id):
    data = {'id':id}
    return render_template('show.html',user=User.get_one(data))

@app.route('/user/edit/<int:id>')
def edit_user(id):
    data={'id':id}
    return render_template('edit.html',user=User.get_one(data))

@app.route('/user/update',methods={"POST"})
def update_user():
    User.update_user(request.form)
    return redirect('/read')

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

@app.route('/user/delete/<int:id>')
def delete_user(id):
    user_id = {'id':id}
    User.delete(user_id)
    return redirect('/read')


if __name__ == "__main__":
    app.run(debug=True)