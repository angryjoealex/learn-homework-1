"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""
age_place = [
        {'place': 'Детскому саду', 'min_age': 1, 'max_age': 6},
        {'place': 'Школе', 'min_age': 7, 'max_age': 18},
        {'place': 'ВУЗу', 'min_age': 19, 'max_age': 24},
        {'place': 'Работе', 'min_age': 25, 'max_age': 70}
    ]


def check_age(user_age):
    try:
        user_age = float(user_age)
    except ValueError:
        print('Вы ввели не цифру! Попробуйте снова')
        return True
    else:
        if user_age <= 0:
            print('Возраст должен быть больше 0. Попробуйте снова')
            return True
        elif user_age >= 130:
            print('Вы должны быть мертвы')
            return False
        elif 70 <= user_age < 130:
            print('Вы на пенсии')
            return False
        else:
            for place in age_place:
                if place['min_age'] <= user_age <= place['max_age']:
                    print(f'Ваш возраст {user_age} который соответсвует {place["place"]}')
                    return False


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    while True:
        user_age = input('Пожалуйста введите свой возраст: ')
        return_code = check_age(user_age)
        if return_code is False:
            break


if __name__ == "__main__":
    main()
