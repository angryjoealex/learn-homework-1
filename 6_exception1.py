"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""


def hello_user():
    input_string = input("Как дела?")
    while input_string != 'хорошо':
        try:
            input_string = input("Ну так не пойдет. Давай еще раз! Как дела? ")
        except KeyboardInterrupt:
            print("\nПока")
            break
        if input_string == 'хорошо':
            print("Ну наконец то у тебя все наладилось! Пока")


if __name__ == "__main__":
    try:
        hello_user()
    except KeyboardInterrupt:
        print("\nПока")
