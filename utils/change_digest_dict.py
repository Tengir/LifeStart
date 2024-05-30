import os
from data_message import data


def change_digest(text, files_id):
    file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data_message.py")

    data['message']['digest']['text'] = text
    data['message']['digest']['files_id'] = files_id

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(f"data = {str(data)}")
