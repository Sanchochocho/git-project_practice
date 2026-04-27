from utils import *

while True:
    print("1 - Добавить задание\n2 - Изменить задание\n3 - Удалить\n0 - Выйти")
    choice = input("Выберите пункт: ")
    if choice == "1":
        create_task()
    elif choice == "2":
        change_task()
    elif choice == "3":
        delete_task()
    elif choice == "0":
        print("Завершение...")
        break
    else:
        print("Неверный ввод")
    