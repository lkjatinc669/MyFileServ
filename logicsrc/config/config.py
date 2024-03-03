from flask import Blueprint, render_template

configPrint = Blueprint('config', __name__, static_folder="static", template_folder="/websrc")

@configPrint.route('/start')
def welcome():
    return render_template("config/base.html", title="Config Start", form="start")

@configPrint.route('/config-01')
def config1():
    return render_template("config/base.html", title="Creating SuperUser", form="config1")

@configPrint.route('/config-02')
def config2():
    return render_template("config/base.html", title="Creating Services", form="config2")

@configPrint.route("/complete")
def complete():
    return render_template("config/base.html", title="Final", form="complete", code=["123456", "123456", "123456", "123456", "123456", "123456", "123456", "123456", "123456", "123456", "123456", "123456"])