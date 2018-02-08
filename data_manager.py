import connection
import encryption

@connection.connection_handler
def register_user(cursor, new_user_data):
    cursor.execute("""INSERT INTO users(
                      name, e_mail, pass_hash)
                      VALUES (%(name)s, %(e_mail)s, %(pass_hash)s);
                      """, {'name' : new_user_data['username_reg'], 'e_mail' : new_user_data['e_mail_reg'], 'pass_hash' : new_user_data['password_reg']})


@connection.connection_handler
def get_user_id_by_email(cursor, e_mail):
    cursor.execute("""
                      SELECT id FROM users
                      WHERE e_mail = %(e_mail)s;
    """, {'e_mail': e_mail})
    id_dic = cursor.fetchone()
    return id_dic['id']


@connection.connection_handler
def email_used(cursor, e_mail_reg):
    cursor.execute(
        """
        SELECT e_mail FROM users
        WHERE e_mail = %(e_mail_reg)s; 
        """,
        {
            'e_mail_reg' : e_mail_reg
        }
    )
    used_email = cursor.fetchall()
    return used_email


@connection.connection_handler
def get_users_last_month_balance(cursor, user_id):
    '''Get the last 30 days' spendings and earnings.'''
    pass


@connection.connection_handler
def get_users_current_balance(cursor, user_id):
    '''Shows the overall finantioal position you are in.'''

    cursor.execute(
        """
        SELECT SUM(amount) FROM transactions
        JOIN users ON transactions.user_id = users.id
        WHERE users.id = %(user_id)s;
        """,
        {
            "user_id": user_id
        }
    )
    balance = cursor.fetchall()

    return balance


@connection.connection_handler
def get_all_expenses_by_user(cursor, user_id):
    cursor.execute("""
                             SELECT category, amount FROM transactions
                             INNER JOIN categories ON transactions.category_id = categories.id
                             INNER JOIN users ON categories.user_id = users.id
                             WHERE categories.income = False
                             AND users.id = %(user_id)s;
                               """,
                   {"user_id": user_id})
    return cursor.fetchall()


@connection.connection_handler
def insert_expense(cursor, spend_info):
    cursor.execute("""
                    INSERT INTO transactions (category, date, amount, note, user_id) 
                    VALUES (%(category)s, %(date)s, %(amount)s, %(note)s, %(user_id)s);
                    """, spend_info)


@connection.connection_handler
def get_user_data_by_id(cursor, user_id):
    cursor.execute("""
                   SELECT * FROM users
                   WHERE id = %(user_id)s
                    """, {'user_id': user_id})
    return cursor.fetchone()


@connection.connection_handler
def get_user_data_by_e_mail(cursor, e_mail):
    cursor.execute("""
                   SELECT * FROM users
                   WHERE e_mail = %(e_mail)s
                    """, {'e_mail': e_mail})
    return cursor.fetchone()


@connection.connection_handler
def insert_income(cursor, income_info):
    cursor.execute("""
                        INSERT INTO transactions (category, date, amount, user_id) 
                        VALUES (%(category)s, %(date)s, %(amount)s, %(user_id)s);
        """, income_info)


