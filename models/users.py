#pydantic user model
from pydantic import BaseModel

class User(BaseModel):
    profile_url:str