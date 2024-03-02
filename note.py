import datetime

# Путь к файлу для хранения заметок
file_name = 'notes.csv'

# Выбор действий с заметками
def choose_action(notes):
    while True:
        print('Вы открыли приложение "Заметки"! Что вы хотите сделать?')
        user_choice = input('1 - Добавить заметку\n2 - Найти заметку\n3 - Изменить заметку\n4 - Удалить заметку\n5 - Просмотреть все заметки\n0 - Выйти из приложения\n')
        print()
        if user_choice == '1':
            add_note(notes)
        elif user_choice == '2':
            contact_list = read_file_to_dict(notes)
            find_note(contact_list)
        elif user_choice == '3':
            change_note(notes)
        elif user_choice == '4':
            delete_note(notes)
        elif user_choice == '5':
            show_notes(notes)
        elif user_choice == '0':
            print('Работа с приложением "Заметки" завершена!')
            break
        else:
            print('Введено некорректно число! Повторите ввод\n')
            print()
            continue

def read_file_to_dict(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    headers = ['id', 'Заголовок заметки', 'Текст тела заметки']
    note_list = []
    for line in lines:
        line = line.strip().split()
        note_list.append(dict(zip(headers, line)))
    return note_list


def read_file_to_list(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        note_list = []
        for line in file.readlines():
            note_list.append(line.split())
    return note_list

# Поиск заметок по заданным параметрам
def search_parameters():
    print('По какому полю выполнить поиск?')
    search_field = input('1 - По id заметки\n2 - По заголовку заметки\n')
    print()
    search_value = None
    if search_field == '1':
        search_value = input('Введите id заметки для поиска: ')
        print()
    elif search_field == '2':
        search_value = input('Введите заголовок заметки для поиска: ')
        print()
    return search_field, search_value


def find_note(note_list):
    search_field, search_value = search_parameters()
    search_value_dict = {'1': 'id', '2': 'Заголовок заметки'}
    found_notes = []
    for note in note_list:
        if note[search_value_dict[search_field]] == search_value:
            found_notes.append(note)
    if len(found_notes) == 0:
        print('Заметка не найдена!')
    else:
        print_notes(found_notes)
    print()

# Добавление новой заметки
def get_new_note():
    id = input('Введите id заметки: ')
    name_note = input('Введите заголовок заметки: ')
    body_note = input('Введите текст тела заметки: ')
    timestamp = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    return id, name_note, body_note, timestamp


def add_note(file_name):
    info = ' '.join(get_new_note())
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(f'{info}\n')
    print('Заметка сохранена!\n')

# Отображение списка заметок
def show_notes(file_name):
    list_of_notes = sorted(read_file_to_dict(file_name), key=lambda x: x['id'])
    if len(list_of_notes) == 0:
        print('Сохраненных заметок не найдено!\n')
    else:
        print_notes(list_of_notes)
        print('Сохраненные заметки\n')
    return list_of_notes

# Редактирование заметки
def search_to_modify_note(notes_list: list):
    search_field, search_value = search_parameters()
    search_result = []
    for note in notes_list:
        if note[int(search_field) - 1] == search_value:
            search_result.append(note)
    if len(search_result) == 1:
        return search_result[0]
    
    elif len(search_result) > 1:
        print('Найдено несколько заметок')
        for i in range(len(search_result)):
            print(f'{i + 1} - {search_result[i]}')
        num_count = int(input('Выберите id заметки, которую нужно изменить/удалить: '))
        return search_result[num_count - 1]
    else:
        print('Заметка не найдена! \n')
        
    print()

# Изменение содержания заметки
def change_note(file_name):
    note_list = read_file_to_list(file_name)
    number_to_change = search_to_modify_note(note_list)
    note_list.remove(number_to_change)
    print('Какое поле заметки вы хотите изменить?')
    field = input('1 - id\n2 - Заголовок заметки\n3 - Текст тела заметки\n')
    if field == '1':
        number_to_change[0] = input('Введите новый id заметки: ')
    elif field == '2':
        number_to_change[1] = input('Введите новый заголовок заметки: ')
    elif field == '3':
        number_to_change[2] = input('Введите новый текст тела заметки: ')
    note_list.append(number_to_change)
    with open(file_name, 'w', encoding='utf-8') as file:
        for note in note_list:
            line = ' '.join(note) + '\n'
            file.write(line)
    print('Заметка изменена и сохранена! \n')

# Удаление заметки
def delete_note(file_name):
    note_list = read_file_to_list(file_name)
    number_to_change = search_to_modify_note(note_list)
    note_list.remove(number_to_change)
    with open(file_name, 'w', encoding='utf-8') as file:
        for note in note_list:
            line = ' '.join(note) + '\n'
            file.write(line)
    print('Заметка из списка удалена! \n')


def print_notes(note_list: list):
    for note in note_list:
        for key, value in note.items():
            print(f'{key}: {value:12}', end='')
        print()


if __name__ == '__main__':
    file = 'notes.csv'
    choose_action(file)