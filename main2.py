from peewee import MySQLDatabase,BooleanField,  CharField, DateTimeField,  Model
from datetime import datetime
import time
HOST = "localhost"
USER = "root"
PASSWORD = ""
DATABASE= "prueba"
db = MySQLDatabase(DATABASE, host=HOST, port=3306, user=USER, passwd=PASSWORD)
class User(Model):
    username =  CharField(unique=True, max_length=50, index=True)
    password = CharField(max_length=50)
    email = CharField(max_length=50, null=True)
    active = BooleanField(default=True)
    created_date = DateTimeField(default=datetime.now)
    class Meta:
        database = db
def on():
    db.connect()
    print("[+]conexion establecida...")
    print("[=]agregando tabla...")
    print([User])
    time.sleep(2)
def create_table():
    db.create_tables([User])
    time.sleep(5)
def of():
    db.close()
    print("[-]conexion finalizada...")
def  insert_date():
    user = User()
    user.username = str(input("[+]digite un usuario: "))
    user.password = str(input("[+]digite una contraseña: "))
    user.email = str(input("[+]digite un correo electronico: "))
    user.save()
    print("[=]datos guardados en la tabla", [User])
on()
create_table()
insert_date()
of()