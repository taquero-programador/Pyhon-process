#!/usr/bin/env python3

"""
check_xlsx.py: compara las nuevas cuentas especiales con las del dia
anterior, esto para validar que cumplan con ciertos criterios y poder
cargar la informacion a la db, de lo contrario no se iran a los
servicios correspondientes.

si la cuenta especial esta en el dia anterior me devuelve:
cuenta_especial_nueva, mora, edo, sis, loc, corte, capital.
en la hoja de excel se puede ver y filtrar, en caso de existir
una anomalia muy grande se reporta junto con las cuentas especiales
que no cumplieron los criterios.
"""

import csv
import xlsxwriter

lista_sim = {}
mora_sim =  {}
edo = {}
sis = {}
loc = {}
corte = {}
capital = {}

check_xls = "CHECK_ETKS"

with open('NUEVA_SIM.txt', 'r') as pr:
    lector = csv.reader(pr, delimiter=',')
    for x in lector:
        cuenta, lista = x[1], x[2]
        lista_sim[cuenta] = lista
        mora = x[7]
        mora_sim[cuenta] = mora
        edos = x[5]
        edo[cuenta] = edos
        sistema = x[0]
        sis[cuenta] = sistema
        locacion = x[3]
        loc[cuenta] = locacion
        corte_sim = x[20]
        corte[cuenta] = corte_sim
        cap_s = x[21]
        capital[cuenta] = cap_s


header= ['CUENTA', 'ETK', 'LISTA', 'MV', 'EDO', 'SIS', 'LOC', 'CORTE', 'CAPITAL']
header2 = ['CUENTA', 'ETK', 'ETKDUPLICADA']
workbook = xlsxwriter.Workbook(check_xls + '.xlsx')
worksheet = workbook.add_worksheet("CHECK_ETIQUETAS")
worksheet.autofilter('A1:I1')
worksheet1 = workbook.add_worksheet("DUBLICADOS")
worksheet1.autofilter('A1:C1')
header_format = workbook.add_format({"bold": True, "bg_color": "#4f81bd", "font_color": "#ffffff", "font_size": 12, "border": True, "border_color": "#ffffff", "align": "center"})
content_format= workbook.add_format({"border": True, "border_color": "#000000"})
fila, col = 0, 0

for x in header:
    worksheet.write(fila, col, x, header_format)
    col += 1

fila, col = 1, 0

with open('AUTODLR_UNION.txt', 'r') as ent:
    lec = csv.reader(ent, delimiter=',')
    for c in lec:
      listas = lista_sim.get(c[0], '#N/A') 
      mora = mora_sim.get(c[0], '#N/A')
      edo_s = edo.get(c[0], '#N/A')
      sis_s = sis.get(c[0], '#N/A')
      loc_s = loc.get(c[0], '#N/A')
      cte_s = corte.get(c[0], '#N/A')
      cp_s = capital.get(c[0], "#N/A")
      data = c + [listas] + [mora] + [edo_s] + [sis_s] + [loc_s] + [cte_s] + [cp_s] 
      worksheet.write(fila, col, c[0])
      worksheet.write(fila, col + 1, c[1])
      worksheet.write(fila, col + 2, listas)
      worksheet.write(fila, col + 3, mora)
      worksheet.write(fila, col + 4, edo_s)
      worksheet.write(fila, col + 5, sis_s)
      worksheet.write(fila, col + 6, loc_s)
      worksheet.write(fila, col + 7, cte_s)
      worksheet.write(fila, col + 8, cp_s)
      fila += 1

worksheet.set_column("A:A", 20)
worksheet.set_column("B:B", 10)
worksheet.set_column("C:C", 30)
worksheet.set_column("D:D", 10)
worksheet.set_column("E:E", 10)
worksheet.set_column("F:F", 10)
worksheet.set_column("G:G", 10)
worksheet.set_column("H:H", 10)
worksheet.set_column("I:I", 16)

workbook.close()
