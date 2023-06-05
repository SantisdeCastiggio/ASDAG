import random
import csv
import os
import datetime
import Connection_to_postgresql
connection = Connection_to_postgresql.create_connection(
    "postgres", "postgres", "mayday", "127.0.0.1", "5432"
)
cursor = connection.cursor()
def random_date():
    start_date = datetime.date(1950, 1, 1)
    end_date = datetime.date(2005, 1, 1)
    num_days = (end_date - start_date).days
    rand_days = random.randint(1, num_days)
    random_date = start_date + datetime.timedelta(days=rand_days)
    t = random_date.strftime("%d.%m.%Y")
    return t

def bdate_adult_under40():
    start_date = datetime.date(1984, 1, 1)
    end_date = datetime.date(2004, 1, 1)
    num_days = (end_date - start_date).days
    rand_days = random.randint(1, num_days)
    random_date = start_date + datetime.timedelta(days=rand_days)
    bdate_under40 = random_date.strftime("%d.%m.%Y")
    return bdate_under40

def pdate_adult_under40(x):
    f = datetime.datetime.strptime(x, "%d.%m.%Y")-datetime.timedelta(days=20*365)
    return f.strftime("%d.%m.%Y")

def bdate_adult_18_20():
    start_date = datetime.date(2003, 1, 1)
    end_date = datetime.date(2005, 1, 1)
    num_days = (end_date - start_date).days
    rand_days = random.randint(1, num_days)
    random_date = start_date + datetime.timedelta(days=rand_days)
    bdate_adult_18_20 = random_date.strftime("%d.%m.%Y")
    return bdate_adult_18_20

def pdate_adult_18_20(x):
    if datetime.datetime.strptime(x, "%d.%m.%Y") > datetime.datetime.strptime('01.01.2004', "%d.%m.%Y"):
        pdate_adult_18_20 = datetime.datetime.strptime(x, "%d.%m.%Y") + datetime.timedelta(days=14 * 365)
        return pdate_adult_18_20.strftime("%d.%m.%Y")
    else:
        pdate_adult_18_20 = datetime.datetime.strptime(x, "%d.%m.%Y")+datetime.timedelta(days=20*365)
        return pdate_adult_18_20.strftime("%d.%m.%Y")

def bdate_youth_14_18():
    start_date = datetime.date(2005, 1, 1)
    end_date = datetime.date(2009, 1, 1)
    num_days = (end_date - start_date).days
    rand_days = random.randint(1, num_days)
    random_date = start_date + datetime.timedelta(days=rand_days)
    bdate_youth_14_18 = random_date.strftime("%d.%m.%Y")
    return bdate_youth_14_18

def pdate_youth_14_18(x):
    pdate_youth_14_18 = datetime.datetime.strptime(x, "%d.%m.%Y")-datetime.timedelta(days=14*365)
    return pdate_youth_14_18.strftime("%d.%m.%Y")

def pdate_youth_14_18_prosrocheno(x):
    pdate_youth_14_18 = datetime.datetime.strptime(x, "%d.%m.%Y")-datetime.timedelta(days=14*365)+ datetime.timedelta(days = 3 * 31)
    return pdate_youth_14_18.strftime("%d.%m.%Y")


def bdate_youth_0_14():
    start_date = datetime.date(2009, 1, 1)
    end_date = datetime.date(2023, 1, 1)
    num_days = (end_date - start_date).days
    rand_days = random.randint(1, num_days)
    random_date = start_date + datetime.timedelta(days=rand_days)
    bdate_youth_0_14 = random_date.strftime("%d.%m.%Y")
    return bdate_youth_0_14

def pdate_youth_0_14(x):
    if datetime.datetime.strptime(x, "%d.%m.%Y") > datetime.datetime.strptime('01.01.2010', "%d.%m.%Y"):
        pdate_youth_0_14 = datetime.datetime.strptime(x, "%d.%m.%Y")
        return pdate_youth_0_14.strftime("%d.%m.%Y")
    else:
        pdate_youth_0_14 = datetime.datetime.strptime(x, "%d.%m.%Y") + datetime.timedelta(days=14 * 365)
        return pdate_youth_0_14.strftime("%d.%m.%Y")

