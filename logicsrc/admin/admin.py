from flask import Blueprint, render_template

adminPrint = Blueprint('admin', __name__, static_folder="static", template_folder="websrc/admin")

@adminPrint.route('/')
def welcome():
    return render_template("index.html")

@adminPrint.route('/config-01')
def config1():
    return 'Config 1'

@adminPrint.route('/config-02')
def config2():
    return 'Config 2'

@adminPrint.route("/complete")
def complete():
    return 'Complete'

@adminPrint.route("/dashboard")
def dashboard():
    return 'Dashboard'