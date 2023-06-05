import pytest
import case1
from Ofile_create import file_name, file_gen
import psycopg2
from psycopg2 import OperationalError
import Connection_to_postgresql
connection = Connection_to_postgresql.create_connection(
    "postgres", "postgres", "mayday", "127.0.0.1", "5432"
)
name = 'postgres'
user = 'postgres'
password = "mayday"
host = "127.0.0.1"
port = "5432"
def pytest_adoption(parser):
    parser.addoption('--db', action ="store", default =name, help='db')
    parser.addoption('--user', action="store", default=user, help='user')
    parser.addoption('--password', action="store", default=password, help='password')
    parser.addoption('--host', action="store", default=host, help='host')
    parser.addoption('--port', action="store", default=port, help='port')
@pytest.fixture (scope="session")
def cursor():
    '''name = request.config.getoption('--db')
    user = request.config.getoption('--user')
    password = request.config.getoption('--password')
    host = request.config.getoption('--host')
    port = request.config.getoption('port')
    connection = Connection_to_postgresql.create_connection(
        name,user,password,host,port)'''
    connection = Connection_to_postgresql.create_connection(
        "postgres", "postgres", "mayday", "127.0.0.1", "5432"
    )
    cursor = connection.cursor()
    return cursor
@pytest.mark.files
@pytest.mark.case1
def test_gen_file_case1(cursor,code_OBPO,filetype,count):
    filename,sfilename = file_name(code_OBPO)
    file_gen(filetype,cursor,filename,case1,code_OBPO,count,"case1")
    