def pdate_youth_0_14_prosrocheno(x):
    if datetime.datetime.strptime(x, "%d.%m.%Y") > datetime.datetime.strptime('01.01.2010', "%d.%m.%Y"):
        pdate_youth_0_14 = datetime.datetime.strptime(x, "%d.%m.%Y")
        return pdate_youth_0_14.strftime("%d.%m.%Y")
    else:
        pdate_youth_0_14 = datetime.datetime.strptime(x, "%d.%m.%Y") + datetime.timedelta(days=14 * 365) + datetime.timedelta(days = 3 * 31)
        return pdate_youth_0_14.strftime("%d.%m.%Y")

def bdate_adult_20_45():
    start_date = datetime.date(1978, 1, 1)
    end_date = datetime.date(2003, 1, 1)
    num_days = (end_date - start_date).days
    rand_days = random.randint(1, num_days)
    bdate_adult_20_45 = start_date + datetime.timedelta(days=rand_days)
    return bdate_adult_20_45.strftime("%d.%m.%Y")

def pdate_adult_20_45(x):
    if datetime.datetime.strptime(x, "%d.%m.%Y") > datetime.datetime.strptime('01.01.1979', "%d.%m.%Y"):
        pdate_adult_20_45 = datetime.datetime.strptime(x, "%d.%m.%Y") + datetime.timedelta(days=20 * 365)
        return pdate_adult_20_45.strftime("%d.%m.%Y")
    else:
        pdate_adult_20_45 = datetime.datetime.strptime(x, "%d.%m.%Y") + datetime.timedelta(days=45 * 365)
        return pdate_adult_20_45.strftime("%d.%m.%Y")

def pdate_adult_20_45_prosrocheno(x):
    if datetime.datetime.strptime(x, "%d.%m.%Y") > datetime.datetime.strptime('01.01.1979', "%d.%m.%Y"):
        pdate_adult_20_45 = datetime.datetime.strptime(x, "%d.%m.%Y") + datetime.timedelta(days=20 * 365) + datetime.timedelta(days = 3 * 31)
        return pdate_adult_20_45.strftime("%d.%m.%Y")
    else:
        pdate_adult_20_45 = datetime.datetime.strptime(x, "%d.%m.%Y") + datetime.timedelta(days=45 * 365) + datetime.timedelta(days = 3 * 31)
        return pdate_adult_20_45.strftime("%d.%m.%Y")

def bdate_adult_45():
    start_date = datetime.date(1951, 1, 1)
    end_date = datetime.date(1978, 1, 1)
    num_days = (end_date - start_date).days
    rand_days = random.randint(1, num_days)
    bdate_adult_45 = start_date + datetime.timedelta(days=rand_days)
    return bdate_adult_45.strftime("%d.%m.%Y")

def pdate_adult_45(x):
    pdate_adult_45 = datetime.datetime.strptime(x, "%d.%m.%Y") + datetime.timedelta(days=45 * 365)
    return pdate_adult_45.strftime("%d.%m.%Y")

def pdate_adult_45_prosrocheno(x):
    pdate_adult_45 = datetime.datetime.strptime(x, "%d.%m.%Y") + datetime.timedelta(days=45 * 365) + datetime.timedelta(days = 3 * 31)
    return pdate_adult_45.strftime("%d.%m.%Y")


def only_year():
    start_date = datetime.date(1951, 1, 1)
    end_date = datetime.date(1978, 1, 1)
    num_days = (end_date - start_date).days
    rand_days = random.randint(1, num_days)
    only_year = start_date + datetime.timedelta(days=rand_days)
    return only_year.strftime("%Y")

def seria_passporta(x):
    data_blanka_full = datetime.datetime.strptime(x, "%d.%m.%Y")
    f = data_blanka_full.strftime("%Y")
    seria_passporta =  str(45)+str(f[2:])
    return seria_passporta

def nomer_svidor():
    with open("azbuka.txt", "r", encoding='utf-8') as f:
        azbuka1 = [line.strip().split('  ') for line in f]
    with open("ROMAN.txt", "r", encoding='utf-8') as f:
        ROMAN1 = [line.strip().split('  ') for line in f]
    nomer_svidor = str(' '.join(random.choice(ROMAN1))) + "-" + str(random.choice(azbuka1)[0]) + str(random.choice(azbuka1)[0]) + " " + str(random.randrange(111111, 999999))
    return nomer_svidor

