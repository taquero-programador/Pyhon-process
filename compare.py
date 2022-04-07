#!/usr/bin/env python3

"""
compare.py: este proceso compara 2 archivos con informacion, uno
porveniente de sql y otro procesado por py, de ahi obtiene el
nombre de servicio y el mumero de registros, con chain añade el
nunero de registros, los resta y les aplica una etiqueta por resultado.

el proceso se ejecutaba en un equipo con python 3.4, por eso el uso
de format() y list(sorted()).
"""

import csv
import glob
from collections import Counter, defaultdict
from itertools import chain
from datetime import datetime

fecha = datetime.today().strftime("%Y/%m/%d")
yr, mes, dia = fecha.split('/')
r = int(dia) - 1
d_ayer = mes + str(r)

file_local = r'RESULTADOS\RPT_DIALER_PERFORMANCE_' + d_ayer + '.csv'
infile = [fn for fn in sorted(glob.glob(r'\\192.168.73.23\Tables\NVO72\ICARO_NOC\RPT_DIALER_PERFORMANCE_*[0-9].csv'))]

def get_csv(file_name):
        "retorna una lista del archivo pasado como argumento"

        return list(csv.reader(open(file_name, 'r')))

icaro_org = get_csv(infile[0])
icaro_sal = get_csv(file_local)

uno = Counter(n[0] for n in icaro_org)
dos =  Counter(i[0] for i in icaro_sal)

serv_uno = Counter(n[1] for n in icaro_org)
serv_dos = Counter(i[1] for i in icaro_sal)

union = defaultdict(list)

def crea_chain(*args):
        for k, v in chain(args[0].items(), args[1].items()):
                union[k].append(v)

        with open(r'check.txt', 'w', newline='') as sl:
                escritor=csv.writer(sl, delimiter='\t')
                escritor.writerow(
                    ['CONT', 'FECHAS', 'ICARO', 'RESULTADO', 'DIF', 'STATUS'])
                reg = 0
                for fechas, registros in list(sorted(union.items())):
                        reg += 1
                        op = registros[0] - registros[1]
                        if op == 0:
                                men = 'OK'
                        else:
                                men = 'Error'

                        data = '{:02} {:>15} {:>5} {:>10} {:>10} {:>10}'.format(
                            reg, fechas, registros[0], registros[1], op, men)
                        escritor.writerow([data])
                escritor.writerow(['-'*60])

crea_chain(uno, dos)
crea_chain(serv_uno, serv_dos)
