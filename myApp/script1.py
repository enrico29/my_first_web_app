import datetime as date
import random
from time import sleep


def addOnStanza(n_stanza):
    file = open('stanza'+ str(n_stanza) + '.csv', 'a')
    data = date.datetime.now()
    temp = random.randrange(0,40)
    file.write(
        str(data) + ";" +
        str(n_stanza) + ";" +
        str(temp) + "\n"
    )
    file.close()

while(True):
    for i in range(4):
        addOnStanza(i)
    sleep(5)