def nomer_passSSSR():
    with open("azbuka.txt", "r", encoding='utf-8') as f:
        azbuka1 = [line.strip().split('  ') for line in f]
    with open("ROMAN.txt", "r", encoding='utf-8') as f:
        ROMAN1 = [line.strip().split('  ') for line in f]
    nomer_passSSSR = str(' '.join(random.choice(ROMAN1)))+"-"+str(random.choice(azbuka1)[0])+str(random.choice(azbuka1)[0]) +" " + str(random.randrange(111111,999999))
    return nomer_passSSSR

def foreign_pass_nomer():
    i = 0
    m = ""
    while i < 9:
            with open("foreign_pass.txt", "r", encoding='utf-8') as f:
                foreign_pass1 = [line.strip().split('  ') for line in f]
            c = str(' '.join(random.choice(foreign_pass1)))
            m = m+c
            i = i+1
    return m

def foreign_pass_seria_nomer():
    with open("foreign_azbuka.txt", "r", encoding='utf-8') as f:
        azbuka2 = [line.strip().split('  ') for line in f]
    i = 0
    m = ""
    while i < 9:
            with open("foreign_pass.txt", "r", encoding='utf-8') as f:
                foreign_pass1 = [line.strip().split('  ') for line in f]
            c = str(' '.join(random.choice(foreign_pass1)))
            m = m+c
            i = i+1
    return str(random.choice(azbuka2)[0])+str(random.choice(azbuka2)[0]) + " " + str(m)

def migrats_card():
    mig_card = "40"+" "+"08"+" "+str(random.randrange(111111,999999))
    return mig_card
def vid_na_zhit():
    vid = "40"+""+"05"+" "+str(random.randrange(1111111,999999))
    return vid

def random_date2(date):
    start_date = datetime.date(1950, 1, 1)
    end_date   = datetime.date(2005, 1, 1)
    num_days = (end_date - start_date).days
    rand_days = random.randint(1, num_days)
    random_date = start_date + datetime.timedelta(days=rand_days)
    f = random_date.strftime("%d.%m.%Y")
    while f > date == True:
        return f
    else:
        f = datetime.datetime.strptime(f, "%d.%m.%Y")+datetime.timedelta(days=14*365)
        return f

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


def random_date_for_file():
    start_date = datetime.date(2022, 1, 1)
    end_date   = datetime.date(2023, 1, 1)
    num_days   = (end_date - start_date).days
    rand_days   = random.randint(1, num_days)
    random_date = start_date + datetime.timedelta(days=rand_days)
    return random_date.strftime("%y%m%d")


def date_for_file():
    return str(datetime.datetime.now().strftime("%y%m%d"))

def random_name():
    with open("names2.txt", "r", encoding='utf-8') as f:
        names=[line.strip().split('  ') for line in f]
        return random.choice(names)[0]

def random_long_name():
    with open("dlinnie_imena.txt", "r", encoding='utf-8') as f:
        names=[line.strip().split('  ') for line in f]
        return random.choice(names)[0]

def standard_name():
    with open("names_standardized.txt", "r", encoding='utf-8') as f:
        names = [line.strip().split('  ') for line in f]
        return random.choice(names)[0]

def random_surename():
    with open("surename2.txt", "r", encoding='utf-8') as f:
        surenames = [line.strip().split('  ') for line in f]
        return random.choice(surenames)[0]

def random_long_surename():
    with open("dlinnie_familii.txt", "r", encoding='utf-8') as f:
        surenames = [line.strip().split('  ') for line in f]
        return random.choice(surenames)[0]

def standard_surename():
    with open("surenames_standardized.txt", "r", encoding='utf-8') as f:
        surenames = [line.strip().split('  ') for line in f]
        return random.choice(surenames)[0]

def random_secondname():
    with open("othcestvo2.txt", "r", encoding='utf-8') as f:
        secondnames = [line.strip().split('  ') for line in f]
        return random.choice(secondnames)[0]

def itogo():
    with open("itogo.txt", "r", encoding='utf-8') as f:
        itogo1 = [line.strip().split('  ') for line in f]
        return random.choice(itogo1)[0]

