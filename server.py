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
    user_data['password_reg'] = encryption.hash_password('password_reg')
    data_manager.register_user(user_data)
    return redirect(url_for('route_index'))


@app.route('/login', methods=['POST', 'GET'])
def route_login():
    pass


@app.route('/<user_id>')
def route_user_page(id):
    return render_template('user_index.html')


@app.route('/spend')
def route_spend_money():
    pass


@app.route('/incomes')
def route_incomes():
    pass


@app.route('/all-expenses')
def route_all_expenses():
    pass



if __name__ == '__main__':
    app.secret_key = 'TrainsAreAwesome'
    app.run(
        host='0.0.0.0',
        port=5000,
        debug='True'
    )