#!/usr/bin/env python3

"""
contactos.py: el proceso trabaja con un archivo contactos que se extrae
de una base de datos y se depositaba en determinada ruta, cada contacto
que hacia el agente se registraba con toda la info del cliente y la hora de
contacto, el problema era que segun el horario de verano e invierno, el
archivo tenia 5 o 6 horas de mas, las cuales debian ajustarse.
"""

import csv
import shutil
from datetime import datetime, timedelta

hoy = datetime.today().strftime("%Y/%m/%d")
f_out = 'TEL_CONTACTOS_KNT_MTY_' + hoy.replace('/', '') + '.txt'

with open('CONTACTOS.csv', 'r', encoding='utf-8-sig') as fcsv,\
     open(f_out, 'w', newline='') as salida:
    lec = csv.reader(fcsv)
    escritor = csv.writer(salida)

    for l in lec:
        fecha_interna = datetime.strptime(
            "2016-06-15" + " " + l[6], "%Y-%m-%d %H:%M:%S")
        # hora = timedelta(hours=5)# horario de verano
        hora = timedelta(hours=6)  # horario de invierno
        fecha_actualizada=datetime.strftime(
            fecha_interna - hora, "%Y-%m-%d %H:%M:%S")
        cliente = '{:>012}'.format(l[0])
        cd = '{:>02}'.format(l[2])
        data = cliente, l[1][0:10], cd, hoy, l[5], fecha_actualizada[-8:], l[4]
        escritor.writerow(data)

shutil.copy("CONTACTOS.csv", "CONTACTOS_" + hoy.replace('/', '') + ".csv")
