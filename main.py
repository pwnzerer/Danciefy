from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn
from fastapi.responses import HTMLResponse
import requests

my_token =

def scoregenerator(songname):
    
    
    
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer BQCkQpxbj0eU23E2IrvvAg8VM6CCj7p-fkYecJ7-yN8PBoqER4o4AyuEDLr5qk6zUMzYUKfuA0Z-VGpzw7WUyxWWpkLWrmpvZU97snQGYuUwkmQTeXK-CAikQUaDRL5b6PUuyzlzrARnUHdiNv47cNlceYGEOr-s6N8',
    }


    params = (
        ('q', songname),
        ('type', 'track'),
        ('limit', '1'),
    )


    response = requests.get('https://api.spotify.com/v1/search', headers=headers,params=params)

    jsresponse = response.json()

    v1 = jsresponse['tracks']
    v2 = v1['items']
    v3 = v2[0]
    v4 = v3['uri']
    v5 = v4.split(":")
    trackid = v5[2]
    

    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer BQCkQpxbj0eU23E2IrvvAg8VM6CCj7p-fkYecJ7-yN8PBoqER4o4AyuEDLr5qk6zUMzYUKfuA0Z-VGpzw7WUyxWWpkLWrmpvZU97snQGYuUwkmQTeXK-CAikQUaDRL5b6PUuyzlzrARnUHdiNv47cNlceYGEOr-s6N8',
    }

    params = (
        ('ids', trackid),
    )

    trackresponse = requests.get('https://api.spotify.com/v1/audio-features', headers=headers, params=params)
    jstrackresponse = trackresponse.json()

    z1 = jstrackresponse['audio_features']
    z2 = z1[0]
    dancescore = z2['danceability']
    dancescore2 = dancescore * 100
    return dancescore2


app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")



@app.get('/',response_class=HTMLResponse)
async def root(request : Request):
    return templates.TemplateResponse('index.html',{"request": request})

@app.post('/',response_class=HTMLResponse)
async def get_form_data(request : Request,inputsongname: str = Form(...)):
    songscore = scoregenerator(inputsongname)
    return templates.TemplateResponse('index.html',{"request": request,"songscore1": songscore})

# if __name__ == '__main__':
#     uvicorn.run(app)
    
    
    
