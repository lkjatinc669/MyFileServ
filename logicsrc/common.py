from flask import Blueprint, session, redirect, url_for, render_template

commonPrint = Blueprint('common', __name__, static_folder="static", template_folder="websrc")

@commonPrint.route("/")
def index():
    if 'usrsecname' in session:
        return redirect(url_for("/user"))
    if 'admsecname' in session:
        return redirect(url_for("/admin"))
    return render_template( "index.html")