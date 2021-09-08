"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def hello_user():
    input_string = input("Как дела? ")
    while input_string != 'хорошо':
        input_string = input("Ну так не пойдет. Давай еще раз! Как дела? ")


if __name__ == "__main__":
    hello_user()
