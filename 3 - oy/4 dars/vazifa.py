class User:
    objects = []

    def __init__(self, username, password):
        self.validate_username(username)
        self.validate_password(password)
        
        self.username = username
        self.password = password
        User.objects.append(self)

    def validate_username(self, username):
        for user in User.objects:
            if username == user.username:
                raise ValueError("Foydalanuvchi nomi noyob emas! ")
        if not username.isalnum():
            raise ValueError("Foydalanuvchi nomi faqat harflar va raqamlardan iborat bo'lishi kerak")
        if username.count(' ') != 0: 
            raise TabError("Foydalanuvchi nomida joy tashlash mumkin emas! ")

    def validate_password(self, password):
        if len(password) < 8:
            raise ValueError("Parolda 8 ta belgidan kam bo'lmasligi kerak!")
        if not any(c.isalpha() for c in password):
            raise ValueError("Parolda kamida bitta harf bo'lishi kerak!")
        if not any(c.isdigit() for c in password):
            raise ValueError("Parolda kamida bitta raqam bo'lishi kerak")

    def create_account(self):
        while True:
            try:
                username = input("Username kiriting: ")
                password = input("Password kiriting: ")
                new_user = User(username, password)
                print("Account muvaffaqiyatli yaratildi!")
                break
            except ValueError as e:
                print(f"Xatolik: {e}")

    def login(self):
        print('Dasturga kirish')
        username = input('Username: ')
        password = input('Password: ')
        result = False
        for user in User.objects:
            if username == user.username and password == user.password:
                result = True
                break
        if result:
            print('Dasturga xush kelibsiz')
            return True
        else:
            print('Username yoki passwordda xatolik')
            return False

User('testuser', 'testpass123').create_account()

if User.objects:
    user1 = User.objects[0]
    if user1.login():
        print('Siz muvaffaqiyatli kirdingiz!')
