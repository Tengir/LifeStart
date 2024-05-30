import json
from data_message import data as DATA


class Data:
    def __init__(self):
        data = DATA
        self.message = self.Message(data['message'])
        self.question = [
            (q["message"], [(ans[0], ans[1]) for ans in q["answers"]])
            for q in data["questions"]]

    class Message:
        def __init__(self, message):
            self.menu = message['menu']
            self.digest = self.Digest(message["digest"])
            self.faq = message['faq']
            self.sections = message['sections']
            self.call_menu_test = message["call_menu_test"]

        class Digest:
            def __init__(self, message):
                self.text = message["text"]
                self.files_id = message["files_id"]


# Метод для чтения "data.json". В новой версии перешли на dict в data_message.
# def read_json():
#     file_path = "data.json"
#     with open(file_path, "r", encoding="utf-8") as json_file:
#         data = json.load(json_file)
#     return data
