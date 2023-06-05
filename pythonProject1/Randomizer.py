import time
start_time = time.time()
import Connection_to_postgresql
import Select_sql
import random

from functions import random_country, random_name, random_secondname, random_surename, itogo, random_date, random_date2, date_for_file, select, select_sysname, bdate_adult_under40, pdate_adult_under40, create_csv, seria_passporta, pdate_adult_18_20, bdate_adult_18_20
from variables_list import nu, ic, so, fo, mo, ko, po, no, bd, bp, i, pd
import execute_quiery
connection = Connection_to_postgresql.create_connection(
    "postgres", "postgres", "mayday", "127.0.0.1", "5432"
)

cursor = connection.cursor()

filetype = select(Select_sql.filetype_select)

brief = select(Select_sql.brief_select)

separator = select(Select_sql.separator_select)

ecode = select(Select_sql.ecode_select)

sysname = select_sysname(Select_sql.sysname_select, separator)
print(separator, filetype, brief, ecode, sysname)

name_of_file = random.randrange(111, 999)
filename = "%s.%s" % ('O'+date_for_file()+str(name_of_file), ecode)
with open(filename, "w", encoding="utf-8") as file:
    while i < 11:
        for item in sysname:
            if item == 'NU':
                nu = str(i)
            elif item == 'IC':
                ic = str(ecode)
            elif item == 'SO':
                so = str(random_name())
            elif item == 'FO':
                fo = str(random_surename())
            elif item == 'MO':
                mo = str(random_secondname())
            elif item == 'KO':
                ko = str(ko)
            elif item == 'PO':
                po = str(4521)
            elif item == 'NO':
                no = str(random.randrange(123456, 987654))
            elif item == 'PD':
                pd = str(pdate_adult_18_20(bd))
                '''
                elif item == 'BD':
                bd = str(bdate1_adult_under40())
                bd = str(random_date())'''
            elif item == 'BP':
                bp = str(random_country())
            elif item == 'BD':
                bd = str(bdate_adult_18_20())
                '''pd = str(random_date())'''
        i += 1
        num_of_workers = i-1
        input_in = nu+separator+ic+separator+so+separator+fo+separator+mo+separator+ko\
                   +separator+po+separator+no+separator+pd+separator+bp+separator+bd
        print(input_in)
        file.write(input_in)
        file.write('\n')
print(num_of_workers)
final_itogo = str(itogo()) + str(num_of_workers)
Itogo_insert = open(filename, "a", encoding="utf-8")
Itogo_insert.write(final_itogo)
Itogo_insert.close()
create_csv(filename,num_of_workers,brief)
end_time = time.time()
print(end_time-start_time)
'''with open('case1.csv','a',newline='', encoding="utf-8") as f:
   w = csv.writer(f)
   w.writerow(['1',str(filename), str(num_of_workers), str(brief), ''])'''
def transliterate(name):
    slovar = {"А":"A", "Б":"B", "В":"V","Г":"G","Д":"D",
              "Е":"E", "Ж":"ZH","З":"Z","И":"I","Й":"J","К":"K","Л":"L","М":"M",
              "Н":"N", "О":"O","П":"P","Р":"R","С":"S","Т":"T","У":"U",
              "Ф":"F","Х":"H","Ц":"TS","Ч":"CH","Ш":"SH","Щ":"SCH",
              "Ь":"","Ы":"Y","Ъ":"","Э":"E","Ю":"YU","Я":"YA",}
    for key in slovar:
        name = name.replace(key, slovar[key])
    return name
def find_unic_number(cursor, docseries, docnumber, doctype):
    sql_find_unic = f'''select count(x) from pinstlicense where docseries = "{docseries}" and numdoc = "{docnumber}" and doctypeid ={doctype}'''
    cursor.execute(sql_find_unic)
    unic = cursor.fecthval()
    return unic
'''def value_gen(case, count, code_obpo, cursor):
    format = {"NU":[],"IC","SO", "FO", "MO","HO","TO","RS","RE"}
    format_var = case
    res_dates_bd = []
    res_dates = []
    i = 1
    while i <= count:
        nu_arr = format.get("NU")
        nu_arr.append(str(i))
        ic_arr = format.get('IC')
        ic_arr.append(str(code_obpo))
        s0_arr = format.get("S0")
        with open('ofile//data//' + format_var.S0_fn), 'r', encoding='utf-8') as f:
            surname = [line.strip().split('   ') for line in f]
            sn = random.choice((surename)[0])
            s0_arr.append(sn)
        fo_arr = format.get("F0")
        with open('ofile//data//' + format_var.F0_fn), 'r', encoding='utf-8') as f:
            names = [line.strip().split('   ') for line in f]
            fn = random.choice((names)[0])
            f0_arr.append(fn)
        mo_arr = format.get("M0")
        with open('ofile//data//' + format_var.M0_fn), 'r', encoding='utf-8') as f:
            names = [line.strip().split('   ') for line in f]
            mn = random.choice((otchestvo)[0])
            m0_arr.append(mn)
        
        bd_arr = format.get('BD')
        start_date, end_date = add_years(date_today(), - format_var.age_min - format_var.age_delta),add_years(date.today(), -format_var.age_min)
        while start_date < end_date:
            start_date += timedelta(days=1)
            res_dates_bd.append(start_date)
        res_bd = random.choice(res_dates_bd)
        bd_arr.append(res_bd.strftime("%d,%m,%Y"))
        
        pd_arr = format.get('PD')
        start_date, end_date = add_years(res_bd, format_var,age_change_passport ), date.today()
        res_dates[]
        while start_date < end_date:
            start_date += timedelta(days=1)
            res_dates.append(start_date)
        res = random.choice(res_dates)
        pd_arr.append(res.strftime("%d,%m,%Y"))
        e0_arr = format.get('E0')
        e0_arr.append(transliterate(fn_upper()))
        g0_arr = format.get('G0')
        g0_arr.append(transliterate(sn_upper()))
        i = i+1
        k0_arr = format.get("K0")
        k0_arr.append(str(format_var.K0))
        if str(format_var.KO) == '21'
            p0_arr = format.get("P0")
            p0_str = seria_passports(res.strftime("%d,%m,%Y"))
            p0_arr.append(p0_str)
            n0_arr = format.get("N0")
            n0_str = str(random.randrange(format_var.n0_min, format_var.no_max))
            if find_unic_number(cursor,p0_str,n0_str,n0_str,20) > 0:
                n0_str = str(random.randrange(format_var.n0_min, format_var.no_max))
            else:
                n0_arr.append(n0_str)
    format.update(
        {"NU": nu_arr})
    return format'''

