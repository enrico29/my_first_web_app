
from flask import Flask,render_template
from json import *
from time import *

app =  Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/stanza/<parametro>')
def stanza(parametro):
    stanze = []
    data = load(open('database/index.json', 'r'))
    for i in data:
        if(i["stanza"] == int(parametro)):
            stanze.append(i)
    
    stanze = stanze[ (len(stanze) - 4) : ]
    return render_template('stanza.html', dati = stanze , REFRESH = 5)
