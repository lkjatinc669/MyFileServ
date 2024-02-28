from flask import Blueprint

userPrint = Blueprint('user', __name__, static_folder="static", template_folder="websrc/user")

@userPrint.route('/login')
def login():
    return 'Login Page'

@userPrint.route('/register')
def register():
    return 'Register Page'