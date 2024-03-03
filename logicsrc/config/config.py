from flask import Blueprint, render_template, request, redirect, url_for

configPrint = Blueprint('config', __name__, static_folder="static", template_folder="/websrc")

@configPrint.route('/')
def a():
    return redirect("/config/start")

@configPrint.route('/start')
def welcome():
    return render_template("config/base.html", title="Config Start", form="start")

@configPrint.route('/config-01', methods=["POST", "GET"])
def config1():
    if request.method== "POST" and request.form.get("uniqpass2next") == "Start" :
        frstname = request.form.get("firstname")
        lastname = request.form.get("lastname")
        username = request.form.get("username")
        password = request.form.get("password")
        return render_template("config/base.html", title="Creating SuperUser", form="config1")
    if request.method == "GET":
        return redirect("/config/start")

@configPrint.route('/config-02', methods=["POST", "GET"])
def config2():
    if request.method == "POST" and request.form.get("conf1") == "Next":
        return render_template("config/base.html", title="Creating Services", form="config2")
    if request.method == "GET":
        return redirect("/config/start")

@configPrint.route("/complete", methods=["POST", "GET"])
def complete():
    if request.method== "POST" and request.form.get("conf1") == "Next":
        return render_template("config/base.html", title="Final", form="complete", code=["123456", "123456", "123456", "123456", "123456", "123456", "123456", "123456", "123456", "123456", "123456", "123456"])
    if request.method == "GET":
        return redirect("/config/start")