import json
from datetime import datetime

def load_operations(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:  # Добавлено encoding='utf-8'
        return json.load(file)

def format_account_number(account):
    return f"**{account[-4:]}"

def format_card_number(card):
    return f"{card[:4]} {card[4:6]}** **** {card[-4:]}"


def display_operations(operations):
    executed_operations = []

    for op in operations:
        if 'state' not in op:
            print("В объекте отсутствует ключ 'state':")
            print(op)
            continue  # Пропуск объекта без ключа 'state'

        try:
            if op['state'] == 'EXECUTED':
                op['date'] = datetime.strptime(op['date'], '%Y-%m-%dT%H:%M:%S.%f')
                executed_operations.append(op)
        except KeyError as e:
            print("Ошибка в следующем объекте:")
            print(op)  # Вывод объекта, вызвавшего ошибку
            raise e  # Повторное возбуждение исключения для прекращения выполнения

    executed_operations.sort(key=lambda x: x['date'], reverse=True)

    for operation in executed_operations[:5]:
        print(operation['date'].strftime('%d.%m.%Y'), operation['description'])
        if 'from' in operation:
            print(format_card_number(operation['from']), '->', format_account_number(operation['to']))
        else:
            print("->", format_account_number(operation['to']))
        print(f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}\n")




