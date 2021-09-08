"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""
input_data = [
    {'input1': 0, 'input2': 0},
    {'input1': 'Test string 1', 'input2': 0},
    {'input1': 0, 'input2': 'Test string 2'},
    {'input1': 'Test string', 'input2': 'Test string'},
    {'input1': 'Test string long', 'input2': 'Test string'},
    {'input1': 'Test string', 'input2': 'learn'},
    {'input1': 'Test string', 'input2': 'Test string long'},
    {'input1': 1.0, 'input2': 1},
    {'input1': [1], 'input2': [0]}
]


def get_data_from_input(value1, value2):
    for value in (value1, value2):
        if not isinstance(value, str):
            return 0
    if value1 == value2:
        return 1
    if len(value1) > len(value2) and value2 != 'learn':
        return 2
    if value2 == 'learn':
        return 3
    else:
        return 'Not defined case'


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    for iteration in input_data:
       print(get_data_from_input(iteration['input1'], iteration['input2']))


if __name__ == "__main__":
    main()
