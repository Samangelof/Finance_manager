# Личный финансовый кошелек

Простое консольное приложение для учета личных доходов и расходов.

## Установка и запуск

1. Склонируйте репозиторий:
2. Запустите приложение:
    python run.py

## Структура проекта

- `manager/` - модуль управления финансами
- `models.py` - классы для управления данными
- `utils.py` - вспомогательные функции
- `cli.py` - интерфейс командной строки

- `run.py` - основной скрипт для запуска приложения

## Примеры использования
### Создание нового аккаунта
```python
create_account()
```

### Добавление записи о доходе или расходе
```python
account.add_record('Доход', 5000, 'Продажа вещей')
account.add_record('Расход', 1500, 'Покупка продуктов')
```

### Редактирование существующей записи
```python
account.edit_record(0, category='Доход', amount=6000, description='Бонус')
```

### Удаление записи по индексу
```python
account.delete_record(1)
```

### Вывод баланса
```python
account.display_balance()
```

### Поиск записей
```python
results = account.search_records(
    category='Доход',
    start_date='2024-01-01',
    end_date='2024-12-31',
    min_amount=1000,
    max_amount=5000
)
# Вывести найденные записи
for result in results:
    print(result)
```

### Вывод меню
```python
view_actions()
```
