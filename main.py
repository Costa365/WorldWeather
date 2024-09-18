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

from pathlib import Path

app = FastAPI()
scheduler = AsyncIOScheduler()

# Create 'static' directory if it doesn't exist
static_dir = Path("static")
static_dir.mkdir(exist_ok=True)

# Mount the static directory only if it exists and is not empty
if static_dir.exists() and any(static_dir.iterdir()):
    app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

# Get the API key from environment variable
OPENWEATHERMAP_API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")

weather_data = {}

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
    print(f"Updating weather data {update_weather.count}", flush=True)
    async with httpx.AsyncClient() as client:
        for city in cities[update_weather.count*60:(update_weather.count+1)*60]:
            url = f"http://api.openweathermap.org/data/2.5/weather?lat={city['lat']}&lon={city['lon']}&appid={OPENWEATHERMAP_API_KEY}&units=metric"
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
    update_weather.count = (update_weather.count + 1) % 5

update_weather.count = 0

@app.on_event("startup")
async def startup_event():
    scheduler.add_job(update_weather, DateTrigger(run_date=datetime.now()))
    scheduler.add_job(update_weather, IntervalTrigger(minutes=6))
    scheduler.start()


@app.on_event("shutdown")
async def shutdown_event():
    scheduler.shutdown()
