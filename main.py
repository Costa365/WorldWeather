# main.py
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.triggers.date import DateTrigger
from datetime import datetime
from cities import cities
import httpx
import os
import math

from pathlib import Path

app = FastAPI()
scheduler = AsyncIOScheduler()

static_dir = Path("static")
static_dir.mkdir(exist_ok=True)

if static_dir.exists() and any(static_dir.iterdir()):
    app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

OPENWEATHERMAP_API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")

weather_data = {}

MAX_API_CALLS = 60
API_QUERY_INTERVAL = 5
BATCHES = math.ceil(len(cities)/MAX_API_CALLS)


@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse('static/favicon.ico')


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/get-weather")
async def get_weather():
    return list(weather_data.values())


def wind_direction(deg):
    directions = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
                  "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
    idx = int((deg + 11.25) / 22.5) % 16
    return directions[idx]


def format_wind(speed, deg):
    direction = wind_direction(deg)
    return f"{speed} km/h {direction}"


async def update_weather():
    dt = datetime.now()
    dts = dt.strftime("%d/%m/%Y %H:%M:%S")
    print(f"{dts} Updating weather data {update_weather.count}", flush=True)
    async with httpx.AsyncClient() as client:
        for city in cities[update_weather.count*MAX_API_CALLS:(update_weather.count+1)*MAX_API_CALLS]:
            url = f"http://api.openweathermap.org/data/2.5/weather?lat={city['lat']}&lon={city['lon']}&appid={OPENWEATHERMAP_API_KEY}&units=metric"
            try:
                response = await client.get(url)
                if response.status_code == 200:
                    data = response.json()
                    weather_data[city["name"]] = {
                        "name": city["name"],
                        "lat": city["lat"],
                        "lon": city["lon"],
                        "temp": round(data["main"]["temp"]),
                        "humidity": data["main"]["humidity"],
                        "wind": format_wind(data["wind"]["speed"], data["wind"]["deg"]),
                        "localtime": data["dt"]+data["timezone"],
                        "description": data["weather"][0]["description"].title()
                    }
            except Exception as e:
                print(f"An error occurred accessing the API: {e}", flush=True)
                return
    update_weather.count = (update_weather.count + 1) % (BATCHES)

update_weather.count = 0


@app.on_event("startup")
async def startup_event():
    scheduler.add_job(update_weather, DateTrigger(run_date=datetime.now()))
    scheduler.add_job(update_weather, IntervalTrigger(minutes=API_QUERY_INTERVAL))
    scheduler.start()


@app.on_event("shutdown")
async def shutdown_event():
    scheduler.shutdown()
