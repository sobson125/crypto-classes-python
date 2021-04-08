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
    return {"Hello": "World"}


@app.get("/symmetric/key")
def get_symmetric_key():
    return Symmetric.create_random_key()


@app.post("/symmetric/key", status_code=201)
def set_symmetric_key(key: str):
    symmetric.set_key(key=key)
    return {"info": "ok"}


@app.post("/symmetric/encode", status_code=201)
async def symmetric_encode(message: Message):
    return {"encrypted_message": symmetric.encode_message(message.message)}


@app.post("/symmetric/decode", status_code=201)
async def symmetric_decode(message: Message):
    return {"decoded_message": symmetric.decode_message(message.message)}


@app.get("/asymmetric/key")
def generate_and_get_asymmetric_keys():
    asymmetric.generate_keys()
    return asymmetric.get_keys()


@app.get("/asymmetric/key/ssh")
def get_asymmetric_keys_ssh():
    return asymmetric.get_keys_ssh()


@app.post("/asymmetric/key/", status_code=201)
def set_asymmetric_keys(private_key, public_key):
    asymmetric.set_keys(private_key=private_key, public_key=public_key)
    return {"info": "ok"}


@app.post("/asymmetric/sign", status_code=201)
def sign_message(message: Message):
    signed_message = asymmetric.sign_message(message.message)
    return {"sign": signed_message}


@app.post("/asymmetric/verify", status_code=201)
def verify_message(message: SignedMessage):
    verified = asymmetric.verify_message(message.message, message.signature)
    return {"Verified": verified}


@app.post("/asymmetric/encode", status_code=201)
def encode_asymmetric_message(message: Message):
    encoded_message = asymmetric.encode_message(message.message)
    return {"Encoded message": encoded_message}


@app.post("/asymmetric/decode", status_code=201)
def decode_asymmetric_message(message: Message):
    decoded_message = asymmetric.decode_message(message.message)
    return {"Decoded message": decoded_message}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
