''' Задача_1(49). Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.

1. Программа должна выводить данные

2. Программа должна сохранять данные в текстовом файле

3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию
человека)

4. Использование функций. Ваша программа не должна быть линейной

Решение:

1. Создать файл для записи телефонной книги.
    • открытие файла на дозапись.

2. Подготовка меню для пользователя.

3. Запись данных в файл по каждому контакту:
    • ввод данных пользователя,
    • подготовка данных для записи в файл,
    • открытие файла в режиме дозаписи,
    • запись новой строки с данными

4. Чтение данных из файла:
    • открытие файла в режиме чтения,
    • считать все данные и вывести их на экран.

5. Поиск записей по параметрам и вывод соответствующих данных
    • ввод пользователем параметра поиска,
    • открыть файл в режиме чтения,
    • считать все данные из файла и сохранить их в программе,
    • сделать выборку нужной записи - сам поиск,
    • показать результат поиска. '''

'''Домашняя работа:
Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и 
удаления данных. '''

def input_name():
    return input("Введите имя контакта: ")


def input_surname():
    return input("Введите фамилию контакта: ")


def input_patronymic():
    return input("Введите отчетство контакта: ")


def input_phone():
    return input("Введите телефон контакта: ")


def input_adress():
    return input("Введите адрес контакта: ")


def input_data():
    surname = input_surname()
    name = input_name()
    patronymic = input_patronymic()
    phone = input_phone()
    adress = input_adress()
    str_contact = f"{surname} {name} {patronymic} {phone}\n{adress}\n\n"
    with open("phonebook.txt", "a", encoding="UTF-8") as file:
        file.write(str_contact)


def read_file():
    with open("phonebook.txt", "r", encoding="UTF-8") as file:
        return file.read()


def print_data():
    print(read_file())


def search_contact():
    print("Варианты для поиска:\n"
          "1.Фамилия\n"
          "2.Имя\n"
          "3.Отчество\n"
          "4.Телефон\n"
          "5.Адрес")
    command = input("Укажите вариант поиска: ")
    while command not in ("1", "2", "3", "4", "5"):
        print("Некорректный ввод номера варианта!\n"
              "Повторите ввод")
        command = input("Укажите номер варианта: ")
    print()
    i_search_param = int(command) - 1
    search = input("Введите данные для поиска: ").title()
    contacts_list = read_file().rstrip().split("\n\n")
    # print(contacts_list)

    for contact_str in contacts_list:
        contact_lst = contact_str.replace("\n", " ").split()
        # print(contact_lst)
        if search in contact_lst[i_search_param]:
            print(contact_str + "\n")


def change_contact():
    print("Варианты для изменения:\n"
          "1.Фамилия\n"
          "2.Имя\n"
          "3.Отчество\n"
          "4.Телефон\n"
          "5.Адрес")
    command = input("Укажите вариант изменения: ")
    while command not in ("1", "2", "3", "4", "5"):
        print("Некорректный ввод номера варианта!\n"
              "Повторите ввод")
        command = input("Укажите номер варианта: ")
    # print()
    i_change_param = int(command) - 1
    search = input("Введите данные для поиска: ").title()
    contacts_list = read_file().rstrip().split("\n\n")
    # print(contacts_list)
    new_contacts_list = []
    for contact_str in contacts_list:
        contact_lst = contact_str.replace("\n", " ").split()
        # print(contact_lst)
        if search in contact_lst[i_change_param]:
            new_contact_lst = contact_lst
            new_contact_lst[i_change_param] = input(f"Введите новые данные для изменения {contact_lst[i_change_param]}: ")
            new_contacts_list.append(" ".join(new_contact_lst))
            print()
        else:
            new_contacts_list.append(contact_str)
    with open("phonebook.txt", "w", encoding="UTF-8") as file:
        for contact_str in new_contacts_list:
            file.write(contact_str + "\n\n")


def delete_contact():
    print("Варианты для удаления:\n"
          "1.Фамилия\n"
          "2.Имя\n"
          "3.Отчество\n"
          "4.Телефон\n"
          "5.Адрес")
    command = input("Укажите вариант удаления: ")
    while command not in ("1", "2", "3", "4", "5"):
        print("Некорректный ввод номера варианта!\n"
              "Повторите ввод")
        command = input("Укажите номер варианта: ")
    print()
    i_delete_param = int(command) - 1
    search = input("Введите данные для поиска: ").title()
    contacts_list = read_file().rstrip().split("\n\n")
    # print(contacts_list)
    new_contacts_list = []
    for contact_str in contacts_list:
        contact_lst = contact_str.replace("\n", " ").split()
        # print(contact_lst)
        if search not in contact_lst[i_delete_param]:
            new_contacts_list.append(contact_str)
    with open("phonebook.txt", "w", encoding="UTF-8") as file:
        for contact_str in new_contacts_list:
            file.write(contact_str + "\n\n")


def interface():
    with open("phonebook.txt", "a", encoding="UTF-8"):
        pass
    command = ""
    while command != "6":
        print("Выберите вариантработы с телефонной книгой:\n"
              "1.Запись данных\n"
              "2.Вывод телефонной книги на экран\n"
              "3.Поиск данных\n"
              "4.Изменение данных\n"
              "5.Удаление данных\n"
              "6.Выход")
        command = input("Введите номер операции: ")
        while command not in ("1", "2", "3", "4", "5", "6"):
            print("Некорректный ввод номера операции!\n"
                  "Повторите ввод")
            command = input("Введите номер операции: ")
        print()

        match command:
            case "1":
                input_data()
            case "2":
                print_data()
            case "3":
                search_contact()
            case "4":
                change_contact()
            case "5":
                delete_contact()
            case "6":
                print("Приложение закрыто!")

if __name__ == '__main__':
    interface()