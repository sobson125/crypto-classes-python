from cryptography.fernet import Fernet
import logging

logger = logging.getLogger("hashing")
logging.basicConfig(level=logging.DEBUG)


class Symetric():

    def __init__(self) -> None:
        self.key = None

    @staticmethod
    def create_random_key() -> str:
        key = Fernet.generate_key()
        return key.hex()

    def set_key(self, key: str) -> None:
        self.key = bytearray.fromhex(key)
        print(self.key)

    def encode_message(self, message: str) -> bytes:
        logger.info('debugining inside encode')
        logger.critical(Fernet(self.key).encrypt(bytes(message, 'utf-8')))
        return Fernet(self.key).encrypt(bytes(message, 'utf-8'))

    def decode_message(self, message: str) -> bytes:
        logger.info('debugining inside decode')
        logger.critical(Fernet(self.key).decrypt(bytes(message, 'utf-8')))
        return Fernet(self.key).decrypt(bytes(message, 'utf-8'))
