import unittest
from Saving_Passwords.src.User import User
from Saving_Passwords.src.Password_Utils import PasswordUtils


class TestPasswordUtils(unittest.TestCase):
    def test_hashing_password(self):
        user = User("damian", "123$123qwe")
        hashed = PasswordUtils.hash_password(user.password, user.salt)
        self.assertNotEqual(hashed, "123$123qwe")

    def test_verifying_password(self):
        user = User("damian", "123$123qwe")
        is_verified = PasswordUtils.verify_password(stored_password=user.password, salt=user.salt,
                                                    input_password="123$123qwe")
        self.assertTrue(is_verified)

    def test_verifying_wrong_password(self):
        user = User("damian", "123$123qwe")
        is_verified = PasswordUtils.verify_password(stored_password=user.password, salt=user.salt,
                                                    input_password="does it work?")
        self.assertFalse(is_verified)