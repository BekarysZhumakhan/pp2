import psycopg2 as psg
import csv

# Подключение к базе данных
conn = psg.connect(
    host="localhost",
    dbname="Lab_10",
    user="postgres",
    password="12345678",
    port=5432
)

cur = conn.cursor()

# Создание таблицы, если её нет
cur.execute("""
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        user_name VARCHAR(50) NOT NULL,
        surname VARCHAR(50) NOT NULL,
        phone VARCHAR(15) NOT NULL
    );
""")

# Вставка данных вручную
def insert_data():
    cur.execute(
        "INSERT INTO phonebook (user_name, surname, phone) VALUES (%s, %s, %s)",
        ('Jumakhan', 'Bekarys', '87777777777')
    )
    cur.execute(
        "INSERT INTO phonebook (user_name, surname, phone) VALUES (%s, %s, %s)",
        ('Alice', 'Smith', '87775554433')
    )

insert_data()


# with open('C:\\Users\\diffi\\OneDrive\\Рабочий стол\\pp2\\asd\\txt.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     for line in csv_reader:
#         cur.execute(
#             "INSERT INTO phonebook (user_name, surname, phone) VALUES (%s, %s, %s)",
#             (line[0], line[1], line[2])
#         )

# Обновление имени
def update_name(old_name, new_name):
    cur.execute("UPDATE phonebook SET user_name=%s WHERE user_name = %s", (new_name, old_name))

# Поиск по данным
def query_data(name=None, surname=None, phone=None):
    if name:
        cur.execute("SELECT * FROM phonebook WHERE user_name=%s", (name,))
    elif surname:
        cur.execute("SELECT * FROM phonebook WHERE surname=%s", (surname,))
    elif phone:
        cur.execute("SELECT * FROM phonebook WHERE phone=%s", (phone,))
    rows = cur.fetchall()
    for row in rows:
        print(row)

# Удаление по имени
def deleting_data(name):
    cur.execute("DELETE FROM phonebook WHERE user_name=%s", (name,))

# Сохранение изменений и закрытие соединения
conn.commit()
cur.close()
conn.close()
