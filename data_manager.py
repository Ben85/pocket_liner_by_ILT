import connection

@connection.connection_handler
def register_user():
    pass

@connection.connection_handler
def get_users_last_month_balance(cursor, user_id):
    '''Get the last 30 days' spendings and earnings.'''
    pass


@connection.connection_handler
def get_users_current_status(cursor, user_id):
    '''Shows the overall finantioal position you are in.'''
    pass


@connection.connection_handler
def get_all_expenses_by_user(cursor, user_id):
    pass


@connection.connection_handler
def insert_expense(cursor, user_id):
    """ dont forget the notes"""
    pass


@connection.connection_handler
def get_user_data_by_id(cursor, user_id):
    pass


@connection.connection_handler
def insert_income(cursor, user_id):
    pass


