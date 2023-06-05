import Connection_to_postgresql
from Select_sql import read_format
from Value_generator import value_gen
import random
import time
start_time = time.time()
from functions import random_country, random_name, random_secondname, random_surename, itogo, random_date, random_date2, date_for_file, select, select_sysname, bdate_adult_under40, pdate_adult_under40, create_csv, seria_passporta, pdate_adult_18_20, bdate_adult_18_20

def file_name(code_OBPO):
    filename = "%s.%s" % ('O' + date_for_file() + str(random.randrange(111,999)), code_OBPO)
    sfilename = "%s.%s" % ('O' + date_for_file() + str(random.randrange(111, 999)), code_OBPO)
    return filename, sfilename


def file_gen(filetype, cursor,file_name,case,code_OBPO, count, case1):
    start_time = time.time()
    format_var = case
    format_array, separator = read_format(cursor,filetype,code_OBPO)
    result_array = []
    i = 1
    j = 0
    row_count = 1
    format_value = value_gen(format_var,count, code_OBPO, cursor)
    with open(file_name,'w', encoding = 'utf-8') as file:
        while i <= count:
            for d in format_array:
                if d == "NU":
                    format_var.NU = str(i)
                    result_array.append(format_var.NU)
                elif d == "IC":
                    format_var.IC = str(code_OBPO)
                    result_array.append(format_var.IC)
                elif d == "S0":
                    result_array.append(format_value['S0'][j])
                elif d == "F0":
                    result_array.append(format_value['F0'][j])
                elif d == "M0":
                    result_array.append(format_value['M0'][j])
                elif d == "H0":
                    result_array.append(format_value['H0'][j])
                elif d == "RS":
                    result_array.append(format_value['RS'][j])
                elif d == "NN":
                    result_array.append(format_value['NN'][j])
                elif d == "SN":
                    result_array.append(format_value['SN'][j])
                elif d == "K0":
                    result_array.append(format_value['K0'][j])
                elif d == "P0":
                    result_array.append(format_value['P0'][j])
                elif d == "N0":
                    result_array.append(format_value['N0'][j])
                elif d == "B0":
                    result_array.append(format_value['B0'][j])
                elif d == "D0":
                    result_array.append(format_value['D0'][j])
                elif d == "PI":
                    result_array.append(format_value['PI'][j])
                elif d == "RC":
                    result_array.append(format_value['RC'][j])
                elif d == "BD":
                    result_array.append(format_value['BD'][j])
                elif d == "BC":
                    result_array.append(format_value['BC'][j])
                elif d == "BP":
                    result_array.append(format_value['BP'][j])
                elif d == "PW":
                    result_array.append(format_value['PW'][j])
                elif d == "SC":
                    result_array.append(format_value['SC'][j])
                elif d == "PH":
                    result_array.append(format_value['PH'][j])
                elif d == "WP":
                    result_array.append(format_value['WP'][j])
                elif d == "MP":
                    result_array.append(format_value['MP'][j])
                elif d == "EM":
                    result_array.append(format_value['EM'][j])
                elif d == "EP":
                    result_array.append(format_value['EP'][j])
                elif d == "OE":
                    result_array.append(format_value['OE'][j])
                elif d == "CI":
                    result_array.append(format_value['CI'][j])
                elif d == "MN":
                    result_array.append(format_value['MN'][j])
                elif d == "MR":
                    result_array.append(format_value['MR'][j])
                elif d == "MI":
                    result_array.append(format_value['MI'][j])
                elif d == "AC":
                    result_array.append(format_value['AC'][j])
                elif d == "RG":
                    result_array.append(format_value['RG'][j])
                elif d == "AR":
                    result_array.append(format_value['AR'][j])
                elif d == "CT":
                    result_array.append(format_value['CT'][j])
                elif d == "TW":
                    result_array.append(format_value['TW'][j])
                elif d == "ST":
                    result_array.append(format_value['ST'][j])
                elif d == "HS":
                    result_array.append(format_value['HS'][j])
                elif d == "FR":
                    result_array.append(format_value['FR'][j])
                elif d == "BL":
                    result_array.append(format_value['BL'][j])
                elif d == "FL":
                    result_array.append(format_value['FL'][j])
                elif d == "G0":
                    result_array.append(format_value['G0'][j])
                elif d == "E0":
                    result_array.append(format_value['E0'][j])
                elif d == "A2U":
                    result_array.append(format_value['A2U'][j])
                elif d == "A3S":
                    result_array.append(format_value['A3S'][j])
                elif d == "A4C":
                    result_array.append(format_value['A4C'][j])
                elif d == "A6P":
                    result_array.append(format_value['A6P'][j])
            j += 1
            i += 1
            row_count += 1
            final = separator.join(result_array)
            file.write(str(final))
            file.write('\n')
            result_array.clear()
    final_itogo = str(itogo()) + str(row_count-1)
    Itogo_insert = open(file_name, "a", encoding="utf-8")
    Itogo_insert.write(final_itogo)
    Itogo_insert.close()
    create_csv(file_name, row_count, code_OBPO)
    end_time = time.time()
    print(end_time - start_time)
