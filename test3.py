import sqlite3


columns_to_check=['login', 'password']
table_name='users'
conn = sqlite3.connect('db/database.db')
cursor = conn.cursor()

    # Находим дубликаты и удаляем их
cursor.execute(f'''
        DELETE FROM {table_name} WHERE rowid NOT IN (
            SELECT MIN(rowid) FROM {table_name} GROUP BY {', '.join(columns_to_check)}
        )
    ''')

conn.commit()
conn.close()

# Пример использования функции

