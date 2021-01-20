from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension 

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret_code_here"

debug = DebugToolbarExtension(app)

@app.route('/howdy')
def howdy():
    """Return hello file at index"""
    return render_template("hello.html")

