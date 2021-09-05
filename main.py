# fastapi lib
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path

base_path = Path(__file__).resolve().parent
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
template = Jinja2Templates(directory=str(base_path / 'templates'))


@app.get('/airportHome')
async def root(request: Request):
    return template.TemplateResponse('index.html', {'request': request})
