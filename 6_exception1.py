"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def hello_user():
    try:
        str=input("Как дела?")
        #return str
        while str != 'хорошо':
            try:
                str=input("Ну так не пойдет. Давай еще раз! Как дела? ")
                if str == 'хорошо':
                    print("Ну наконец то у тебя все наладилось! Пока")
            except KeyboardInterrupt:
                print(f"\nПока")
                break                  
    except KeyboardInterrupt: ## Достаточно этой проверки, но по заданию надо через while break,так что см выше
        print(f"\nПока")    
    
    
if __name__ == "__main__":
    hello_user()
