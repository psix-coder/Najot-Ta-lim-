class User:
    objects = []
    def __init__(self, username, password):
        self.validate_username(username)
        self.validate_password(password)

        User.objects.append(self)
        self.username = username
        self.password = password

    def validate_username(self, username):
        for user in User.objects:
            if username == user.username:
                raise ValueError("Foydalanuvchi nomi noyob emas! ")
        if not username.isalnum():
            raise ValueError("Foydalanuvchi nomi faqat harflar va raqamlardan iborat bo'lishi kerak")
    def create_account(self,password):
        while True:
            try:
                username = input("Username kirting: ")
                password = input("Password kirting: ")
                User(username, password)
                if len(password ) < 8:
                    raise ValueError("Siz kiritgan Parolda 8 ta belgidan kamaymasligi kerak! ")
                if not password.search("[a-zA-Z]", password):
                    raise ValueError("Parolda kamida bitta harf bo'lishi kerak! ")
                if not password.search("[0-9]", password):
                    raise ValueError("Parolda kamida bitta son bo'lishi kerak")
                break
            except ValueError as e:
                print(f"Xatolik: {e}")
                print("Account muvaffaqiyatli yaratildi!")


    
def login(self):
            print('Dasturga kirish')
            username = input('username: ')
            password = input('password: ')
            result = False
            for user in User.objects:
                if username == user.username and password == user.password:
                    result = True
                    break
            if result:
                print('Dasturga xush kelibsiz')
            else:
                print('Usename yoki passwordda xatolik')


if User.objects:
    user1 = User.objects[0]
    if user1.login():
        print('Siz muvaffaqiyatli kirdingiz!')
