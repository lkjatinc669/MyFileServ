from flask import Flask, session, redirect, url_for, request, render_template
from logicsrc.config.config import configPrint
from logicsrc.admin.admin import adminPrint
from logicsrc.user.user import userPrint
from logicsrc.common import commonPrint

app = Flask(__name__, static_folder="static", template_folder="websrc")

app.register_blueprint(configPrint, url_prefix='/config')
app.register_blueprint(adminPrint, url_prefix='/admin')
app.register_blueprint(userPrint, url_prefix='/user')
app.register_blueprint(commonPrint)

@app.errorhandler(404) 
def not_found(e): 
    return render_template("notfound.html") 

app.run(
    host="0.0.0.0",
    port=3440
)

# from logicsrc.handlers.FFoldersHandler import FFoldersHandler

# print(FFoldersHandler("./").getFilesFolders())