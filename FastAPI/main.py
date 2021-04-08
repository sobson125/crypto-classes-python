import uvicorn
from symmetric import Symmetric
from fastapi import FastAPI
from FastAPI.dto.message import Message
from FastAPI.dto.signed_message import SignedMessage
from asymmetric import Asymmetric

app = FastAPI()
symmetric = Symmetric()
asymmetric = Asymmetric()


@app.get("/")
def read_root():
    """
    Home root
    :return:
    """
    return {"Hello": "World"}


@app.get("/symmetric/key")
def get_symmetric_key():
    """
    Get symmetric key
    :return:
    """
    return Symmetric.create_random_key()


@app.post("/symmetric/key", status_code=201)
def set_symmetric_key(key: str):
    """
    Set symmetric key
    :param key:
    :return:
    """
    symmetric.set_key(key=key)
    return {"info": "ok"}


@app.post("/symmetric/encode", status_code=201)
async def symmetric_encode(message: Message):
    """
    Encode message symmetrically
    :param message:
    :return:
    """
    return {"encrypted_message": symmetric.encode_message(message.message)}


@app.post("/symmetric/decode", status_code=201)
async def symmetric_decode(message: Message):
    """
    Decode message symmetrically
    :param message:
    :return:
    """
    return {"decoded_message": symmetric.decode_message(message.message)}


@app.get("/asymmetric/key")
def generate_and_get_asymmetric_keys():
    """
    Generete and return asymmetric public and private keys
    :return:
    """
    asymmetric.generate_keys()
    return asymmetric.get_keys()


@app.get("/asymmetric/key/ssh")
def get_asymmetric_keys_ssh():
    """
    Return public and private keys using ssh
    :return:
    """
    return asymmetric.get_keys_ssh()


@app.post("/asymmetric/key/", status_code=201)
def set_asymmetric_keys(private_key, public_key):
    """
    Set asymmetric public and private keys
    :param private_key:
    :param public_key:
    :return:
    """
    asymmetric.set_keys(private_key=private_key, public_key=public_key)
    return {"info": "ok"}


@app.post("/asymmetric/sign", status_code=201)
def sign_message(message: Message):
    """
    Sign message asymmetrically
    :param message:
    :return:
    """
    signed_message = asymmetric.sign_message(message.message)
    return {"sign": signed_message}


@app.post("/asymmetric/verify", status_code=201)
def verify_message(message: SignedMessage):
    """
    Verify whether message wasn't modified
    :param message:
    :return:
    """
    verified = asymmetric.verify_message(message.message, message.signature)
    return {"Verified": verified}


@app.post("/asymmetric/encode", status_code=201)
def encode_asymmetric_message(message: Message):
    """
    Encode message asymmetrically
    :param message:
    :return:
    """
    encoded_message = asymmetric.encode_message(message.message)
    return {"Encoded message": encoded_message}


@app.post("/asymmetric/decode", status_code=201)
def decode_asymmetric_message(message: Message):
    """
    Decode message asymmetrically
    :param message:
    :return:
    """
    decoded_message = asymmetric.decode_message(message.message)
    return {"Decoded message": decoded_message}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
