sysname_select = '''SELECT
    sysname
FROM
    tenterprise AS e
    INNER JOIN tentformat AS r ON e.enterpriseID=r.EnterpriseID
    INNER JOIN tinputformat AS f ON r.inputformatid = f.inputformatid
    WHERE
        f.brief = 'OkodPO' and f.filltype = 1 and f.separator = ',' '''

sysname_select2 = '''SELECT
    sysname
FROM
    tenterprise AS e
    INNER JOIN tentformat AS r ON e.enterpriseID=r.EnterpriseID
    INNER JOIN tinputformat AS f ON r.inputformatid = f.inputformatid
    WHERE
        f.brief = 'OkodPO' and f.filltype = 1 and f.separator = ';' '''

separator_select= '''SELECT
    separator
FROM
    tenterprise AS e
    INNER JOIN tentformat AS r ON e.enterpriseID=r.EnterpriseID
    INNER JOIN tinputformat AS f ON r.inputformatid = f.inputformatid
    WHERE
        f.brief = 'OkodPO' and f.filltype = 1 and f.separator = ',' '''

separator_select2= '''SELECT
    separator
FROM
    tenterprise AS e
    INNER JOIN tentformat AS r ON e.enterpriseID=r.EnterpriseID
    INNER JOIN tinputformat AS f ON r.inputformatid = f.inputformatid
    WHERE
        f.brief = 'OkodPO' and f.filltype = 1 and f.separator = ';' '''

filetype_select = '''SELECT
    filltype
FROM
    tenterprise AS e
    INNER JOIN tentformat AS r ON e.enterpriseID=r.EnterpriseID
    INNER JOIN tinputformat AS f ON r.inputformatid = f.inputformatid
    WHERE
        e.code = 9092'''

brief_select = '''SELECT
    brief
FROM
    tenterprise AS e
    INNER JOIN tentformat AS r ON e.enterpriseID=r.EnterpriseID
    INNER JOIN tinputformat AS f ON r.inputformatid = f.inputformatid
    WHERE
        e.code = 9092 '''

ecode_select = '''SELECT
    code
FROM
    tenterprise AS e
    INNER JOIN tentformat AS r ON e.enterpriseID=r.EnterpriseID
    INNER JOIN tinputformat AS f ON r.inputformatid = f.inputformatid
    WHERE
        e.institutionid = 31 '''

ecode_select2 = '''SELECT
    code
FROM
    tenterprise AS e
    INNER JOIN tentformat AS r ON e.enterpriseID=r.EnterpriseID
    INNER JOIN tinputformat AS f ON r.inputformatid = f.inputformatid
    WHERE
        e.institutionid = 24 '''
def read_format(cursor,filetype,code_obpo):
    sql_obpo_format = f'''SELECT
    sysname
FROM
    tenterprise AS e
    INNER JOIN tentformat AS r ON e.enterpriseID=r.EnterpriseID
    INNER JOIN tinputformat AS f ON r.inputformatid = f.inputformatid
    WHERE
        f.filltype = {filetype} and e.code = {code_obpo}'''
    separator = ','
    cursor.execute(sql_obpo_format)
    sysname = cursor.fetchone()
    x = "".join(map(str, sysname))
    x1 = "".join(map(str,separator))
    format_array =  x.split(x1)
    return format_array, separator
'''SELECT
    ksocr,kname,sname,ssocr,dgninmb,socatd,dindex,dcode,dsocr,dname
FROM
    street
	inner JOIN doma ON street.sgninmb = doma.dgninmb  and street.socatd = doma.docatd 
	inner join kladr ON kladr.kgninmb  = doma.dgninmb and  kladr.kocatd = doma.docatd
	where street.sindex is not null and doma.dindex is not null and kladr.kindex is not null and doma.dgninmb is not null and doma.dname != 'двлд66' '''