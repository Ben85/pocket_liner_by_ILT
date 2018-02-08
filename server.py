from flask import Flask, flash, redirect, render_template, url_for, request, session
import data_manager
import validation
from functools import wraps

app = Flask(__name__)


def login_required(function):
    @wraps(function)
    def decorated_function(args, **kwargs):
        if session == {}:
            flash("For this you need to log in")
            return redirect(url_for('login', next=request.url))
        return function(args, **kwargs)
    return decorated_function


@app.route('/', methods=['GET', 'POST'])
def route_index():
    return render_template('index.html')


@app.route('/registration', methods=['POST', 'GET'])
def route_register():
    user_data = request.form.to_dict()

    data_manager.register_user(user_data)
    return redirect(url_for('route_index'))


@app.route('/login', methods=['POST', 'GET'])
def route_login():
    if request.method == 'POST':
        if validation.is_user_pass(request.form['password'], session['id']):
            session['id'] = data_manager.get_user_id_by_email(request.form['e_mail'])
        else:
            raise ValueError

    return redirect(url_for('route_user_page', session['id']))


@app.route('/<user_id>')
@login_required
def route_user_page(id):
    pass


@app.route('/spend')
@login_required
def route_spend_money():
    pass


@app.route('/incomes')
@login_required
def route_incomes():
    pass


@app.route('/all-expenses')
@login_required
def route_all_expenses():
    pass



if __name__ == '__main__':
    app.secret_key = 'TrainsAreAwesome'
    app.run(
        host='0.0.0.0',
        port=5000,
        debug='True'
    )