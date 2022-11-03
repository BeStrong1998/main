"""Создаём файл create_admin.py который поможет нам из командной строки пользователя дабовлять"""

from getpass import getpass # Не видно в командной строке что печат пользователь (Для вода пароля)
import sys # Этот модуль нужен для того что бы правельно завершать наш скрипт

from webapp import create_app
from webapp.model import db, User

app = create_app() #Создаём апликейшен

with app.app_context(): # Доступ к базе данных
    username = input('Введите имя:') # Запрашиваем username в командной строке

    if User.query.filter(User.username == username).count(): #Проверяем что такой пользователь существует
        print('Пользователь с таким именем уже существует') # Если такой пользователь существует печатаем: 'Пользователь с таким именем уже существует'
        sys.exit(0) #Выходим из программы

    password1 = getpass('Введите пароль') # метод getpass делает вводимый пароль невидимым. Просим пользователя ввести 2 раза пароль 
    password2 = getpass('Повторите пароль')

    if not password1 == password2: #Проверяем что пароли равны
        print('Пароли не одинаковые') #Если пароли не равны пишем ошибку: 'Пароли не одинаковые'
        sys.exit(0) # Выходим из программы


    """Если проверки прошли то можем создавать пользователя"""
    new_user = User(username=username, role='admin') #Создаём объект пользователя
    new_user.set_password(password1) #Создаём пароль, превращаем пароль в зашифрованную строку при помощи функции set_password

    db.session.add(new_user) #Фуиксируем пользователя
    db.session.commit() #Сохраняем пользователя
    print('Создан пользоваткль с id={}'.format(new_user.id)) # Отображаем в командной строке

    
