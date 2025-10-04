from redis import Redis

redis_client = Redis(host="localhost", port=6379, db=0, decode_responses=True)

# 1 - topshiriq

# redis_client.set("name", "Azizbek")
# print(redis_client.get('name'))
# -----------------------------------------------------------------

# 2 - topshiriq

# new_name = redis_client.setnx('name', 'Toxir')
# print(new_name)
# -----------------------------------------------------------------

# 3 - topshiriq

# mavjud key value ni o'zgartirdim

# name = redis_client.setex('name', 30, 'Azizbek')
# redis_client.ttl('name')

# yangi key value yaratib o'shani o'zgartirdim

# age = redis_client.setex('age', 60, '18')
# redis_client.ttl('age')
# -----------------------------------------------------------------

# 4 - topshiriq

# old_name = redis_client.getset('name', 'Toxir')
# print(f"Bu yangi ism: {redis_client.get('name')}\n"
#       f"Bu eski ism: {old_name}")
# -----------------------------------------------------------------

# 5 - topshiriq

# count = redis_client.set('count', '0')
# print(f"Bu eski count: {redis_client.get('count')}")


# incr orqali

# print(f"Bu yangi count: {redis_client.incr('count')}")

# incrby orqali

# print(f"Bu yangi count: {redis_client.incrby('count', 25)}")
# -----------------------------------------------------------------

# 6 -topshiriq

# print(f"Bu eski count: {redis_client.get('count')}")

# decr orqali

# print(f"Bu yangi count: {redis_client.decr('count')}")

# decrby orqali

# print(f"Bu yangi count: {redis_client.decrby('count', 5)}")

# -----------------------------------------------------------------

# 7 - topshiriq

# ttl

# print(f"Natija: {redis_client.ttl('name')}")

# exists

# print(f"Natija: {redis_client.exists('name')}")

# 8 - topshiriq

# mset

# mset = redis_client.mset({
#     'email': 'ahmadjonovazizbek856@gmail.com',
#     'isMarried': 'False',
#     'address': 'Ferghana'
# })

# mget

# print(f"Natija: {redis_client.mget(['email', 'isMarried', 'address'])}")
# -----------------------------------------------------------------

# 9 - topshiriq

# redis_client.append('name', ' Toxirov')
# print(redis_client.get('name'))
# -----------------------------------------------------------------

# 10 - topshiriq

# print(redis_client.getrange('name', 0, -1))
# -----------------------------------------------------------------

# 11 - topshiriq

# print(f"Eski email: {redis_client.get('email')}")
# redis_client.setrange('email', 17, '444@gmail.com')
# print(f"Yangi email: {redis_client.get('email')}")

# -----------------------------------------------------------------

# 12 -topshiriq

# print(f"Natija: {redis_client.delete('count')}")
# -----------------------------------------------------------------

# 13 - topshiriq

# print(f"Eski email: {redis_client.getset('email', 'ahmadjonovazizbek2007@gmail.com')}\n"
#       f"Yangi email: {redis_client.get('email')}")
# -----------------------------------------------------------------

# 14 - topshiriq

# print(f"Email uzunligi: {redis_client.strlen('email')}")

# -----------------------------------------------------------------

# 15 - topshiriq

# print(redis_client.set('name', 'Azizbek Ahmadjonov', nx=True))
# print(redis_client.get('name'))
# -----------------------------------------------------------------

# 16 - topshiriq

# print(f"Eski qiymat: {redis_client.getset('address', 'Tashkent')}\n"
#       f"Yangi qiymat: {redis_client.get('address')}")

# -----------------------------------------------------------------

# 17 - topshiriq

# users = ['Bakir', 'Sobir', 'Ali', 'Vali']
# redis_client.set('users', ", ".join(users))
# print(redis_client.get('users'))

# -----------------------------------------------------------------

# 18 - topshiriq

# print(redis_client.type('name'))

# -----------------------------------------------------------------

# 19 - topshiriq

# print(redis_client.keys('*'))
# print(redis_client.keys('*name'))
# print(redis_client.scan())


redis_client.close()
