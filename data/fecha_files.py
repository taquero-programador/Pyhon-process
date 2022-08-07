#!/usr/bin/env python3

import datetime

fecha = datetime.date.today()

yr, mes, dia = str(fecha).split('-')

meses = list(enumerate(['ENERO', 'FEBRERO', 'MARZO', 'ABRIL', 'MAYO', 'JUNIO',
         'JULIO', 'AGOSTO', 'SEPTIEMBRE', 'OCTUBRE', 'NOVIEMBRE', 'DICIEMBRE'], 1))


def index():
    for index in meses:
        if str(index[0]) == mes:
            mff = index[1]
                return mff
