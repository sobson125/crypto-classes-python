from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.exceptions import InvalidSignature
import base64


class Asymmetric():
    def __init__(self) -> None:
        self.private_key = None
        self.public_key = None

    def generate_keys(self) -> None:
        """
        Generates public and private key
        :return:
        """
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
        )
        self.public_key = self.private_key.public_key()

    def get_keys(self) -> dict:
        """
        Getter for both fields of private and public keys in class instance
        :return:
        """
        pem_private = self.private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )
        pem_public = self.private_key.public_key().public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        return {
            "private key": pem_private.hex(),
            "public key": pem_public.hex()
        }

    def get_keys_ssh(self) -> dict:
        """
        Getter for both fields of private and public keys in class instance in using ssh
        :return:
        """
        pem_private_ssh = self.private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.OpenSSH,
            encryption_algorithm=serialization.NoEncryption()
        )
        pem_public_ssh = self.private_key.public_key().public_bytes(
            encoding=serialization.Encoding.OpenSSH,
            format=serialization.PublicFormat.OpenSSH
        )
        return {
            "private key": pem_private_ssh.hex(),
            "public key": pem_public_ssh.hex()
        }

    def set_keys(self, private_key, public_key) -> None:
        """
        Setter for public and private key
        :param private_key:
        :param public_key:
        :return:
        """
        self.private_key = serialization.load_pem_private_key(
            bytearray.fromhex(private_key),
            password=None
        )
        self.public_key = serialization.load_pem_public_key(bytearray.fromhex(public_key))

    def sign_message(self, message: str) -> bytes:
        """
        Signs message so it can not be forged
        :param message:
        :return:
        """
        return base64.b64encode(self.private_key.sign(
            bytes(message, "utf-8"),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256())
        )

    def verify_message(self, message: str, signature: str) -> bool:
        """
        Verifies whether messsage recieved is not changed by people with malicious intent
        :param message:
        :param signature:
        :return:
        """
        decoded_sign = base64.b64decode(signature)
        try:
            self.public_key.verify(
                decoded_sign,
                bytes(message, "utf-8"),
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except InvalidSignature:
            return False

    def encode_message(self, message: str) -> bytes:
        """
        Encodes message
        :param message:
        :return:
        """
        return base64.b64encode(self.public_key.encrypt(
            bytes(message, "utf-8"),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            ))
        )

    def decode_message(self, message: str) -> str:
        """
        Decodes message
        :param message:
        :return:
        """
        decoded = base64.b64decode(message)
        return self.private_key.decrypt(
            decoded,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
