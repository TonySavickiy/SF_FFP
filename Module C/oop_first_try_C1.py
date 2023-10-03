class User():
    def __init__(self, name, email):
        self.name = name
        self.email = email

#Здесь создаём экземпляр

admin = User(email='dgworkmail@yandex.ru')
print(admin.email)