from json import *
from datetime import *
from random import *
from time import *
#
dati = []
while(True):
    file = open('./database/index.json', 'w')
    time_stamp = datetime.now()
    stanza = randint(1,4)
    temp = randrange(0,40)

    dato = {
        "timeStamp": str(time_stamp),
        "stanza": stanza,
        "temp": temp
    }
    dati.append(dato)
    file.write(dumps(dati , indent=2))
    file.close()
    sleep(5)