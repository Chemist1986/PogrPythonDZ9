import csv
import json
import math
import random


def find_quadratic_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None  
    elif discriminant == 0:
        root = -b / (2*a)
        return (root,)
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return (root1, root2)


def generate_csv_file(filename, num_rows):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        for _ in range(num_rows):
            row = [random.random() for _ in range(3)]
            writer.writerow(row)


def with_csv_quadratic_roots(func):
    def wrapper(filename):
        with open(filename, newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) != 3:
                    continue  
                a, b, c = map(float, row)
                roots = func(a, b, c)
                print(f"Уравнение: {a}x^2 + {b}x + {c} = 0, Корни: {roots}")
    return wrapper


def save_to_json(func):
    def wrapper(*args):
        result = func(*args)
        data = {
            "args": args,
            "result": result
        }
        with open('results.json', 'a') as file:
            json.dump(data, file)
            file.write('\n')
        return result
    return wrapper


def main():
    while True:
        print("Выберите опцию:")
        print("1. Найти корни квадратного уравнения")
        print("2. Сгенерировать CSV файл с тремя случайными числами в каждой строке")
        print("3. Запустить функцию нахождения корней с каждой тройкой чисел из CSV файла и сохранить результаты в JSON файле")
        print("4. Выход")
        
        choice = input()

        if choice == '1':
            a = float(input("Введите коэффициент a: "))
            b = float(input("Введите коэффициент b: "))
            c = float(input("Введите коэффициент c: "))
            roots = find_quadratic_roots(a, b, c)
            print(f"Корни уравнения: {roots}")

        elif choice == '2':
            num_rows = int(input("Введите количество строк в CSV файле: "))
            generate_csv_file("random_numbers.csv", num_rows)
            print("Файл 'random_numbers.csv' успешно создан.")

        elif choice == '3':
            filename = input("Введите имя CSV файла: ")
            with_csv_roots_decorator = with_csv_quadratic_roots(find_quadratic_roots)
            with_csv_roots_decorator(filename)

            filename = input("Введите имя CSV файла для сохранения результатов: ")
            with_csv_roots_decorator = with_csv_quadratic_roots(save_to_json(find_quadratic_roots))
            with_csv_roots_decorator(filename)

        elif choice == '4':
            print("Выход.")
            break
        else:
            print("Ошибка: выбрана неверная опция.")

if __name__ == "__main__":
    main()