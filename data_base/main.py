import sqlite3 as sq


def check_api_key(api_key):
    with sq.connect('test.db') as con:
        name = 'main'
        cur = con.cursor()
        cur.execute(f'SELECT * FROM "{name}" WHERE api_key = {api_key}')
        return cur.fetchone()


def create_user_in_db(api_key):
    with sq.connect('test.db') as con:
        name = 'main'
        cur = con.cursor()
        cur.execute(f'INSERT INTO "{name}" (api_key) VALUES ({api_key})')


def add_promt_to_user(api_key, prompt):
    pass


def create_table():
    """
    Создать таблицу
    """
    with sq.connect('test.db') as con:
        name = 'main'
        cur = con.cursor()
        cur.execute(f'''
        CREATE TABLE IF NOT EXISTS '{name}'(
            api_key INTEGER PRIMARY KEY AUTOINCREMENT,
            language TEXT NOT NULL DEFAULT 'en',
            num_of_generations INTEGER DEFAULT 0
        )
        ''')


def drop_table():
    """
    Удалить таблицу
    """
    with sq.connect('test.db') as con:
        name = 'main'
        cur = con.cursor()
        cur.execute(f'DROP TABLE IF EXISTS "{name}"')


def drop_user(api_key):
    with sq.connect('test.db') as con:
        name = 'main'
        cur = con.cursor()
        cur.execute(f'DELETE FROM "{name}" WHERE api_key = {api_key}')

def num_gens(api_key):
    with sq.connect('test.db') as con:
        name = 'main'
        cur = con.cursor()
        cur.execute(f'SELECT num_of_generations FROM "{name}" WHERE api_key = {api_key}')
        return cur.fetchone()[0]
