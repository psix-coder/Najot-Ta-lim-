import psycopg2
from colorama import Fore
from redis import Redis


def connect(sql, *args, fetchone=False, fetchall=True):
    db = psycopg2.connect(
        user='postgres',
        dbname='instagram',
        password='1',
        host='localhost'
    )

    cursor = db.cursor()

    cursor.execute(sql, args)

    result = None
    if fetchone:
        result = cursor.fetchone()
    elif fetchall:
        result = cursor.fetchall()

    db.commit()
    db.close()

    return result


def get_number_of_friends(user_id):

    redis_user = Redis(decode_responses=True)

    user = redis_user.get(f"user_{user_id}")

    if not user:
        print(Fore.GREEN +  "PostgreSql ma'lumotlar omboriga so'rov yuborilmoqda...")
        sql = '''SELECT users.userId, users.fullName, count(*) FROM users JOIN friends ON 
        users.userId = friends.user_id WHERE users.userId = %s GROUP BY users.userId;'''
        user = connect(sql, user_id, fetchone=True)
        redis_user.setex(f"user_{user_id}", 60, str(user))

    redis_user.close()
    return user


print(get_number_of_friends(3))
