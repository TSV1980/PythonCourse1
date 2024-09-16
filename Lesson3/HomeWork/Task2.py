#2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Осуществить вывод данных о пользователе одной строкой.

def get_use_info(name, surname, birthday, city, email, phone_number):
    """Функция принимает несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
       Именованные параметры:
       name -- имя
       surname -- фамилия
       birthday -- год рождения
       email -- e-mail
       phone_number -- номер телефона
       """
    print(f' {surname} {name}. Год рождения:{birthday}. Проживает в г.{city}. EMail:{email}. Телефон:{phone_number}')

#ввод данных пользователя
print('--- Ввод данных пользователя ---')
user_name = input('Введите имя:')
user_surname = input('Введите фамилию:')
user_birthday= input('Введите дату рождения:')
user_city = input('Введите город проживания:')
user_email = input('Введите email:')
user_phone_number = input('Введите телефон:')

#вывод информации на экран
get_use_info(name=user_name,
             surname=user_surname,
             birthday=user_birthday,
             city=user_city,
             email=user_email,
             phone_number=user_phone_number)