def random_country():
    with open("Countries.txt", "r", encoding='utf-8') as f:
        countries = [line.strip().split('  ') for line in f]
        return random.choice(countries)[0]
def embosing(x,y):
    a = y+" "+x
    k = y + " "+ x[0]+ "."
    n = len([v for v in a if v.isalpha()])
    p = len([b for b in y if b.isalpha()])
    if n <= 14:
        return a
    elif 14 > n >= 20:
        return a
    elif n > 20:
       if p < 17:
           return k
       elif p < 19:
           return y
       else:
           g = p - 19
           ret = y[:-g]
           return ret

def add_years(dates, years):
    try:
        return dates.replace(year = dates.year + years)
    except ValueError:
        return dates + (datetime.date(dates.year + years, 3, 1) - datetime.date(dates.year, 3, 1))
def create_csv(filename,num_of_workers,brief):
        if os.path.isfile('./case1.csv') == False:
            with open('case1.csv', 'w', newline='', encoding="utf-8") as f:
                w = csv.writer(f)
                w.writerow(['Кейс', 'название О файла', 'количество строк', 'ОБПО', 'загружен'])
                w.writerow(['1', str(filename), str(num_of_workers), str(brief), ''])
        else:
            with open('case1.csv', 'a', newline='', encoding="utf-8") as f:
                w = csv.writer(f)
                w.writerow(['1',str(filename), str(num_of_workers), str(brief), ''])
def INN():
    i = 0
    spisok = ["1","2","3","4","5","6","7","8","9","0"]
    INN = ""
    while i < 12:
        INN += str(random.choice(spisok))
        i += 1
    return INN
def mobilephone():
    spisok_operatorov = ["910","915","916","917","919",'985','986','925','926','929','936','999','901',
                         '958','977','999','903','905','906','909','962','963','964','965','966','967',
                         '968','969','980','983','999']
    mobilephone = "+7"+str(random.choice(spisok_operatorov))+str(random.randrange(111,999))+str(random.randrange(11,99))+str(random.randrange(11,99))
    return mobilephone
def stationaryphone():
    spisok = ["495","499",'496','498']
    stationary = "+7"+str(random.choice(spisok))+"-"+str(random.randrange(111,999))+'-'+str(random.randrange(11,99))+str(random.randrange(11,99))
    return stationary
def SNILS():
    SNILS = str(random.randrange(111,999))+"-"+str(random.randrange(111,999))+"-"+str(random.randrange(111,999))+" "+str(random.randrange(11,99))
    return SNILS
def email():
    slovar_angl = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N',
              'O','P','Q','R','S','T','U','V','W','X','Y','Z']
    slovar_mail = ['mail.ru','gmail.com','yandex.ru','list.ru','bk.ru','vk.ru','inbox.ru']
    email = "test"+str(random.choice(slovar_angl))+str(random.choice(slovar_angl))+str(random.choice(slovar_angl))+"@"+str(random.choice(slovar_mail))
    return email
def armia_nomer():
    slovar = ["А","Б","В","Г","Д","Е","Ж","З","И","Й","К","Л","М",
              "Н","О","П","Р","С","Т","У","Ф","Х","Ц","Ч","Ш","Щ"
    ,"Ь","Ы","Ъ","Э","Ю","Я"]
    armia_nomer = str(random.choice(slovar))+'-'+str(random.randrange(111111,999999))
    return armia_nomer
def armia_rang():
    slovar = ["Рядовой","Младший сержант","Старший сержант","Старшина","Прапорщик","Старший прапорщик",
              "Младший лейтенант","Лейтенант","Старший лейтенант","Капитан","Майор",
              "Подполковник","Полковник","Генерал-майор","Генерал-лейтенант","Генерал-полковник"]
    armia_rang = str(random.choice(slovar))
    return armia_rang
def gender():
    slovar = ["М"]
    gender = str(random.choice(slovar))
    return gender
def kodovoe_slovo():
    slovar = ["А","Б","В","Г","Д","Е","Ж","З","И","Й","К","Л","М",
              "Н","О","П","Р","С","Т","У","Ф","Х","Ц","Ч","Ш","Щ"
    ,"Ь","Ы","Ъ","Э","Ю","Я"]
    kodovoe_slovo = 'тест'+str(random.choice(slovar))+str(random.choice(slovar))+str(random.choice(slovar))
    return kodovoe_slovo
