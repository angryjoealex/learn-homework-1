"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""
school = [ 
    {'school_class': '4a', 'scores': [3, 4, 4, 5, 2]},
    {'school_class': '4b', 'scores': [5, 4, 1, 5, 4]},
    {'school_class': '4c', 'scores': [1, 3, 1, 2, 4]}
]


def avg_school():
    total = 0
    counter = 0
    for score in school:
        total += sum(score['scores'])
        counter += len(score['scores']) 
    return f"School avg is {total/counter}"


def avg_class():
    answer = ''
    for score in school:
        answer += f"Class {score['school_class']} avg is {sum(score['scores'])/len(score['scores'])} \n"
    return answer


def main():
    print(avg_school())
    print(avg_class())


if __name__ == "__main__":
    main()
