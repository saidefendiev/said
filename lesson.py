import sqlite3

db = sqlite3.connect('server.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS users (
    name TEXT,
    Lastname TEXT,
    Age TEXT,
    work TEXT

)""")

db.commit()

user_name = input('name: ')
user_Lastname = input('Last name: ')
user_age = input('Age: ')
user_work = input('work: ')

user_name = input('name: ')
user_Lastname = input('Last name: ')
user_age = input('Age: ')
user_work = input('work: ')

user_name = input('name: ')
user_Lastname = input('Last name: ')
user_age = input('Age: ')
user_work = input('work: ')

user_name = input('name: ')
user_Lastname = input('Last name: ')
user_age = input('Age: ')
user_work = input('work: ')

user_name = input('name: ')
user_Lastname = input('Last name: ')
user_age = input('Age: ')
user_work = input('work: ')
db.commit

sql.execute("SELECT * FROM users")
if sql.fetchone() is None:
    db.commit()
    print('5 пользователей - зарегистрированы')
else:
    print('Такой пользователь уже имеется')