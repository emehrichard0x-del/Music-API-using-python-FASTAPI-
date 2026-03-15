#import object
from fastapi import FastAPI 
from fastapi import FastAPI, HTTPException
from schemas import GenreURLChoices,Band


#instanciate
app = FastAPI()


BANDS= [
    {'id':1,'name': 'id->1 The Kin1ks', 'genre': 'Rock'},
    {'id':1,'name': 'id->1 The Kin1ks', 'genre': 'Rock'},
    
    {'id':2,'name': 'id->2 The a5', 'genre': 'metal'},
    {'id':3,'name': 'id->3 The Kinks', 'genre': 'electronic','albums':[
        {'title': 'master of reality','release_date': '1992-01-12'},
        {'title': 'master of reality','release_date': '1992-01-12'},
        {'title': 'master of reality','release_date': '1992-01-12'}
    
    ]},
    {'id':4,'name': 'id->4 The Kinks', 'genre': 'hip-hop'},
    
]

#decorator
@app.get("/bands")
async def bands(
    genre:GenreURLChoices | None = None,
    has_albums: bool = False
    
    )->list[Band]:
    band_list= [Band(**b) for b in BANDS]
    if genre:
        band_list = [
            b for b in band_list if b.genre.lower() == genre.value
        ]
    
    if has_albums:
        band_list = [b for b in band_list if len(b.albums) > 0 ]

    return band_list

"""
@app.get('/about')
async def about():
    return 'An excetpr company'
"""

@app.get('/bands/{band_id}')#,status_code = 206
async def band(band_id:int)->Band:
    band = next((Band(**b) for b in BANDS if b['id'] == band_id),None)
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
