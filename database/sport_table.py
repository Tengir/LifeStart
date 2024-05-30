import sqlite3


class SportTable:
    def __init__(self):
        self.conn = sqlite3.connect('sport.db')
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS sport_table
                              (Sport TEXT, Gender INTEGER, ActivityLevel INTEGER, Stamina INTEGER, Coordination INTEGER, Strength INTEGER, Flexibility INTEGER, Thinking INTEGER, TeamOrIndiv INTEGER)''')
        self.conn.commit()

    def insert_data(self, data):
        self.cursor.execute('DELETE FROM sport_table')
        self.cursor.executemany(
            'INSERT INTO sport_table VALUES (?,?,?,?,?,?,?,?,?)', data)
        self.conn.commit()

    def print(self):
        self.cursor.execute('SELECT * FROM sport_table')
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)

    def close_connection(self):
        self.conn.close()


# SportTable().insert_data( [('Хоккей', 1, 4, 3, 5, 4, 2, 3, 1)])
# SportTable().print()
# data = [('Хоккей', 'М', 4, 3, 5, 4, 2, 3, 1),
#                 ('Алтимат', 'М', 3, 2, 4, 2, 1, 3, 1),
#                 ('Диск-гольф', 'М', 2, 1, 5, 2, 4, 2, 0),
#                 ('Фехтование', 'М', 4, 3, 5, 3, 2, 2, 0),
#                 ('Армрестлинг', 'М', 3, 1, 3, 5, 1, 1, 0),
#                 ('Академическая гребля', 'М', 4, 4, 3, 4, 2, 2, 1),
#                 ('Плавание', 'М', 3, 4, 4, 3, 2, 2, 0),
#                 ('Бадминтон', 'М', 4, 1, 4, 1, 2, 2, 0),
#                 ('Баскетбол', 'М', 4, 3, 5, 3, 1, 3, 1),
#                 ('Волейбол', 'М', 4, 3, 5, 2, 1, 3, 1),
#                 ('Аэробика', 'М', 2, 2, 4, 3, 4, 2, 0),
#                 ('Функциональный тренинг', 'М', 4, 3, 3, 3, 3, 1, 0),
#                 ('Настольный теннис', 'М', 4, 1, 4, 1, 1, 3, 0),
#                 ('Ритмическая гимнастика', 'М', 4, 2, 4, 1, 5, 2, 0),
#                 ('Чирлидинг', 'М', 3, 2, 3, 1, 2, 1, 1),
#                 ('Тяжёлая атлетика', 'М', 4, 2, 3, 5, 1, 1, 0),
#                 ('Пляжный волейбол', 'М', 4, 3, 5, 2, 1, 2, 1),
#                 ('Керлинг', 'М', 1, 5, 3, 2, 4, 1, 0),
#                 ('Лёгкая атлетика', 'М', 4, 4, 2, 3, 2, 2, 0),
#                 ('Лыжные гонки', 'М', 5, 5, 4, 3, 2, 3, 0),
#                 ('Биатлон', 'М', 5, 5, 4, 3, 2, 4, 0),
#                 ('Полиатлон', 'М', 4, 5, 4, 4, 2, 3, 0),
#                 ('Стрельба', 'М', 2, 1, 5, 1, 2, 3, 0),
#                 ('Парусный спорт', 'М', 2, 5, 2, 1, 4, 1, 0),
#                 ('Регби', 'М', 4, 3, 4, 4, 1, 2, 1),
#                 ('Теннис', 'М', 4, 3, 5, 3, 2, 3, 0),
#                 ('Ушу', 0, 0, 0, 0, 0, 0, 0, 0),
#                 (
#                 'Рукопашный бой', 0, 0, 0, 0, 0, 0, 0, 0),
#                 ('Грепплинг', None, None, None, None, None, None, None, 0),
#                 ('Спортивная борьба', None, None, None, None, None, None, None,
#                  0),
#                 ('Смешанные единоборства', None, None, None, None, None, None,
#                  None, 0),
#                 ('Восточная борьба', None, None, None, None, None, None, None,
#                  0),
#                 ('Бокс', None, None, None, None, None, None, None, 0),
#                 ('Футбол', 'М', 3, 3, 4, 3, 1, 3, 1),
#                 ('Мини-футбол', 'М', 3, 2, 4, 3, 1, 3, 1),
#                 ('Пляжный футбол', 'М', 3, 2, 4, 3, 1, 3, 1),
#                 ('Йога/Кунг фу', 'М', 3, None, None, None, 0, None, 0),
#                 ('Айкидо', None, None, None, None, None, None, None, 0),
#                 ('Шахматы. HSE Chess club', 'М', 2, 0, 1, 0, 0, 5, 0),
#                 ('Воркаут', 'М', 4, 1, 3, 5, 2, 1, 0),
#                 ('Самостоятельные тренировки в спортзалах', 'М', 2, 1, 3, 3, 2,
#                  1, 0)]