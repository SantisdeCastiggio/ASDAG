"""import Select_sql
import random
from functions import random_country, random_name, random_secondname, random_surename, itogo, random_date,random_date2, random_date_for_file
from variables_list import nu, ic, so, fo, mo, ko, po, no, bd, bp, i, pd
import execute_quiery
connection = Connection_to_postgresql.create_connection(
    "postgres", "postgres", "mayday", "127.0.0.1", "5432"
)

filetype_select = Select_sql.filetype_select
cursor.execute(filetype_select)
filetype_uncut = cursor.fetchone()

brief_select = Select_sql.brief_select
cursor.execute(brief_select)
brief_uncut = cursor.fetchone()

sysname_select = Select_sql.sysname_select
cursor.execute(sysname_select)
sysname_uncut = cursor.fetchone()

separator_select = Select_sql.separator_select
cursor.execute(separator_select)
separator_uncut = cursor.fetchone()

ecode_select = Select_sql.ecode_select
cursor.execute(ecode_select)
ecode_uncut = cursor.fetchone()

print(sysname_uncut, separator_uncut, filetype_uncut, brief_uncut, ecode_uncut)
sysname_str = ''.join(map(str, sysname_uncut))
separator = ''.join(map(str, separator_uncut))
filetype = ''.join(map(str, filetype_uncut))
brief = ''.join(map(str, brief_uncut))
ecode = ''.join(map(str, ecode_uncut))
sysname = sysname_str.split(separator)

cursor = connection.cursor()

def select(sql):
    sql = cursor.execute(sql)
    sql = cursor.fetchone()
    sql = ''.join(map(str, sql))
    return sql
def select_sysname(sql,separator):
    sql = cursor.execute(sql)
    sql = cursor.fetchone()
    sql = ''.join(map(str, sql))
    sql = sql.split(separator)
    return sql


filetype = select(Select_sql.filetype_select)

brief = select(Select_sql.brief_select)

separator = select(Select_sql.separator_select)

ecode = select(Select_sql.ecode_select)

sysname = select_sysname(Select_sql.sysname_select, separator)

print(separator, filetype, brief, ecode, sysname)
name_of_file = random.randrange(1234, 9876)
filename = "%s.%s" % ('O'+random_date_for_file()+str(name_of_file), ecode)

with open(filename, "w", encoding="utf-8") as file:
    while i < 10:
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
                po = str(random.randrange(4510, 4522))
            elif item == 'NO':
                no = str(random.randrange(123456, 987654))
            elif item == 'BD':
                bd = str(random_date())
            elif item == 'BP':
                bp = str(random_country())
            elif item == 'PD':
                pd = str(random_date())
        i += 1
        num_of_workers = i-1
        input_in = nu+separator+ic+separator+so+separator+fo+separator+mo+separator+ko+separator+po+separator+no+separator+bd+separator+bp+separator+pd
        print(input_in)
        file.write(input_in)
        input_in = nu, ic, so, fo, mo, ko, po, no, bd, bp, pd
                linput_in = list(input_in)
                jlinput_in = ','.join(linput_in)
                print(jlinput_in)
                file.write(jlinput_in)
        file.write('\n')
print(num_of_workers)
final_itogo = str(itogo()) + str(num_of_workers)
Itogo_insert = open(filename, "a", encoding="utf-8")
Itogo_insert.write(final_itogo)
Itogo_insert.close()"""
from functions import only_year, fms_unit, SNILS,seria_passporta,bdate_adult_45, INN, pdate_adult_45, nomer_passSSSR,foreign_pass_nomer, foreign_pass_seria_nomer, pdate_adult_18_20, bdate_adult_18_20, bdate_youth_0_14, pdate_youth_0_14, bdate_adult_20_45, pdate_adult_20_45, random_long_name, random_long_surename, embosing
import dbf
bd = bdate_adult_45()
print(bd)
print(seria_passporta(bd))
print(nomer_passSSSR())
print()
print(foreign_pass_nomer())
print(foreign_pass_seria_nomer())
x = bdate_adult_18_20()
y = pdate_adult_18_20(x)
z = bdate_youth_0_14()
w = pdate_youth_0_14(z)
n = bdate_adult_20_45()
m = pdate_adult_20_45(n)
l = bdate_adult_45()
k = pdate_adult_45(l)
print(x, y)
print(w, z)
print(n,m)
print(l,k)
d = embosing(random_long_name(),random_long_surename())
print(d)
print(embosing(random_long_name(),random_long_surename()))
print(embosing(random_long_name(),random_long_surename()))
print(embosing(random_long_name(),random_long_surename()))
print(embosing(random_long_name(),random_long_surename()))
print(embosing(random_long_name(),random_long_surename()))
print(embosing(random_long_name(),random_long_surename()))
print(embosing(random_long_name(),random_long_surename()))
print(embosing(random_long_name(),random_long_surename()))
print(INN())
print(SNILS())
import os.path
if os.path.exists('./case1.csv'):
    print(os.path.exists('./case1.csv'))

print(fms_unit())