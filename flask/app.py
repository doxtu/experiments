from flask import Flask, request, abort, session
from flask_cors import CORS
from markupsafe import escape
import os

app = Flask(__name__)
app.secret_key = os.urandom(16)
CORS(app)

@app.route('/')
def hello_world():
    ret = ''
    if 'username' in session:
        ret = ret + escape(session['username']) 
    else:
        ret = ret + 'unknown'
    return f'Hello, {ret}\n\n'

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        try:
            session['username'] = request.args.get('user')
        except:
            return 'Failfish \n\n'
    return 'good job :)\n\n'

@app.route('/api')
def api_handler():
    ret = ''
    ret = ret + f'Welcome to the api!!!\n\n'
    for arg in request.args:
        ret = ret + f'You sent the following args {arg} - {request.args.get(arg)}\n'

    ret = ret + '\n'
    return ret

@app.route('/api/<premise>')
def premise_handler(premise):
    return f'Premise = {escape(premise)} \n\n'

@app.route('/api/<premise>/dump', methods=['GET','POST'])
def get_premise_info(premise):
    if request.method == 'POST':
        return 'DONE\n\n'
    else:
        clown = {'hi': 'hola', 'bye': 'adios'}
        return clown

@app.route('/api/intentional-abort')
def intentional_abort():
    abort(401)

@app.errorhandler(401)
def unauthorized_handler(error):
    return 'LOGIN, CLOWN\n\n'
