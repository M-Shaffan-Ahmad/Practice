import sqlite3


def database_up(text, file_name="None"):
    conn = sqlite3.connect('text2speech.sqlite')
    cur = conn.cursor()
    check = True
    cur.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='SpeechText' ''')
    if cur.fetchone()[0] == 1:
        check = False

    if check:
        cur.execute('''
        CREATE TABLE SpeechText (speech TEXT, file_name TEXT)''')
    cur.execute("""
        INSERT INTO SpeechText VALUES
            (?, ?)""", (text, file_name))

    conn.commit()
    conn.close()



