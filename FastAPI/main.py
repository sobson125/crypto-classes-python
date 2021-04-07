import uvicorn
from symetric import Symetric
from fastapi import FastAPI
from message import Message

app = FastAPI()
symetric = Symetric()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/symetric/key")
def get_key():
    return Symetric.create_random_key()


@app.post("/symetric/key")
def post_key(key: str):
    symetric.set_key(key=key)
    return {"info": "ok"}


@app.post("/symetric/encode")
async def post_symmetric_encode(message: Message):
    return {"encrypted_message": symetric.encode_message(message.message)}


@app.post("/symetric/decode")
async def post_symmetric_decode(message: Message):
    return {"decoded_message": symetric.decode_message(message.message)}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
