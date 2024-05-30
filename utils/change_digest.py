# Метод, который меняет digest в data.json, при этом в коде используется
# старая версия data.json. Ее нужно обновить функцией update_data.

# В новой версии не используется тк заменен json на dict в data_message.

# Я хз для чего оно тут. Рудимент крч.

import json
import os


def change_digest(text, photos_id):
    file_path = os.path.join(os.path.dirname(__file__), "../data.json")

    # Открыть файл JSON с указанием кодировки
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Изменить значение ключа 'digest'
    data['message']['digest'] = text

    # Записать обновленные данные в файл JSON
    with open(file_path, 'w') as f:
        json.dump(data, f)
