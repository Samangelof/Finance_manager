""" Интерфейс командной строки """
import time
import uuid

from manager.models import PersonalAccount
from manager.utils import (
    add_record_input,
    edit_record_input,
    remove_record_input,
    search_records_from_input
)

# Создание аккаунта
# - Имя
# - Уникальный id
# создание объекта на основе класса PersonalAccount и последущих методов
# Один запуск скрипта равняется одному созданию аккаунта
def create_account():
    name = input("Введите ваше имя: ")
    account_id = str(uuid.uuid4())[:8]
    account = PersonalAccount(name, account_id)
    time.sleep(1)
    return account

# Все доступные операции
def view_actions():
    print("\nМеню:")
    print("1. Добавить запись")
    print("2. Редактировать запись")
    print("3. Удалить запись")
    print("4. Вывести баланс")
    print("5. Поиск записей")
    print("6. Выйти")

# За выбором операции предполагается выполнение валидированных действий и
# основных методов с учетом выбираемой операции
# код будет ругаться, если не нашел индекс или тип данных не соответсвующий запрашиваемому
def main_loop(account):
    while True:
        view_actions()
        choice = input("Выберите действие: ")
        if choice == '1':
            add_record_input(account)
            print('[INFO] Операция пр добавлению была завершена')
            time.sleep(1)
        elif choice == '2':
            edit_record_input(account)
            print('[INFO] Операция по изменению была завершена')
            time.sleep(1)
        elif choice == '3':
            remove_record_input(account)
            print('[INFO] Операция по удалению была завершена')
            time.sleep(1)
        elif choice == '4':
            account.display_balance()
        elif choice == '5':
            search_records_from_input(account)
            print('[INFO] Операция по поиску завершена')
            time.sleep(1)
        elif choice == '6':
            print('[EXIT] Выход...')
            time.sleep(1)
            break
        else:
            print("Некорректный выбор. Попробуйте снова")