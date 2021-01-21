from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from random import randint, choice, sample

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret_code_here"

app.debug = True 
toolbar = DebugToolbarExtension(app)

@app.route('/form')
def show_form():
    return render_template('form.html')

#---------------------------------------------- GREET2 COMPLIMENTS ---------------------------------------------------

COMPLIMENTS = ["nearly cool","borderline clever","tenacious","awesome","not-nearly-as-dumb as people say", "smelly... but in a good(ish) way", "audacious","well-mannered for your level of class"]

@app.route('/greet')
def get_greeting():
    """receive form data from show_form"""
    nice_thing = choice(COMPLIMENTS)
    username=request.args["username"]
    return render_template('greet.html',username=username, compliment=nice_thing)

@app.route('/form-2')
def show_form_2():
    return render_template("form_2.html")

@app.route('/greet2')
def get_greeting_2():
    """to select three random compliments if user wants them"""
    idx=0
    username=request.args["username"]
    wants_compliments=request.args.get("wants_compliments")
    nice_things = sample(COMPLIMENTS, 3) #from random
    return render_template('greet_2.html', username=username, wants=wants_compliments, compliments=nice_things, idx=idx)

#----------------------------------------------------------------------------------------------------------------------


"""
^ browser requests /form -> server renders template form.html to browser
browser/form requests /greet route -> goes to @app.route('/greet') at server
server get_greeting processes form ->renders template 'greet.html' to browser
"""

@app.route('/howdy')
def howdy():
    '''Return hello file at index'''
    return render_template("hello.html")

@app.route('/lucky')
def lucky_number():
    """returns lucky numbers through jinja and render_template"""
    num = randint(1,10)
    return render_template('lucky.html', lucky_num=num, msg="You are so lucky!")

@app.route('/spell/<word>')
def spell_word(word):
    """Turns words into individual H1 letters"""
    return render_template("spell_word.html",word=word)


