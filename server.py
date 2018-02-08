from flask import Flask, flash, redirect, render_template, url_for, request, session
import data_manager
import validation
from functools import wraps
import encryption

app = Flask(__name__)


def login_required(function):
    @wraps(function)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash("For this you need to log in")
            return redirect(url_for('login', next=request.url))
        return function(*args, **kwargs)
    return decorated_function


@app.route('/logout')
def route_logout():
    session.clear()

    return redirect('/')


@app.route('/registration', methods=['POST', 'GET'])
def route_register():
    user_data = request.form.to_dict()
    is_email_used = data_manager.email_used(request.form["e_mail_reg"])
    if len(is_email_used) > 0:
        return render_template('login.html', is_email_used = True)
    user_data['password_reg'] = encryption.hash_password(request.form["password_reg"])
    data_manager.register_user(user_data)
    return redirect(url_for('login'))


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if validation.is_user_pass(request.form['password'], request.form['e_mail']):
            user_data = data_manager.get_user_data_by_e_mail(request.form['e_mail'])
            session['user_id'] = user_data['id']
            session['user_name'] = user_data['name']
            return redirect(url_for('home'))
    return render_template('login.html')


@app.route('/', methods=['POST', 'GET'])
@login_required
def home():
    return render_template('user_index.html', user_id=session['user_id'], user_name=session['user_name'])


@app.route('/spend', methods=['POST', 'GET'])
@login_required
def route_spend_money():
    spend_info = request.form.to_dict()
    spend_info['user_id'] = session['user_id']
    spend_info['amount'] = abs(int(spend_info['amount']))
    data_manager.insert_expense(spend_info)
    return redirect(url_for('home'))

@app.route('/incomes', methods=['POST', 'GET'])
@login_required
def route_incomes():
    income_info = request.form.to_dict()
    income_info['user_id'] = session['user_id']
    income_info['amount'] = abs(int(income_info['amount']))
    data_manager.insert_income(income_info)
    return redirect(url_for('home'))


@app.route('/<int:user_id>/all-expenses')
@login_required
def route_all_expenses(user_id):
    expenses = data_manager.get_all_expenses_by_user(user_id)
    return render_template('expenses.html', expenses=expenses)


@app.route('/inc_exp')
@login_required
def route_inc_exp():
    return render_template('income_expense.html')



if __name__ == '__main__':
    app.secret_key = 'TrainsAreAwesome'
    app.run(
        host='0.0.0.0',
        port=5000,
        debug='True'
    )