"""
@Author: your name
@Date: 2020-04-19 21:26:56
@LastEditTime: 2020-04-19 22:54:33
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \Password-management\sqlitelib.py
"""
import sqlite3


def sqlitelib(dbfile, command):
    con = sqlite3.connect(dbfile)
    cur = con.cursor()
    cur.execute(command)
    con.commit()

    result = cur.fetchall()

    cur.close()
    con.close()
    return result


if __name__ == "__main__":
    a = sqlitelib('sqlite3-key.db', 'select * from pwd')
    print(a)
