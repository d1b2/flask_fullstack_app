
import pymysql
import json

def get_db_credentials():
    with open('secrets/db_secrets.json') as secret:
        db_info=json.load(secret)
    return db_info

keys=get_db_credentials()

#print(keys)
#print(type(keys))

conn = pymysql.connect(host="localhost",user=keys['db_super_user_key'],password=keys['db_super_user_pswd'])

cursor=conn.cursor()

cursor.execute(f"CREATE DATABASE IF NOT EXISTS {keys['new_db']};")
print("New database created.")

cursor.execute(f"CREATE USER '{keys['new_user_key']}'@'%' IDENTIFIED by '{keys['new_user_pswd_key']}';")
print("New User created.")

cursor.execute(f"GRANT ALL PRIVILEGES ON {keys['new_db']}.* TO {keys['new_user_key']}@'%';")
print("Priveleges granted to new user.")

conn.commit()
print("Queries commited.")

cursor.close()

conn.close()