from flask import Flask, redirect, render_template, url_for, request, session
import data_manager
import validation

app = Flask(__name__)


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
        session['id'] = data_manager.get_user_id_by_email(request.form['e_mail'])

        validation.is_user_pass(request.form['password'], session['id'])
    return redirect(url_for('route_user_page', session['id']))

@app.route('/<user_id>')
def route_user_page(id):
    pass


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