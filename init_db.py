import os

from dotenv import load_dotenv

import psycopg2

load_dotenv()


def init_db():
    # DBの情報を取得
    dsn = os.environ.get('DATABASE_URL')
    # print(dsn)
    # DBに接続(コネクションを貼る)
    conn = psycopg2.connect(dsn)
    cur = conn.cursor()
    # SQLを用意
    with open('schema.sql', encoding="utf-8") as f:
        sql = f.read()
        # SQLを実行
        cur.execute(sql)

    # 実行状態を保存
    conn.commit()
    # コネクションを閉じる
    conn.close()


def register_user(name, age):
    # DBの情報を取得
    dsn = os.environ.get('DATABASE_URL')
    # print(dsn)
    # DBに接続(コネクションを貼る)
    conn = psycopg2.connect(dsn)
    cur = conn.cursor()
    # SQLを用意
    sql = "INSERT INTO users (name, age) VALUES (%(name)s, %(age)s)"
    # SQLを実行
    cur.execute(sql, {'name': name, 'age': age})
    # 実行状態を保存
    conn.commit()
    # コネクションを閉じる
    conn.close()


def all_users():
    dsn = os.environ.get('DATABASE_URL')
    conn = psycopg2.connect(dsn)
    cur = conn.cursor()
    # すべてのユーザー情報を取得
    sql = "SELECT * FROM users;"
    cur.execute(sql)
    users = cur.fetchall()
    conn.commit()
    conn.close()
    return users


def main():
    init_db()

    name = 'Bob'
    age = 19
    register_user(name, age)

    users = all_users()
    print(users)

    # command = input('どんな操作?')
    # if command == '1':
    #     name = input('name?')
    #     age = input('age?')
    #     register_user(name, age)


if __name__ == '__main__':
    main()
