import os
"""
create task
delete task
change task
"""

def create_task():
    file_name = 'tasks.txt'
    task = input("Введите задание: ")
    if not os.path.exists(file_name):
        with open(file_name, 'w', encoding="utf-8") as file:
            file.write(f'{task}\n')
    else:
        with open(file_name, '+a', encoding="utf-8") as file:
            file.write(f'{task}\n')

def change_task():
    file_name = 'tasks.txt'

    if not os.path.exists(file_name):
        print("Файл не найден")
        return

    with open(file_name, 'r', encoding='utf-8') as file:
        tasks = file.readlines()

    if len(tasks) == 0:
        print("Список задач пуст")
        return

    print("\nСписок задач:")
    for i in range(len(tasks)):
        print(f"{i + 1}. {tasks[i].strip()}")

    num = int(input("Введите номер задачи для изменения: "))

    if num < 1 or num > len(tasks):
        print("Неверный номер")
        return

    new_task = input("Введите новое описание: ")

    tasks[num - 1] = new_task + "\n"

    with open(file_name, 'w', encoding='utf-8') as file:
        file.writelines(tasks)

    print("Задача изменена")

def delete_task():
    file_name = 'tasks.txt'

    if not os.path.exists(file_name):
        print("Файл не найден")
        return

    with open(file_name, 'r', encoding='utf-8') as file:
        tasks = file.readlines()

    if len(tasks) == 0:
        print("Список задач пуст")
        return

    print("\nСписок задач:")
    for i in range(len(tasks)):
        print(f"{i + 1}. {tasks[i].strip()}")

    num = int(input("Введите номер задачи для удаления: "))

    if num < 1 or num > len(tasks):
        print("Неверный номер")
        return

    tasks.pop(num - 1)

    with open(file_name, 'w', encoding='utf-8') as file:
        file.writelines(tasks)

    print("Задача удалена")

