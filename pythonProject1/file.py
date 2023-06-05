import case1
import Connection_to_postgresql
from Ofile_create import file_name, file_gen
connection = Connection_to_postgresql.create_connection(
    "postgres", "postgres", "mayday", "127.0.0.1", "5432"
)
def gen_file_case1(cursor,code_OBPO,filetype,count):
    filename,sfilename = file_name(code_OBPO)
    file_gen(filetype,cursor,filename,case1,code_OBPO,count,"case1")
gen_file_case1(connection.cursor(), '9092','1',100)