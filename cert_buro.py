#!/usr/bin/env python3

"""
cert_buro.py: crea un directorio NUEVOS en caso de no existir.

el proceso de alimenta de dos archivos, RESULTADOS_CERT_MTY_FECHA.txt
el cual contiene informacion del dia extraida de Oracle.
quitat.txt es una base fija que se utiliza como condicion para omitir
los resultados en el archico cert_file, pero el cert_buro si los almacena.

"""

import csv
import glob
import os

try:
    os.mkdir('NUEVOS')
except (FileExistsError) as direx:
    print(direx)

for file in sorted(glob.glob('RESULTADO_CERT_MTY_*[0-9].TXT')):
    name_file = file

with open('quitar.txt', 'r') as quita:
    lec = csv.reader(quita, delimiter='|')
    for l in lec:
        quitar = [l[0] for l in lec]

cert_file = open(r'NUEVOS' + os.sep + name_file, 'w')
cert_buro = open(r'NUEVOS' + os.sep + name_file[:-4] + '_BURO' + '.TXT', 'w')

with open(name_file, 'r') as cert,\
	open(r'NUEVOS' + os.sep + name_file, 'w', newline='') as cert_file,\
	open(r'NUEVOS' + os.sep + name_file[:-4] + '_BURO.TXT', 'w', newline='') as cert_buro:
    lec = csv.reader(cert, delimiter='|')
	esc1 = csv.writer(cert_file)
	esc2 = csv.writer(cert_buro)    	
    for x in lec:
        if x[0] in quitar:
            esc1.writerow(x)
            continue
        esc2.writerow(x)

print('done!')
