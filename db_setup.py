import pymysql
import dbconfig

connection = pymysql.connect(host='localhost',
                             user=dbconfig.db_user,
                             passwd=dbconfig.db_password)

db_sql = 'CREATE DATABASE IF NOT EXISTS crimemap'

tbl_sql = '''CREATE TABLE IF NOT EXISTS crimemap.crimes (
               id int NOT NULL AUTO_INCREMENT,
               latitude FLOAT(10,6),
               longitude FLOAT(10,6),
               date DATETIME,
               category VARCHAR(50),
               description VARCHAR(1000),
               updated_at TIMESTAMP,
               PRIMARY KEY (id)
               )'''

try:
    with connection.cursor() as cursor:
        print("Creating crimemap database")
        cursor.execute(db_sql)
        print("Creating crimes table")
        cursor.execute(tbl_sql);
    connection.commit()
finally:
    print("Closing database connection")
    connection.close()
