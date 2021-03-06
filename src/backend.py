import requests

#base_url = "http://norbye.com/-other-/liblog/api/"
base_url = "http://tung.deichman.no/api/"

actions = {
    'create_user': 'create_user.php',
    'get_user_info': 'get_user_info.php',
    'update_pin': 'update_pin.php',
    'delete_user': 'delete_user.php',
    'login_user': 'login_user.php',
    'scan_book': 'book_scanned.php',
    'get_book_info': 'get_book_info.php',
    'give_feedback': 'feedback.php',
    'get_lended_books': 'get_lended_books.php',
    'admin_login': 'admin/index.php',
    'admin_get_all_books': 'admin/index.php?index=books',
    'admin_get_lent_books': 'admin/index.php?index=global/history',
    'admin_get_all_users': 'admin/index.php?index=users',


}


def request(action, data):
    return requests.post(base_url + actions[action], data=data)
