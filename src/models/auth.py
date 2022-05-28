from pydantic import BaseModel
from src.configs.main_configuration import AUTH0_CLIENT_ID, AUTH0_CLIENT_SECRET, AUTH0_GRANT_TYPE


class AuthDataModel(BaseModel):
    client_id: str = AUTH0_CLIENT_ID
    client_secret: str = AUTH0_CLIENT_SECRET
    grant_type: str = AUTH0_GRANT_TYPE


class AuthResponseModel(BaseModel):
    token_type: str
    access_token: str
    expires_in: int
