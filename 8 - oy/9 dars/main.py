import time
import requests
import psycopg2
from colorama import Fore
from tabulate import tabulate

ATTEMPTS = 3
WAIT_TIME = 3


def connect():
    db = psycopg2.connect(
        user='postgres',
        dbname="news",
        password='1',
        host='db',
        port='5432'
    )
    return db

for i in range(ATTEMPTS):
    count = 1
    try:
        connect()
        break
    except Exception as e:
        print(Fore.RED + f"Ma'lumotlar omboriga ulanishning {count} - urinishida xatolik yuz berdi: {e}")
        time.sleep(WAIT_TIME)
        count += 1

db = connect()
cursor = db.cursor()

print(Fore.GREEN + "Ma'lumotlar omboriga muvaffaqiyatli tarzda ulanildi!")

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS posts(
        id SERIAL PRIMARY KEY,
        userID INTEGER NOT NULL,
        title VARCHAR(200) NOT NULL,
        body TEXT NOT NULL 
    )'''
)

response = requests.get("https://jsonplaceholder.typicode.com/posts")

if response.status_code == 200:
    data = response.json()
    posts_list = []
    for i in data:
        posts_list.append((i['userId'], i['title'], i['body']))

    cursor.executemany('''
        INSERT INTO posts (userID, title, body) VALUES (%s, %s, %s)''', posts_list)

    db.commit()
    cursor.execute("SELECT * FROM posts ORDER BY id;")
    posts = cursor.fetchall()

    headers = ["ID", "UserID", "Title", "Body"]

    print(Fore.BLUE + tabulate(posts, headers=headers, tablefmt="fancy_grid", rowalign="middle"))

    print(Fore.GREEN + "API dan olingan ma'lumotlar muvaffaqiyatli tarzda ma'lumotlar omboriga saqlandi!")
db.close()