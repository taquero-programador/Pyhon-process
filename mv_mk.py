#!/usr/bin/env python3

"""
mv_mk.py: este proceso en un inicio estaba hecho en un batch para win7,
pero despues de que migraron los equipos a win10 e hicieron "ajustes"
perdimos muchos permisos, incluso algo tan simple como un batch dejo
de funcionar, si se ejecutaban pero no surtian efecto.

lo que hace este proceso es crear una copia de los archivos en rutas
especificas, se añadio una tarea programada que a cierta hora por la
madrugada copiara los archivos.
"""

import shutil
import os
import time
from datetime import datetime
from datetime import timedelta

fecha=datetime.today().strftime('%Y%m%d')
dm=timedelta(days=1)
hoy=datetime.today()
fen=datetime.strftime(hoy - dm, '%Y%m%d')

codificaciones=['Codificaciones_318.csv', 'Codificaciones_327.csv',
                  'Codificaciones_325.csv', 'Codificaciones_323.csv']
# activity
activity=r'\\192.168.73.23\Tables\NVO72\BASESOTA\ACTIVITY_NEW'
destino=r'\\192.168.130.81\Backup\ACTIVITY_NEW'
act=activity + os.sep + 'ACTIVITY_NEW_{}.txt'.format(fen[4:])
shutil.copy2(act, destino)
print('ACTIVITY Listo!')

# union y detalle de remesa
union_rem=r'\\192.168.73.23\Tables\NVO72\PROCESO_REMESA'
destino2=r'\\192.168.130.81\Backup\REMESA'
shutil.copy2(union_rem + os.sep + 'AUTODLR_UNION.TXT', destino2)
print('UNION Listo!')
shutil.copy2(union_rem + os.sep + 'REMESA_{}.csv'.format(fecha), destino2)
print('DETALLE REM Listo!')

# folios
path_folio=r'\\192.168.73.23\Tables'
destino3=r'\\192.168.130.81\Backup\REMESA\DESARROLLO\HERRAMIENTAS'
shutil.copy2(path_folio + os.sep + 'FOLIO.txt', destino3)
print('FOLIOS Listo!')

# codificaciones
path_cod=r'\\192.168.73.23\Tables\NVO72'
destino4=r'\\192.168.130.81\Backup\MIS_BAU\CODIFICACIONES'
for codi in os.listdir(path_cod):
    if codi in codificaciones:
        shutil.copy2(path_cod + os.sep + codi, destino4)
        print('{} Listo!'.format(codi))

time.sleep(3)