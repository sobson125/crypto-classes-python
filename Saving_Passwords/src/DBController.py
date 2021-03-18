import sqlite3
import os
from Saving_Passwords.src.User import User


class DBController:
    DB_NAME = 'saving-pass.db'

    def __init__(self) -> None:
        if os.path.exists(self.DB_NAME):
            os.remove(self.DB_NAME)
        connection = self.connect_to_db()
        cursor = connection.cursor()
        cursor.execute("""CREATE TABLE users (username text,salt text,password text)""")
        connection.commit()
        connection.close()

    def connect_to_db(self):
        return sqlite3.connect(self.DB_NAME)

    def add_user(self, username: str, password: str) -> User:
        connection = self.connect_to_db()
        cursor = connection.cursor()
        new_user = User(username, password)
        cursor.execute("INSERT INTO users VALUES (?,?,?)", (new_user.username, new_user.salt, new_user.password))
        connection.commit()
        connection.close()
        return new_user

    def get_user(self, username: str) -> User:
        connection = self.connect_to_db()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = :username", {'username': username})
        user = cursor.fetchone()
        connection.close()
        return user
