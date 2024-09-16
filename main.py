# main.py
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from cities import cities
import httpx
import os
import threading

from pathlib import Path

app = FastAPI()

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


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/get-weather")
async def get_weather():
    if not weather_data:
        async with httpx.AsyncClient() as client:
            for city in cities:
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
                        "description": data["weather"][0]["description"]
                    }
    return list(weather_data.values())


def start_server():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    server_thread = threading.Thread(target=start_server)
    server_thread.start()
