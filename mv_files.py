#!/usr/bin/env python3

"""
mv_files.py: mueve los archivos del directorio actual.

El programa le pregunta al usuario que mes deses respaldar, pues en el
directorio actual se encuentras archivos csv con el mismo nombre pero
con el mes de procesamiento diferente, comprueba que correspondan a la
opcion ingresada y que sean solo archivos .csv, crea una carpera con el
mes a respaldar y ahi coloca los archivos.
RESULTADOS/MES/MESFILES.CSV
"""

import os
import shutil
import time
from DATA.fechas_files import meses, yr


def respaldo():

    directorio_files = 'RESULTADOS'
    [print('{:>2} > {:}'.format(*np)) for np in meses]
    bk_files = int(input('\nMES A RESPALDAR?: '))
    for mon in meses:
        if bk_files == mon[0]:
            mon_to_folder = mon[1] + '_' + yr
            mon_files = mon[1]
            if os.path.exists(directorio_files + os.sep + mon_to_folder):
                print('el directorio ya existe.')

                os.chdir(directorio_files)
                for mv in os.listdir():
                    fname, ext = os.path.splitext(mv)
                    if fname.endswith(mon_files):
                        if ext == '.csv':
                            shutil.move(mv, mon_to_folder)
                print('archivos en {} listos'.format(mon_to_folder))
                time.sleep(3)
            else:
                os.mkdir(directorio_files + os.sep + mon_to_folder)
                print('dir listo!!!')
                time.sleep(3)

                os.chdir(directorio_files)
                for mv in os.listdir():
                    fname, ext = os.path.splitext(mv)
                    if fname.endswith(mon_files):
                        if ext == '.csv':
                            shutil.move(mv, mon_to_folder)
                print('archivos en {} listos'.format(mon_to_folder))
                time.sleep(2)

        elif bk_files not in list(range(1, 13)):
            print('--comando no valido')
            time.sleep(2)
            os.system('cls')
            return respaldo()

respaldo()