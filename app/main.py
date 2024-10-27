import uvicorn

from pathlib import Path

from typing import Union
from typing import Annotated

from fastapi import FastAPI, Request
from fastapi import Form

# Esto sirve para importar el BODY de la request HTTP
from pydantic import BaseModel, Field

from fastapi.staticfiles import StaticFiles

#  trabajar con templates y responder html
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

# helpers

from datetime import datetime

# static files

app = FastAPI()

BASE_PATH = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_PATH / "templates"))

app.mount("/public",StaticFiles(directory=str(BASE_PATH / "public"),html = True),name="public")


class Item(BaseModel):
    name:str
    price: float
    is_offer: Union[bool, None] = None

@app.get("/")
def read_root():
    return {"hello","world"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str,None]=None):
    return {"item_id":item_id,"q":q}

@app.put("/items/{item_id}")
async def update_item(item_id:int , item: Item):
    return {"item_name": item.name, "item_id": item_id}

# Otras opciones por defecto
@app.get("/example-htmx", response_class=HTMLResponse)
async def example_clock(request: Request):
    return templates.TemplateResponse(
        "example-htmx.html", {"request": request}
    )

@app.get("/example-clock", response_class=HTMLResponse)
async def example_clock(request: Request):
    now=datetime.now()
    current_time=now.strftime("%H:%M:%S")

    return templates.TemplateResponse(
        "clock.html", {"request": request, "time":current_time}
    )

@app.post("/example-sayhi", response_class=HTMLResponse)
async def example_sayhi(request: Request, name: str = Form(...)):

    return templates.TemplateResponse(
        "say-hi.html", {"request": request,"name":name}
    )

@app.get("/example-load-clock", response_class=HTMLResponse)
async def load_clock(request: Request):
    return templates.TemplateResponse(
        "load-clock.html",context={"request": request}
    )

if __name__ == "__main__":
    uvicorn.run(app,host="0.0.0.0",port=8000)