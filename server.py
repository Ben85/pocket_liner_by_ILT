from flask import Flask, redirect, render_template, url_for, request, session
import data_manager

app = Flask(__name__)


@app.route('/')
def route_index():
    return render_template('index.html')


@app.route('/registration')
def route_register():
    # redirect to '/'. if successfull or not
    pass


@app.route('/login')
def route_login():
    # redirects to user_page
    pass


@app.route('/<user_id>')
def route_user_page(id):
    pass


@app.route('/spend')
def route_spend_money():
    pass


@app.route('/incomes')
def route_incomes():
    pass


@app.route('/<user_id>/all-expenses')
def route_all_expenses(user_id):
    expenses = data_manager.get_all_expenses_by_user(user_id)
    return render_template('expenses.html', expenses=expenses)



if __name__ == '__main__':
    app.secret_key = 'TrainsAreAwesome'
    app.run(
        host='0.0.0.0',
        port= 5000,
        debug='True'
    )