def dohod():
    slovar = ["50","75","100","115","130","145","160","175","200"]
    dohod=str(random.choice(slovar))
    return dohod
def a3s():
    slovar = ['очное',"заочное","очно-заочное","вечернее"]
    a3s = str(random.choice(slovar))
    return a3s
def a4c():
    slovar = ['1',"2",'3','4']
    a4c = str(random.choice(slovar))
    return a4c
def a2u():
    a2u= '45286555'
    return a2u
def a6p():
    slovar = ['101000, г. Москва, Большой Харитоньевский пер., д. 4, стр.',
              '101000, г. Москва, Кривоколенный пер., д. 3А',
              '101000, г. Москва, Потаповский пер., д. 16, стр. 10',
              '101000, г. Москва, ул. Мясницкая, д. 11',
              '101000, г. Москва, ул. Мясницкая, д. 20',
              '101000, г. Москва, ул. Мясницкая, д. 18, стр. 1',
              '105062, г. Москва, пер. Лялин, д. 3А',
              '105066, г. Москва, ул. Старая Басманная, д. 21/4, строен. 1',
              '109028, г. Москва, пер. Трехсвятительский Малый, д. 8/2, стр. 1',
              '109028, г. Москва, пер. Хитровский, д. 2/8, корп. 5',
              '109074, г. Москва, Славянская пл., д. 4, стр. 2',
              '115054, г. Москва, ул. Пионерская Малая, д. 12',
              '117312, г. Москва, ул. Вавилова, д. 7',
              '119048, г. Москва, ул. Усачева, д. 6',
              '119017, г. Москва, ул. Ордынка М., д. 17, строен. 1',
              '119049, г. Москва, ул. Шаболовка, д. 26, стр. 3, 4, 5',
              '123022, г. Москва, Трехсвятительский Большой пер., д. 3',
              '123458, г. Москва, ул. Таллинская, д. 34',
              '127299, г. Москва, ул. Космонавта Волкова, д. 18',
              '125009, г. Москва, пер. Гнездниковский Малый, д. 4',
              '127051, г. Москва, пер. Колобовский 3-й, д. 8, стр. 2',
              '129272, г. Москва, ул. Трифоновская, д. 57, стр. 1, стр. 2',
              '101000, г. Москва, ул. Мясницкая, д. 13, стр. 4',
              '101000, г. Москва, пер. Армянский, д. 4, строен. 2',
              '115184, г. Москва, ул. Большая Ордынка, д. 47/7, строен. 1',
              '115184, г. Москва, ул. Большая Ордынка, д. 47/7, строен. 2',
              '109240, г. Москва, ул. Солянка, д. 14а, стр. 1',
              '105066, г. Москва, ул. Старая Басманная, д. 21/4, строен. 3',
              '105066, г. Москва, ул. Старая Басманная, д. 21/4, строен. 5',
              '105066, г. Москва, ул. Старая Басманная, д. 21/4, строен. 4',
              '119049, г. Москва, ул. Шаболовка, д. 26, стр. 2',
              '119049, г. Москва, ул. Шаболовка, д. 28/11, стр. 2',
              '109028, г. Москва, Покровский б-р, д. 11, стр. 1',
              '109028, г. Москва, Покровский б-р, д. 11, стр. 2',
              '109028, г. Москва, Покровский б-р, д. 11, стр. 3',
              '109028, г. Москва, Покровский б-р, д. 11, стр. 4',
              '109028, г. Москва, Покровский б-р, д. 11, стр. 5',
              '109028, г. Москва, Покровский б-р, д. 11, стр. 10',
              '109028, г. Москва, Покровский б-р, д. 11, стр. 13',
              '117418, г. Москва, ул. Профсоюзная, д. 33, корп. 4',
              '115184, г. Москва, ул. Малая Ордынка, д. 29',
              '109028, г. Москва, Покровский б-р, д. 11, стр. 6',
              '105679, г. Москва, Измайловское шоссе, д.44, стр.2']
    a6p = str(random.choice(slovar))
    return a6p
