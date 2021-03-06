import hashlib


class PasswordUtils:

    @staticmethod
    def hash_password(password: str, salt: bytes) -> str:
        hashed_pass = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 100000)
        return hashed_pass.hex()

    @staticmethod
    def verify_password(stored_password: str, input_password: str, salt: bytes):
        return PasswordUtils.hash_password(input_password, salt) == stored_password
