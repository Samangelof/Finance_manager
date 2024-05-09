""" Основной скрипт для запуска приложения """
from manager.cli import main_loop, create_account


def main():
    account = create_account()
    main_loop(account)
    
if __name__ == "__main__":
    main()