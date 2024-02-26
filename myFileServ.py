from flask import Flask, session, redirect, url_for, request, render_template

app = Flask(__name__, static_folder="static", template_folder="websrc")

@app.route('/')
def index():
    if 'username' in session:
        return f'Logged in as {session["username"]}<br><a href="/logout">Logout</a>'
    return 'You are not logged in<br><a href="/login">Login</a>'

@app.route("/admin/config")
def config():
    return render_template('admin/config.html')

app.run(
    host="0.0.0.0",
    port=3440,
    debug=True
)