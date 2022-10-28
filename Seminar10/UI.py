def input_from_currency():
    from_what_currency = input("Введите трехбуквенный код валюты, \033[1mкоторую вы хотите конвертировать\033[0m: ").strip(" ")
    if from_what_currency.isalpha():
        return from_what_currency
    else:
        print("\033[1mНекоректный ввод, повторите попытку.\033[0m\n")
        return input_from_currency()


def input_in_currency():
    in_what_currency = input("Введите трехбуквенный код валюты, \033[1mв которую вы хотите конвертировать\033[0m: ").strip(" ")
    if in_what_currency.isalpha():
        return in_what_currency
    else:
        print("\033[1mНекоректный ввод, повторите попытку.\033[0m\n")
        return input_in_currency()


def amount_currency():
    amount = input("Введите цифрами сколько необходимо конвектировать: ")
    if amount.isdigit():
        return amount
    else:
        print("\033[1mНекоректный ввод, повторите попытку.\033[0m\n")
        return amount_currency()
