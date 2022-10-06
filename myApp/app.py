from flask import Flask, render_template ,request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/stanza/')
def stanza():
    data = []
    dati_stanza = []
    query = request.args.get("numero")
    nomeFile = "stanza" + query

    file = open(nomeFile + '.csv', 'r')
    file = list(file)
    file.reverse()

    for i in range(4):
        data.append(file[i])

    for i in data:
        riga = i.split(';')
        riga = {
            "TEMPO": riga[0],
            "STANZA": riga[1],
            "TEMP": riga[2],
        }
        dati_stanza.append(riga)
        
    return render_template('stanza.html', dati = dati_stanza , REFRESH= 5)