def mail_index():
    slovar = ['101000']
    mail_index = str(random.choice(slovar))
    return mail_index
def region():
    slovar = ['Москва']
    region = str(random.choice(slovar))
    return region
def district():
    slovar = ['Басманный']
    district = str(random.choice(slovar))
    return district
def city():
    slovar = ['Москва']
    city = str(random.choice(slovar))
    return city
def tw():
    slovar = ['Москва']
    tw = str(random.choice(slovar))
    return tw
def street():
    slovar = ['Старая Басманная']
    tw = "ул."+str(random.choice(slovar))
    return tw
def dom():
    slovar = ["10","10","11/2","11А","12","12","","12",
              "13","14/2","14/2","14/2","14/2","14/2","15А",
              "5","15А","15","0","15","1","15","15","0","15",
              "1","15","15","5","5","6","6","7","7","9","9","9",
              "16/1","16/1Б","16/1Б","16/1Б","16/1Б","16/1Б","16/1Б",
              "16/1Б","17","17","17","17","17","17","18","18","2","18"
        ,"3","18","18","18","18","19","19","2","19","6","19","19","19",
              "19","19","20","20","20","20","20","20","20","20","20","4",
              "20","6","20","5","20","7","20","7","21/4","21/4","0","21/4",
              "1","21/4","2","21/4","8","21/4","21/4","2","21/4","4","21/4"
        ,"6","21/4","21/4","21/4","21/4","21/4","21/4","21/4","22","22кА",
              "22кБ","23/9","23/9","24","24","24","24","25","25","25","26","28/2",
              "30/1","30/1","31","31","32","32А","А","32","33","34","35","35",
              "36","38","38/2","38/2","38/2","38/2","10","10","11/2","11А","12","12"]
    dom= str(random.choice(slovar))
    return dom
def stroenie():
    slovar = ["1","2","3"]
    stroenie= "стр."+str(random.choice(slovar))
    return stroenie
def korpus():
    slovar = ["1"]
    slovar = ["1"]
    korpus= "к."+str(random.choice(slovar))
    return korpus
def flat():
    slovar = ["1","2","3","4","5","6","7","8","9","10"]
    flat= "кв." + str(random.choice(slovar))
    return flat
def ep():
    slovar = ["1","2",'3']
    ep= str(random.choice(slovar))
    return ep
def oe():
    slovar = ["3","4",'5']
    oe= str(random.choice(slovar))
    return oe

def fms_unit():
    with open("fms_unit.txt", "r", encoding='utf-8') as f:
        fms = [line.strip().split(',') for line in f]
        fms1 = random.choice(fms)
        fms_code = ''.join(fms1[0])
        fms_name = ''.join(fms1[1])
        return fms_code,fms_name
def transliterate(name):
    slovar = {"А":"A", "Б":"B", "В":"V","Г":"G","Д":"D",
              "Е":"E", "Ж":"ZH","З":"Z","И":"I","Й":"J","К":"K","Л":"L","М":"M",
              "Н":"N", "О":"O","П":"P","Р":"R","С":"S","Т":"T","У":"U",
              "Ф":"F","Х":"H","Ц":"TS","Ч":"CH","Ш":"SH","Щ":"SCH",
              "Ь":"","Ы":"Y","Ъ":"","Э":"E","Ю":"YU","Я":"YA",}
    for key in slovar:
        name = name.replace(key, slovar[key])
    return name
'''
bd_arr = format.get('BD') 
start_date, end_date = add_years(date_today(), - format_var.age_min - format_var.age_delta),
 add_years(date.today(),-format_var.age_min)
    while start_date<end_date:
        start_date += timedelta(days=1)
        res_dates_bd.append(start_date)
    res_bd = random.choice(res_dates_bd)
    bd_arr.append(res_bd.strftime("%d,%m,%Y"))
    pd_arr = format.get('PD')
    start_date,end_date = add_years(res_bd, ), date.today()
    res_dates[]format_var.age_change_passport
    while start_date < end_date:
        start_date += timedelta(days = 1)
        res_dates.append(start_date)
    res = random.choice(res_dates)
    pd_arr.append(res.strftime("%d,%m,%Y"))'''
