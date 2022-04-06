#!/usr/bin/env python3

"""
bloqueadas.py:El proceso toma 3 archivos ubicados en path, en cada registro
existe un telefonon y un codigo, si ese codigo es 'BLOQ' lo va almacenar en
data_block que ademas le añade la etiqueta sis segun el tipo de archivo.
una vez completado, itera sobre data_block y genera un archivo de salida.

Almaceno los resultados en una lista, pues si bien el metodo csv.writer es
muy bueno, un detalle es que al finalizar una codicion se cierra en automatico
si permitir escribir los siguientes registros.
"""

import csv
import os
from datetime import datetime

fecha = datetime.today().strftime('%d/%m/%Y')
header = ['FECHA_EXCLUSION', 'SIS', 'CLIENTE', 'TEL', 'CODIGO']

def bloq(*args):

    data_block = []

    path = r'NUEVOS'
    for f in args:
        file = f

        with open(path + os.sep + file, 'r', encoding='utf-8-sig') as bl,\
            open('RESULTADO_BLOQ.txt', 'w', newline='') as salida:
            lec=csv.reader(bl)
            esc=csv.writer(salida)
            esc.writerow(header)

            for i in lec:
                if i[2] == 'BLOQ':
                    if f == 'BLOQUEOS_111.txt':
                        sis = 'S111'
                    elif f == 'BLOQUEOS_821.txt':
                        sis = 'R821'
                    elif f == 'BLOQUEOS_404.txt':
                        sis = 'S404'
                    data = fecha, sis, i[0], str(i[1]).strip(), i[2]
                    data_block.append(data)

            for db in data_block:
                esc.writerow(db)

bloq('BLOQUEOS_111.txt', 'BLOQUEOS_821.txt', 'BLOQUEOS_404.txt')
