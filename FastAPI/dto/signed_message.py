from pydantic import BaseModel


class SignedMessage(BaseModel):
    message: str
    signature: str
