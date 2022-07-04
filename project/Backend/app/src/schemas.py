from typing import List

from pydantic import BaseModel



# BODYPART has only a name and no other attributes
class BodyPartBase(BaseModel):
    name: str

class BodyPartCreate(BodyPartBase):
    pass

class BodyPart(BodyPartBase):

    class Config:
        orm_mode = True



# EPISODE

class EpisodeBase(BaseModel):
    date_time: int # Unix timestamp
    duration: int
    temperature: int
    deliberated: bool
    stress_level: int
    daily_cigarette_smoked: int
    body_parts: List[BodyPart]
    
class EpisodeCreate(EpisodeBase):
    pass

class Episode(EpisodeBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True

# USER

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    episodes: List[Episode] = []

    class Config:
        orm_mode = True


# ==== TOKEN ====

class TokenBase(BaseModel):
    access_token: str
    token_type: str

class TokenOut(TokenBase):
    session_expires: int

class TokenData(BaseModel):
    email: str = None        


