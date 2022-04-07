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

path = 'NUEVOS'
try:
    os.mkdir(path)
except (FileExistsError) as direx:
    pass

def get_csv(file_name):
    return list(csv.reader(open(file_name, 'r')))

nf = [n for n in sorted(glob.glob('RESULTADO_CERT_MTY_*[0-9].TXT'))]
name_file = get_csv(nf[0])
quitar = get_csv('quitar.txt')

with open(os.path.join(path, nf[0]), 'w', newline='') as cert_file,\
	open(os.path.join(path, nf[0][:-4] + '_BURO.TXT'), 'w', newline='') as cert_buro:
    esc1 = csv.writer(cert_file)
    esc2 = csv.writer(cert_buro)
    for x in name_file:
        if x[0] in quitar:
            esc1.writerow(x)
            continue
        esc2.writerow(x)

print('done!')
