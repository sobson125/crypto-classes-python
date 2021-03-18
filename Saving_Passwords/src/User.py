from typing import Any

from Saving_Passwords.src.Password_Utils import PasswordUtils
import uuid


class User:

    def __init__(self, username: str, password: str) -> None:
        super().__init__()
        self.username = username
        self.salt = uuid.uuid4().bytes
        self.password = PasswordUtils.hash_password(password=password, salt=self.salt)

    def get_salt(self):
        return self.salt

    def get_password(self):
        return self.password

    def get_username(self):
        return self.username
