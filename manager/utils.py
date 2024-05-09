""" Вспомогательные функции """
from datetime import datetime


# В большинстве всех функций 
# выполняются почти все одинаковые действия 
# поиск корректного индекса, и правильности типа данных 
# после всех правильных введенных данных 
# вызываются методы для сохранения/редактирования/удаления

# 1 валидация данных
# жесткий контроль над тем чтобы было написано одна из двух категорий
# так же переводит написанное в нижний регистр
def add_record_input(account):
    while True:
        category = input("Введите категорию (Доход/Расход): ").strip().lower()
        if category not in ['доход', 'расход']:
            print('[INCORRECT CATEGORY] Некорректная категорияю. \
                  Пожалуйста, введите "Доход" или "Расход"')
        else:
            break

    while True:
        try:
            amount = float(input("Введите сумму: "))
            break
        except ValueError as Err:
            print(f'Value error: {Err}, Некорректная сумма. Пожалуйста, введите число ')
            
    description = input("Введите описание: ")
    account.add_record(category, amount, description)
    
# 2
# валидация индекса и тип данных
def edit_record_input(account):
    while True:
        try:
            index = int(input("Введите индекс записи для редактирования: "))
            if 0 <= index < len(account.manager.data):
                break
            else:
                print("[INDEX EMPTY] Индекст не найден. Пожалуйста, введите существующий индекс.")
        except ValueError:
            print("[INCORRECT INDEX] Некорректный индекс. Пожалуйста, введите целое число.")

    category = input("Введите новую категорию (или оставьте пустым для сохранения текущей): ")
    while category.lower() not in ["", "доход", "расход"]:
        print('[INCORRECT CATEGORY] Некорректная категорияю. \
              Пожалуйста, введите "Доход" или "Расход" \
              (или оставьте пустым для сохранения текущей')
        
        category = input("Введите новую категорию (или оставьте пустым для сохранения текущей): ")

    amount_str = input("Введите новую сумму (или оставьте пустым для сохранения текущей): ")
    if amount_str:
        while True:
            try:
                amount = float(amount_str)
                break
            except ValueError as Err:
                print(f'Value error: {Err}, Некорректная сумма. Пожалуйста, введите число ')
                amount_str = input("Введите новую сумму (или оставьте пустым для сохранения текущей): ")
    else:
        amount = None

    description = input("Введите новое описание (или оставьте пустым для сохранения текущего): ")
    account.edit_record(index, category.strip().lower(), amount, description.strip())


# 3 
# валидация индекса
def remove_record_input(account):
    while True:
        try:
            index = int(input("Введите индекс записи для удаления: "))
            if 0 <= index < len(account.manager.data):
                break
            else:
                print("[INDEX EMPTY] Индекст не найден. Пожалуйста, введите существующий индекс.")
        except ValueError:
            print("[INCORRECT INDEX] Некорректный индекс. Пожалуйста, введите целое число.")
    
    account.delete_record(index)

# 4
# вызов методов внутри функции main_loop в файле cli.py
# метод в классе выполняет все необходимое

# 5
# валидация для правильного формата времени
def validate_date(date_str):
    try:
        if date_str:
            datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

# валидация суммы c типом float
def validate_amount(amount_str):
    try:
        if amount_str:
            float(amount_str)
        return True
    except ValueError:
        return False

# поиск записи по введенным данным
# Категория 
# от какой даты 
# по какую дату искать запись
# диапазон минимальной суммы и максимальной
# и соответсвенно вывод найденных записей
def search_records_from_input(account):
    while True:
        category = input("Введите категорию (или оставьте пустым для любой категории): ").strip()
        if category.lower() in ["", "доход", "расход"]:
            break
        print('[INCORRECT CATEGORY] Некорректная категорияю. \
              Пожалуйста, введите "Доход" или "Расход" \
              или оставьте пустым')

    while True:
        start_date = input("Введите начальную дату (гггг-мм-дд) (или оставьте пустым для любой даты): ").strip()
        if validate_date(start_date):
            break
        print("[INCORRECT DATE] Некорректный формат даты. Пожалуйста, введите дату в формате 'гггг-мм-дд'.")

    while True:
        end_date = input("Введите конечную дату (гггг-мм-дд) (или оставьте пустым для любой даты): ").strip()
        if validate_date(end_date):
            break
        print("INCORRECT DATE] Некорректный формат даты. Пожалуйста, введите дату в формате 'гггг-мм-дд'.")

    while True:
        min_amount_str = input("Введите минимальную сумму (или оставьте пустым для любой суммы): ").strip()
        if validate_amount(min_amount_str):
            break
        print("[INCORRECT SUM] Некорректная сумма. Пожалуйста, введите число.")

    while True:
        max_amount_str = input("Введите максимальную сумму (или оставьте пустым для любой суммы): ").strip()
        if validate_amount(max_amount_str):
            break
        print("[INCORRECT SUM] Некорректная сумма. Пожалуйста, введите число.")

    min_amount = float(min_amount_str) if min_amount_str else None
    max_amount = float(max_amount_str) if max_amount_str else None
    results = account.search_records(category.lower(), start_date, end_date, min_amount, max_amount)
    for i, record in enumerate(results):
        print(f"Запись {i}: {record}")
