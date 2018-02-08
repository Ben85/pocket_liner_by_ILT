from flask import Flask, redirect, render_template, url_for, request, session
import data_manager
import encryption

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def route_index():
    if request.method == 'POST':
        session.clear()

        if request.form['password'] == 'password':
            session['user'] = request.form['username']
            return redirect(url_for('route_user_page'))

    return render_template('index.html')



@app.route('/registration', methods=['POST', 'GET'])
def route_register():
    user_data = request.form.to_dict()
    is_email_used = data_manager.email_used(request.form["e_mail_reg"])
    if len(is_email_used) > 0:
        return render_template('index.html', is_email_used = True)
    user_data['password_reg'] = encryption.hash_password('password_reg')
    data_manager.register_user(user_data)
    return redirect(url_for('route_index'))


@app.route('/login', methods=['POST', 'GET'])
def route_login():
    pass


@app.route('/<user_id>')
def route_user_page(user_id):
    return render_template('user_index.html')


@app.route('/spend')
def route_spend_money():
    spend_info = request.form.to_dict()
    data_manager.insert_expense(spend_info)
    return redirect(url_for('route_user_page'))

@app.route('/incomes')
def route_incomes():
    income_info = request.form.to_dict()
    data_manager.insert_income(income_info)
    return redirect(url_for('route_user_page'))

@app.route('/all-expenses')
def route_all_expenses():
    return render_template('income_expense.html')



if __name__ == '__main__':
    app.secret_key = 'TrainsAreAwesome'
    app.run(
        host='0.0.0.0',
        port=5000,
        debug='True'
    )