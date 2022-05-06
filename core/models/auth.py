from pydantic import BaseModel


class AuthDataModel(BaseModel):
    client_id: str = "qg705rudhk2h7yztnasre9v727ub1p"
    client_secret: str = "zup61ignsbbmk32bwkngpjmp4b5x79"
    grant_type: str = "client_credentials"


class AuthResponseModel(BaseModel):
    token_type: str
    access_token: str
    expires_in: int
