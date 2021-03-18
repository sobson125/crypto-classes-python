import hashlib


class PasswordUtils:

    @staticmethod
    def hash_password(password: str, salt: bytes) -> str:
        hashed_pass = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 100000)
        return hashed_pass.hex()
