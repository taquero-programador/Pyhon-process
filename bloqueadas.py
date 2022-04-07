#!/usr/bin/env python3

"""
v0.2
bloqueadas.py: Toma 3 archivos ubicados en path, en cada registrso existe un
telefono y un codigo, si el codigo es 'BLOQ' lo va a tomar y a escribir en un
archivo de salida.

para evitar almacenar los resultado en una lista para luego iterar y escribir en
el archivo de salida, creo un archivo de salida sin el metodo with, el cual lo
mantiene activo hasta que termine el bucle, salga del metodo with y lo mande llamar
con salida.close() para cerrar el archivo.
"""

import csv
import os
from datetime import datetime

fecha = datetime.today().strftime('%d/%m/%Y')
header = ['FECHA_EXCLUSION', 'SIS', 'CLIENTE', 'TEL', 'CODIGO']

def bloq(*args):
    "procesa archivos en path y genera un RESULTADO_BLOQ"

    salida = open('RESULTADO_BLOQ.txt', 'w')
    salida.write((',').join(header) + '\n')

    path = r'NUEVOS'
    for f in args:
        file = f

        with open(os.path.join(path, file), 'r', encoding='utf-8-sig') as bl:
            lec=csv.reader(bl)

            for i in lec:
                if i[2] == 'BLOQ':
                    if f == 'BLOQUEOS_111.txt':
                        sis = 'S111'
                    elif f == 'BLOQUEOS_821.txt':
                        sis = 'R821'
                    elif f == 'BLOQUEOS_404.txt':
                        sis = 'S404'
                    data = fecha, sis, i[0], str(i[1]).strip(), i[2]
                    salida.write((',').join(data) + '\n')

    salida.close()

bloq('BLOQUEOS_821.txt', 'BLOQUEOS_404.txt', 'BLOQUEOS_111.txt')

