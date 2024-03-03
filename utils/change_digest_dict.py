import os
from data_message import data


def change_digest(digest):
    file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data_message.py")

    data["message"]["digest"] = digest

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(f"data = {str(data)}")
