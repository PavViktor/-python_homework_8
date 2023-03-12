def all_contacts():
    with open("phonebook.txt", "r") as data:
        for line in data:
            print(line)


def find_contact():
    name = input("Введите фамилию или номер телефона: ")
    with open("phonebook.txt", "r") as data:
        for line in data:
            if name in line:
                return str(line)
            # elif name not in data: print('Отсутствует в справочнике')


def print_contact():
    name = input("Введите фамилию или номер телефона: ")
    with open("phonebook.txt", "r") as data:
        for line in data:
            if name in line:
                print(line)


def add_contact():
    new_contact = str(input("Введите имя и номер телефона: "))
    with open("phonebook.txt", "a", encoding="utf-8") as data:
        data.write("\n")
        data.write(new_contact)


def main_menu():
    user_input = int(
        input(
            "Введите:\n 1 - для печати всего справочника\n 2 - для поиска контакта\n 3 - для записи контакта\n 4 - для удаления контакта\n 5 - для изменения контакта\n 6 - выход\n"
        )
    )
    if user_input == 1:
        all_contacts()
    elif user_input == 2:
        print_contact()
    elif user_input == 3:
        add_contact()
    elif user_input == 4:
        remove_contact()
    elif user_input == 5:
        change_contact()
    elif (
        user_input != 1
        and user_input != 2
        and user_input != 3
        and user_input != 4
        and user_input != 5
    ):
        print("До новых встреч!")


def remove_contact():
    contact = find_contact()
    with open("phonebook.txt", "r", encoding="utf-8") as data:
        new_list = data.readlines()
    for i in range(len(new_list) - 1):
        if contact == new_list[i]:
            new_list.pop(i)
    final_list = "".join(new_list)
    with open("phonebook.txt", "w", encoding="utf-8") as data:
        data.write(f"{final_list}")
        print("Запись удалена")


def change_contact():
    contact = find_contact()
    with open("phonebook.txt", "r", encoding="utf-8") as data:
        new_list = data.readlines()
    for i in range(len(new_list) - 1):
        if contact == new_list[i]:
            new_contact = str(input("Введите новые данные контакта: ") + "\n")
            new_list[i] = new_contact
    final_list = "".join(new_list)
    with open("phonebook.txt", "w", encoding="utf-8") as data:
        data.write(f"{final_list}")
        print("Контакт изменён")


main_menu()
