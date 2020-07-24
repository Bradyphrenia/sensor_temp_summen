import os
import re
from koenigin import *


def main():
    pfad = '/Users/steffen/Desktop/sensor/'
    schreiben = {}
    dateiliste = os.listdir(pfad)
    for datei in dateiliste:
        if '.csv' in datei:
            lesen = open(pfad + datei, 'r')
            for zeile in lesen:
                segment = zeile.split(';')
                if segment[0][0:1] == '2' and len(segment[11]) != 0:
                    segment[0] = re.sub("/", "-", segment[0])
                    segment[0] = segment[0][0:10]
                    if schreiben.get(segment[0]) is None:
                        schreiben[segment[0]] = float(segment[11])
                    elif schreiben.get(segment[0]) <= float(segment[11]):
                        schreiben[segment[0]] = float(segment[11])

    bt = brutnest()
    bt.setzeBienen(5000)
    ws = weisel()
    for key in sorted(schreiben):
        bt.berechne(key, schreiben.get(key))
        ws.temperatur = schreiben.get(key)
        print(key, schreiben.get(key), ws.eilegerate(schreiben.get(key)), bt.eier, bt.bienen, bt.relation,
              round((bt.bienen - bt.toteBiene) / bt.bienen, 2))


if __name__ == "__main__":
    main()
