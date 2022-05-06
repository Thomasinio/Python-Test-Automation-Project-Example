from pydantic import BaseModel
from core.configs.main_configuration import AUTH0_CLIENT_ID


class AuthDataModel(BaseModel):
    client_id: str = AUTH0_CLIENT_ID
    client_secret: str = "zup61ignsbbmk32bwkngpjmp4b5x79"
    grant_type: str = "client_credentials"


class AuthResponseModel(BaseModel):
    token_type: str
    access_token: str
    expires_in: int
