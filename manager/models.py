""" Классы для управления данными """
import json
import os
from datetime import datetime


# определяем путь к папке data в родительской директории
data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))

# проверяем существование папки data и создаем ее, если она не существует
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

# Личный аккаунт имеющий имя и уникальный id
# в инициализации класса, создается экземпляр класса FinanceManager
# создает уникальный json файл под каждый аккаунт
# в методах этого класса, объект обращается к методам из объекта manager 
class PersonalAccount:
    def __init__(self, name, account_id):
        self.name = name
        self.account_id = account_id
        self.manager = FinanceManager(f'{self.name}_{account_id}_finances.json')

    def add_record(self, category, amount, description):
        self.manager.add_record(self.name, category, amount, description)

    def edit_record(self, index, category=None, amount=None, description=None):
        self.manager.edit_record(index, category, amount, description)

    def delete_record(self, index):
        self.manager.delete_record(index)

    def display_balance(self):
        self.manager.display_balance()

    def search_records(self, category=None, start_date=None, end_date=None, min_amount=None, max_amount=None):
        return self.manager.search_records(category, start_date, end_date, min_amount, max_amount)




# общий класс для управления финансами
class FinanceManager:
    # инициализируем класс, в будущем объект
    # указываем имя файла (буду хранить в json формате)
    # так же будем загружать данные из файла при создании объекта
    def __init__(self, filename):
        self.filename = os.path.join(data_dir, filename)
        self.data = self.load_data()

    # добавит и сохранит данные в json c разметкой utf8
    # если не установить разметку 
    # в файле будет ничего не понятно
    # так же если имя было написано например: Дерек Фрост
    # запись файла будет Дерек_Форост
    def save_data(self):
        filename = self.filename.replace(' ', '_')
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(self.data, file, ensure_ascii=False, indent=4)


    # та самая загрузка данных,
    # использует менеджер контекста для безопасного открытия и закрытия файла
    # если файл не найден, отдаст пустой список
    def load_data(self):
        try:
            print(f'Запись производится в файл {self.filename}')
            with open(self.filename, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return []
        


    # добавит новую запись в список данных и сохранит
    def add_record(self, name, category, amount, description):
        date = datetime.now().strftime('%Y-%m-%d')
        record = {
            'Имя': name,
            'Дата': date,
            'Категория': category,
            'Сумма': amount,
            'Описание': description
        }
        self.data.append(record)
        self.save_data()

    # редактирует уже существущие записи по указаному индексу
    # если указаны новые записи по индексу
    def edit_record(self, index, category=None, amount=None, description=None):
        if index < len(self.data):
            record = self.data[index]
            record['Категория'] = category if category else record['Категория']
            record['Сумма'] = amount if amount else record['Сумма']
            record['Описание'] = description if description else record['Описание']
            self.save_data()
        else:
            print("Запись для редактирования с таким индексом не найдена")

    # удалит запись с указанным индексом
    def delete_record(self, index):
        if index < len(self.data):
            del self.data[index]
            self.save_data()
        else:
            print("Запись для удаления с таким индексом не найдена")

    # выводит баланс, сумму доходов и расходов
    def display_balance(self):
        income = sum(record['Сумма'] for record in self.data if record['Категория'].lower() == 'доход')
        expenses = sum(record['Сумма'] for record in self.data if record['Категория'].lower() == 'расход')
        balance = income - expenses
        print(f"Баланс: {balance}")

    # метод для поиска записей по заданным данным
    # вернет список записей подходящих к условиям
    def search_records(
            self, 
            category=None,
            start_date=None,
            end_date=None,
            min_amount=None,
            max_amount=None):
        filtered_records = []

        # Поиск записи по заданым данным
        # Дата заполняетсяв диапазоне ОТ и ДО, аналогично и сумма
        for record in self.data:
            is_matching_category = not category or record['Категория'] == category
            is_in_date_range = (not start_date or record['Дата'] >= start_date) and (not end_date or record['Дата'] <= end_date)
            is_in_amount_range = (not min_amount or record['Сумма'] >= min_amount) and (not max_amount or record['Сумма'] <= max_amount)

            if is_matching_category and is_in_date_range and is_in_amount_range:
                filtered_records.append(record)

        return filtered_records
    

# Простой пример для добавления и отображения
# достаточно просто запустить этот файл 
#? python models.py

# account = PersonalAccount('Анастасия', '1')
# account.add_record('Доход', 5000, 'Зарплата')

# account.display_balance()