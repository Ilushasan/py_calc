class Calculator: #Класс калькулятор
    def __init__(self):
        print("Welcome to my calculator")
        print("----------------------------------------")
    # Функция выбора арифметичской операции
    def choice(self):
        choice = input("What calculation do u choice: \n 1. Addition + \n 2. Subtraction - \n 3. Multiplication * \n 4. Division / \n 5. Exponention ** \n 6. '\u221a' \n 7. Exit \n")
        choice_lower = choice.lower() # Приведение к нижнему регистру
        # Проверка  и запуск соответствующей функции
        if choice_lower == '1':
            first_num = input("Enter a first number: ") # Первое число
            second_num = input("Enter a second number: ") # Второе число
            # Обработка ошибки сложения строк
            try:
                first_num_float = float(first_num) # Первое число
                second_num_float = float(second_num) # Второе число
                self.add(first_num_float, second_num_float) # Запуск функции для расчета
            except:
                print('----------- \n Cant calc string\n-----------') # Вывод ошибки
                self.choice() # Запуск выбора арифметической операции
        elif choice_lower == '2':
            first_num = input("Enter a first number: ") # Первое число
            second_num = input("Enter a second number: ") # Второе число
            # Обработка ошибки сложения строк
            try:
                first_num_float = float(first_num) # Первое число
                second_num_float = float(second_num) # Второе число
                self.sub(first_num_float, second_num_float) # Запуск функции для расчета
            except:
                print('----------- \n Cant calc string\n-----------') # Вывод ошибки
                self.choice() # Запуск выбора арифметической операции
        elif choice_lower == '3':
            first_num = input("Enter a first number: ") # Первое число
            second_num = input("Enter a second number: ") # Второе число
            # Обработка ошибки сложения строк
            try:
                first_num_float = float(first_num) # Первое число
                second_num_float = float(second_num) # Второе число
                self.mul(first_num_float, second_num_float) # Запуск функции для расчета
            except:
                print('----------- \n Cant calc string\n-----------') # Вывод ошибки
                self.choice() # Запуск выбора арифметической операции
        elif choice_lower == '4':
            first_num = input("Enter a first number: ") # Первое число
            second_num = input("Enter a second number: ") # Второе число
            # Обработка ошибки сложения строк
            try:
                first_num_float = float(first_num) # Первое число
                second_num_float = float(second_num) # Второе число
                self.dev(first_num_float, second_num_float) # Запуск функции для расчета
            except:
                print('----------- \n Cant calc string\n-----------') # Вывод ошибки
                self.choice() # Запуск выбора арифметической операции
        elif choice_lower == '5':
            first_num = input("Enter a first number: ") # Первое число
            second_num = input("Enter a second number: ") # Второе число
            # Обработка ошибки сложения строк
            try:
                first_num_float = float(first_num) # Первое число
                second_num_float = float(second_num) # Второе число
                self.exponent(first_num_float, second_num_float) # Запуск функции для расчета
            except:
                print('----------- \n Cant calc string\n-----------') # Вывод ошибки
                self.choice() # Запуск выбора арифметической операции
        elif choice_lower == '6':
            first_num_float = input("Enter a first number: ") # Первое число
            # Обработка ошибки сложения строк
            try:
                first_num_float = float(first_num_float) # Первое число
                self.square_root(first_num_float) # Запуск функции для расчета
            except:
                print('----------- \n Cant calc string\n-----------') # Вывод ошибки
                self.choice() # Запуск выбора арифметической операции
        elif choice_lower == '7':
            print('----------- \n Exit\n-----------') # Завершение работы программы
        else:
            print("----------- \n Incorrect choice. Try again.\n-----------")
            self.choice() # Запуск выбора арифметической операции   
    # Фунция сложения
    def add(self, first_num, second_num):
        answer = first_num + second_num
        print("----------- \n" + str(first_num) + " + " + str(second_num) +  " = " + str(answer) + "\n-----------")
        self.choice() # Запуск выбора арифметической операции
    # Фунция вычитания
    def sub(self, first_num, second_num):
        answer = first_num - second_num
        print("----------- \n" + str(first_num) + " - " + str(second_num) +  " = " + str(answer) + "\n-----------")
        self.choice() # Запуск выбора арифметической операции
    # Фунция умножения
    def mul(self, first_num, second_num):
        answer = first_num * second_num
        print("----------- \n" + str(first_num) + " * " + str(second_num) +  " = " + str(answer) + "\n-----------")
        self.choice() # Запуск выбора арифметической операции
    # Фунция деления
    def dev(self, first_num, second_num):
        if second_num == 0: # Обработка ошибки при делении на 0
            print("Сan't divide by zero")
            self.choice() # Запуск выбора арифметической операции
        else:
            answer = first_num / second_num
            print("----------- \n" + str(first_num) + " / " + str(second_num) +  " = " + str(answer) + "\n-----------")
            self.choice() # Запуск выбора арифметической операции
    # Фунция возведения в степень
    def exponent(self, first_num, second_num):
        answer = first_num ** second_num
        print("----------- \n" + str(first_num) + " ** " + str(second_num) +  " = " + str(answer) + "\n-----------")
        self.choice() # Запуск выбора арифметической операции
    # Фунция извлечения квадратного корня
    def square_root(self, first_num):
        print('sad')
        s = u'\u221a' # Символ квадратного корня
        answer = first_num ** 0.5
        print("----------- \n" + f"{s}{str(first_num)}" +  " = " + str(answer) + "\n-----------")
        self.choice() # Запуск выбора арифметической операции

calc = Calculator() # Инициализация класса
calc.choice() # Вызова функции для выбора арифметической оперции
