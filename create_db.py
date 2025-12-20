import pymysql
import traceback
from datetime import datetime
from decouple import config

def create_database(db_name):
    try:
        mysql_conn = pymysql.connect(
            host=config("MYSQL_HOST"),
            user=config("MYSQL_USER"),
            password=config("MYSQL_PASS"),
            port=int(config("MYSQL_PORT")),
        )
        cur = mysql_conn.cursor()
        cur.execute("SHOW DATABASES")
        dbs = []
        for i in cur.fetchall():
            dbs += i
        if db_name not in dbs:
            cur.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
            print(f"INFO : {datetime.now()} {db_name} database successfully created...")
        else:
            print(f"ERROR : {datetime.now()} {db_name} database already existed...")
        mysql_conn.close()
    except Exception:
        print(traceback.format_exc())

if __name__ == "__main__":
    create_database(db_name=config("MYSQL_DB"))