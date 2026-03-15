#import object
from fastapi import FastAPI 
from fastapi import FastAPI, HTTPException
from enum import Enum

#instanciate
app = FastAPI()

#url validation
class GenreURLChoices(Enum):
    #lowercass incase use adds uppercase letters
    METAL= 'metal'
    HIP_HOP = 'hip-hop'
    ROCK='rock'
    ELECTRONIC = 'electronic'

BANDS= [
    {'id':1,'name': 'id->1 The Kinks', 'genre': 'Rock'},
    {'id':2,'name': 'id->2 The a', 'genre': 'metal'},
    {'id':3,'name': 'id->3 The Kinks', 'genre': 'electronic'},
    {'id':4,'name': 'id->4 The Kinks', 'genre': 'hip-hop'},
    
]

#decorator
@app.get("/bands")
async def bands()->list[dict]:
    return BANDS

"""
@app.get('/about')
async def about():
    return 'An excetpr company'
"""

@app.get('/bands/{band_id}')#,status_code = 206
async def band(band_id:int)->dict:
    band = next((b for b in BANDS if b['id'] == band_id),None)
    if band is None:
        print("error")
        #status code 404
        raise HTTPException(status_code = 404,  detail='Band not found')
    return band


"""
@app.get('/bands/genre/{genre}')
async def band(genre:str)-> dict:
    band= next((g for g in BANDS if g['genre'] == genre),None)
    if band is None:
        print("error")
    
    return band

"""
@app.get('/bands/genre/{genre}')
async def bands_for_genre(genre:GenreURLChoices) -> list[dict]:
    return [
       b for b in BANDS if b['genre'].lower() == genre.value
        #b for b in BANDS if b['genre'].lower() == genre.lower()
    
    ]
