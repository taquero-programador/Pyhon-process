#!/usr/bin/env python3

"""
mixed.py: Toma un archivo llamado AUTODLR.S111.CC2.fecha-actual.txt,
el archivo se encuentra separado por tabulaciones.

rmixed almacenara una lista con las cuentas de x[6:22] cuando se encuentren
en 520501.

simulacion almacenara la columna 1 (cuentas) cuando la columna 3
se encuentre en 520501.

cmix saca las cuentas que no sea encuentren en simulacion.

al final itera sobre cmix para escribir una columnas con el resultado y
otra con la etiqueta 'MIXED', todo en un archivo resultado_nregs.csv.
"""

import csv
import glob

def get_csv(file_name):
	return list(csv.reader(open(file_name, 'r')))

simulacion = [s[1] for s in get_csv('NUEVA_SIM.txt') if s[3] in '520501']

cmix = [x[6:22] for x in sorted(glob.glob(get_csv('AUTODLR.S111.CC2.*[0-9].txt')))
			if x[0:6] in '520501' and x[6:22] not in simulacion]

with open('resultado_' + str(len(cmix)) + '.csv', 'w', newline='') as file_result:
	escritor = csv.writer(file_result)
	for regs in cmix:
		data = regs, 'MIXED'
		escritor.writerow(data)
