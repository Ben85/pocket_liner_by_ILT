import encryption
import data_manager


def is_user_pass(user_password, e_mail):
    user_data = data_manager.get_user_data_by_id(data_manager.get_user_id_by_email(e_mail))
    return True if encryption.verify_password(user_password, user_data['pass_hash']) else False