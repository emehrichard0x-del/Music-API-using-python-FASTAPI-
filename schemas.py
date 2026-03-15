from enum import Enum
from pydantic import BaseModel
from datetime import date

#url validation
class GenreURLChoices(Enum):
    #lowercass incase use adds uppercase letters
    METAL= 'metal'
    HIP_HOP = 'hip-hop'
    ROCK='rock'
    ELECTRONIC = 'electronic'

class Album(BaseModel):
    title:str
    release_date:date

class Band(BaseModel):
    #{'id':1,'name': 'id->1 The Kinks', 'genre': 'Rock'},   
    id:int 
    name:str
    genre:str
    albums: list[Album] =[]


