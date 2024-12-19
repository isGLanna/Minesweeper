# -----------------------------------------------
# Program: Campo Minado
# Developers: Giordano Lanna e Elisa Ribeiro
# Date: 17/07/2024
# Language: Python 3.11
# -----------------------------------------------

import sqlite3

# verifica se tabela 'players' já existe, caso contrário será criada
def create_table():
    database = sqlite3.connect("data/historic_player.db")
    cursor = database.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='players'")
    if not cursor.fetchone():
        cursor.execute("CREATE TABLE  IF NOT EXISTS players (name text, time integer, level integer)")
        database.commit()
    
    database.close()

# insere 'players' no banco de dados
def insert_player(name, new_time, level):
    database = sqlite3.connect("data/historic_player.db")
    cursor = database.cursor()

    cursor.execute("SELECT time FROM players WHERE name = ? AND level = ?", (name, level))
    result = cursor.fetchone()

    if result:
        time = result[0]
        if new_time < time:
            cursor.execute("UPDATE players SET time = ? WHERE name = ? AND level = ?", (name, new_time, level))
    else:
        cursor.execute("INSERT INTO players (name, time, level) VALUES (?, ?, ?)", (name, new_time, level))

    print("tentando salvar")
    database.commit()
    database.close()

# apagar histórico
def clean_history():
    database = sqlite3.connect("data/historic_player.db")
    cursor = database.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    all_tables = cursor.fetchall()

    for table in all_tables:
        cursor.execute(f"DROP TABLE {table[0]}")

    database.commit()
    database.close()

# >>---------------------------------- FUNÇÃO DE RETORNO ----------------------------------<< #

def fetch_players():
    database = sqlite3.connect("data/historic_player.db")
    cursor = database.cursor()

    cursor.execute('SELECT name, time FROM players WHERE level = 1 ORDER BY time ASC')
    easy_level_row = cursor.fetchall()

    cursor.execute('SELECT name, time FROM players WHERE level = 0 ORDER BY time ASC')
    hard_level_row = cursor.fetchall()

    database.close()

    return easy_level_row, hard_level_row

create_table()


