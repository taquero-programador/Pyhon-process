#!/usr/bin/env python3

"""
order.py: existe un proceso que extrar arriba de 100 csv con gran
cantidad de informacio, el detalle en esto es que despues se solicito
que a ciertos archivos se les deberia eliminar la segunda, tercera y
en algunos casos la ultima fila, pues esas filas no contenian informacion
importante.

los archivos se obtienen de determinadas rutas, se procesan y generan 
nuevos en un destino diferente para no alterar los originales.
"""

import os
import csv
from datetime import datetime, timedelta

fecha = datetime.today().strftime('%Y%m%d')
dm = timedelta(days=1)
hoy = datetime.today()
fen = datetime.strftime(hoy - dm, '%Y%m%d')

armado_alm=['mis_dt', 'datacenter', 'input_file_name', 'contact_record_id', 'Loc_Code_',
            'Estado_Funcional_', 'resp_colltr_id', 'activity_code', 'Cuenta', 'Cliente_', 'MV',
            'Saldo_Actual_', 'Capital_', 'Corte_', 'CP_', 'LISTNAME', 'TRIAD_Esce_',
            'TRIAD_Estr_', 'Producto_generico', 'Coll_ID_', 'available_phones', 'Cve_Ges_1',
            'Sta_Cta', 'Segmento']

aht_hd=['MIS_DT', 'Server_Name', 'service_id', 'dialer_target_name', 'contact_list_id',
        'contact_list_name', 'dialer_name', 'record_number', 'tme_of_contact',
        'response_status', 'id', 'account_number', 'agent_login_name', 'TYPE_CALL',
        'PREVIEW_TIME', 'TALK_TIME', 'WRAP_TIME']

sum_dis=['MIS_DT', 'DAY_', 'MONTH_', 'YEAR_', 'SERVICE', 'LIST', 'PORTFOLIO_NAME',
        'SEGMENT', 'TYPE_SERVICE', 'GROUP_DISPOSITION', 'DISPOSITION_CODE',
        'DISPOSITION_DESCRIPTION', 'RECORDS']

def proc(*args):
    "quita divisor y contador"

    for f in args:
        file = f + fen[4:] + '.csv'

        with open(r'\\10.208.0.4\d$\Icaro\TMP_FILES' + os.sep + file, 'r', encoding='utf-8-sig') as c01,\
            open(r'RESULTADOS' + os.sep + file, 'w', newline='') as out:
            lec = csv.reader(c01)
            header = next(lec)  # encabezado
            div_head = next(lec)  # divisor
            esc = csv.writer(out)
            if f == 'RPT_SUMM_DISP_':
                esc.writerow(sum_dis)
            else:
                esc.writerow(header)

            for i in lec:
                if len(i) > 1:
                    esc.writerow(i)

proc('CI_INBOUND_', 'CI_INBOUND_MIN_', 'CI_INBOUND_PROD_', 'qry_wrm_exc_', 'qry_wrm_int_',
    'RPT_ocupancy_', 'RPT_SUMM_DISP_', 'RPT_WAR_ROOM_', 'RPT_WAR_ROOM_BALANCE_',
    'RPT_WAR_ROOM_PEN_')


def warn(args_warn):
    "quita linea warning y divisor"

    file=args_warn + fen[4:] + '.csv'
    with open(r'\\10.208.0.4\d$\Icaro\TMP_FILES' + os.sep + file, 'r', encoding='utf-8-sig') as c02,\
        open(r'RESULTADOS' + os.sep + file, 'w', newline='') as out2:
        lec = csv.reader(c02)
        hd_warn = next(lec)  # linea warning
        header = next(lec)  # encabezado
        div_head = next(lec)  # divisor
        esc = csv.writer(out2)
        esc.writerow(header)

        for n in lec:
            esc.writerow(n)

warn('RPT_CPP_DETAIL_')


def encabezados(*args_files):
    "añade los encabezados a los archivos, armado del dia"

    file404 = 'qry_alm_mty_cl_404_' + fecha[4:] + '.csv'
    path_noc = r'\\10.208.0.4\d$\Icaro\TMP_FILES' + os.sep + 'querys_nocturno_mty_'
    for f in args_files:
        if f == 'aht_':
            file = f + fen[4:] + '.csv'
        else:
            file = f + fecha[4:] + '.csv'


        with open(path_noc + fecha + os.sep + file, 'r', encoding='utf-8-sig') as h2,\
            open(r'RESULTADOS' + os.sep + file, 'w', newline='') as out3,\
            open(r'RESULTADOS' + os.sep + file404, 'w', newline='') as out4:
            lec = csv.reader(h2)
            esc = csv.writer(out3)
            esc1 = csv.writer(out4)
            esc1.writerow(armado_alm)
            if f == 'aht_':
                esc.writerow(aht_hd)
            else:
                esc.writerow(armado_alm)

            for i in lec:
                esc.writerow(i)

encabezados('qry_alm_mty_c_111_cob_',
            'qry_alm_mty_c_ecs_cob_',
            'qry_alm_mty_cl_111_', 'qry_alm_mty_cl_ecs_')

