from fastapi import FastAPI, Request

from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.mount("/assets", StaticFiles(directory="front/Paper/dist/assets"), name="assets") 
templates = Jinja2Templates(directory="front/Paper/dist")

@app.get("/")
async def main(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

origins = [
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
                   "Authorization"],
)