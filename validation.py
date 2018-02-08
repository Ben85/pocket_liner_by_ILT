import encryption
import data_manager


def is_user_pass(user_password, user_id):
    user_data = data_manager.get_user_data_by_id(user_id)
    if encryption.verify_password(user_password, user_data['pass_hash']):
        return True
    else:
        return False