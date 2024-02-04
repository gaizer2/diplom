import time

import mysql.connector

# Подключение к базе данных
cnx = mysql.connector.connect(
    host="127.0.0.1",
    user="root",

    database="TEST"
)
cursor = cnx.cursor()
# Пример создания таблицы
create_table_query = "CREATE TABLE IF NOT EXISTS example (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))"
cursor.execute(create_table_query)

# Пример вставки записи
insert_query = "INSERT INTO example (name) VALUES (%s)"
data = ("Пример",)
cursor.execute(insert_query, data)

# Пример выборки данных
select_query = "SELECT * FROM example"
cursor.execute(select_query)
records = cursor.fetchall()
for record in records:
    print(record)
cursor.close()
cnx.close()
time.sleep(10)