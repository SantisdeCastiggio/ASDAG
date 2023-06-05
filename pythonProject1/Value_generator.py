import random
import time
import datetime
start_time = time.time()
import Connection_to_postgresql
import Select_sql
import random
from functions import transliterate,add_years,random_country,\
    standard_name, standard_surename, itogo,random_secondname,\
    random_date, random_date2, date_for_file, select, select_sysname, \
    bdate_adult_under40, pdate_adult_under40, create_csv, seria_passporta,\
    pdate_adult_18_20, bdate_adult_18_20,oe,ep, INN, SNILS,mobilephone,stationaryphone,email,armia_nomer,armia_rang,gender,kodovoe_slovo,dohod,a3s,a4c,a2u,a6p,mail_index,region,district,city,tw,street,dom,stroenie,korpus,flat,fms_unit
def value_gen(case, count, code_obpo, cursor):
    format = {"NU":[],"IC":[],"S0":[],"F0":[],"M0":[],"H0":[],
              "RS":[],"NN":[],"SN":[],"BD":[],
              "K0":[],"P0":[],"N0":[],"B0":[],"D0":[],"PI":[],"PD":[],
              "D7":[],"K2":[],"P2":[],"N2":[],"B2":[],"I2":[],
              "D2":[],"D8":[],"RC":[],"BC":[],"BP":[],"PW":[],
              "SC":[],"PH":[],"WP":[],"MP":[],"EM":[],"EI":[],
              "EP":[],"OE":[],"CI":[],"MN":[],"MR":[],"AD":[],
              "MI":[],"RG":[],"AR":[],"CT":[],"TW":[],"ST":[],
              "HS":[],"FR":[],"FL":[],"BL":[],"G0":[],"E0":[],"EC":[],
              "CP":[],"VD":[],"ED":[],"CF":[],"SD":[],"SE":[],
              "SB":[],"AT":[],"AN":[],"IM":[],"AF":[],
              "A2U":[],"A3S":[],"A4C":[],"A6P":[]
              }
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
        #with open(('ofile//data//' + format_var.S0_fn), 'r', encoding='utf-8') as f:
            #surenames = [line.strip().split('   ') for line in f]
        #sn = random.choice(surenames)[0])
        sn = str(standard_surename())
        s0_arr.append(sn)
        f0_arr = format.get("F0")
        #names = [line.strip().split('   ') for line in f]
        #fn = random.choice((names)[0])
        fn = str(standard_name())
        f0_arr.append(fn)
        m0_arr = format.get("M0")
        #with open(('ofile//data//' + format_var.M0_fn), 'r', encoding='utf-8') as f:
            #otchestvo = [line.strip().split('   ') for line in f]
        #mn = random.choice((otchestvo)[0])
        mn = str(random_secondname())
        m0_arr.append(mn)
        h0_arr = format.get("H0")
        h0_arr.append(sn+" "+fn+" "+mn)
        rs_arr = format.get("RS")
        rs_arr.append("РФ")
        nn_arr = format.get('NN')
        nn_arr.append(str(INN()))
        sn_arr = format.get('SN')
        sn_arr.append(str(SNILS()))
        bd_arr = format.get('BD')
        bd = str(bdate_adult_18_20())
        bd_arr.append(bd)
        pd_arr = format.get('BD')
        pd = str(str(pdate_adult_18_20(bd)))
        pd_arr.append(pd)
        '''bd_arr = format.get('BD')
        start_date, end_date = add_years(datetime.date.today(), - format_var.age_min - format_var.age_delta), add_years(
            datetime.date.today(), -format_var.age_min)
        while start_date < end_date:
            start_date += datetime.timedelta(days=1)
            res_dates_bd.append(start_date)
        res_bd = random.choice(res_dates_bd)
        bd_arr.append(res_bd.strftime("%d,%m,%Y"))

        pd_arr = format.get('PD')
        start_date, end_date = add_years(res_bd, format_var.age_change_passport), datetime.date.today()
        res_dates = []
        while start_date < end_date:
            start_date += datetime.timedelta(days=1)
            res_dates.append(start_date)
        res = random.choice(res_dates)
        pd_arr.append(res.strftime("%d,%m,%Y"))'''
        e0_arr = format.get('E0')
        e0_arr.append(transliterate(fn.upper()))
        g0_arr = format.get('G0')
        g0_arr.append(transliterate(sn.upper()))
        i = i + 1
        k0_arr = format.get("K0")
        k0_arr.append(str(format_var.K0))
        if str(format_var.K0) == '21':
            p0_arr = format.get("P0")
            p0_str = seria_passporta(pd)
            p0_arr.append(p0_str)
            n0_arr = format.get("N0")
            n0 = str(random.randrange(111111, 666666))
            n0_arr.append(n0)
            b0_arr = format.get('B0')
            b0_arr.append(p0_str+n0)
            '''if find_unic_number(cursor, p0_str, n0_str, n0_str, 20) > 0:
                n0_str = str(random.randrange(format_var.n0_min, format_var.no_max))
            else:
                n0_arr.append(n0_str)'''
            d0,pi = fms_unit()
            d0_arr = format.get('D0')
            d0_arr.append(str(d0))
            pi_arr = format.get('PI')
            pi_arr.append(str(pi))
            rc_arr = format.get('RC')
            rc_arr.append('Россия')
            bc_arr = format.get('BC')
            bc_arr.append('Россия')
            bp_arr = format.get('BP')
            bp_arr.append(str(city()))
            pw_arr = format.get('PW')
            pw_arr.append(str(kodovoe_slovo()))
            sc_arr = format.get('SC')
            sc_arr.append(str(gender()))
            ph_arr = format.get("PH")
            ph_arr.append(str(stationaryphone()))
            wp_arr = format.get("WP")
            wp_arr.append(str(stationaryphone()))
            mp_arr = format.get("MP")
            mp_arr.append(str(mobilephone()))
            em_arr = format.get("EM")
            em_arr.append(str(email()))
            ep_arr = format.get('EP')
            ep_arr.append(str(ep()))
            oe_arr = format.get('OE')
            oe_arr.append(str(oe()))
            ci_arr = format.get('CI')
            ci_arr.append(str(dohod()))
            mn_arr = format.get("MN")
            mn_arr.append(str(armia_nomer()))
            mr_arr = format.get('MR')
            mr_arr.append(str(armia_rang()))
            mi_arr = format.get("MI")
            mi = str(mail_index())
            mi_arr.append(mi)
            rg_arr = format.get("RG")
            rg = str(region())
            rg_arr.append(rg)
            ar_arr = format.get("AR")
            ar = str(district())
            ar_arr.append(ar)
            ct_arr = format.get("CT")
            ct = str(city())
            ct_arr.append(ct)
            tw_arr = format.get("TW")
            tw = str("г.")
            tw_arr.append(tw)
            st_arr = format.get("ST")
            st = str(street())
            st_arr.append(st)
            hs_arr = format.get("HS")
            hs = str(dom())
            hs_arr.append(hs)
            fr_arr = format.get("FR")
            fr = str(korpus())
            fr_arr.append(fr)
            bl_arr = format.get("BL")
            bl = str(stroenie())
            bl_arr.append(bl)
            fl_arr = format.get("FL")
            fl = str(flat())
            fl_arr.append(fl)
            a2u_arr = format.get("A2U")
            a2u1 = str(a2u())
            a2u_arr.append(a2u1)
            a3s_arr = format.get("A3S")
            a3s1 = str(a3s())
            a3s_arr.append(a3s1)
            a4c_arr = format.get("A4C")
            a4c1 = str(a4c())
            a4c_arr.append(a4c1)
            a6p_arr = format.get("A6P")
            a6p1 = str(a6p())
            a6p_arr.append(a6p1)
    format.update({"NU": nu_arr, "IC":ic_arr,"S0":s0_arr,"F0":f0_arr,"M0":m0_arr,"H0":h0_arr
            ,"RS":rc_arr,"NN":nn_arr,"SN":sn_arr,"BD":bd_arr,
              "K0":k0_arr,"P0":p0_arr,"NO":n0_arr,"B0":b0_arr,"D0":d0_arr,"PI":pi_arr,"PD":pd_arr
            ,"RC":rc_arr,"BC":bc_arr,"BP":bp_arr,"PW":pw_arr,
              "SC":sc_arr,"PH":ph_arr,"WP":wp_arr,"MP":mp_arr,"EM":em_arr,
              "EP":ep_arr,"OE":oe_arr,"CI":ci_arr,"MN":mn_arr,"MR":mr_arr,
              "MI":mi_arr,"RG":rg_arr,"AR":ar_arr,"CT":ct_arr,"TW":tw_arr,"ST":st_arr,
              "HS":hs_arr,"FR":fr_arr,"FL":fl_arr,"BL":bl_arr,"G0":g0_arr,"E0":e0_arr,
              "A2U":a2u_arr,"A3S":a3s_arr,"A4C":a4c_arr,"A6P":a6p_arr})
    return format