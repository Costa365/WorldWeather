# World Weather Map Application

This project is a web application that displays the weather and temperature of major world cities on an interactive map. It uses FastAPI for the backend, HTMX for dynamic content loading, and Leaflet.js for map rendering.

## Features

- Real-time weather data for major world cities
- Interactive map with weather information popups
- Asynchronous data loading with HTMX
- Dockerized application for easy deployment

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Docker and Docker Compose installed on your system
- An OpenWeatherMap API key (sign up at [OpenWeatherMap](https://openweathermap.org/api))

## Setup

1. Clone this repository to your local machine:

   ```
   git clone https://github.com/costa365/WeatherMap.git
   cd WeatherMap
   ```

2. Create a `.env` file in the project root and add your OpenWeatherMap API key:

   ```
   OPENWEATHERMAP_API_KEY=your_api_key_here
   ```

3. Build and start the Docker containers:

   ```
   docker-compose up --build
   ```

4. Once the containers are running, open your web browser and navigate to `http://localhost:8000` to view the application.

## Project Structure

```
world-weather-map/
├── main.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env
├── README.md
├── static/
│   └── .gitkeep
└── templates/
    └── index.html
```

## Usage

The application will display a world map with markers for major cities. Click on a marker to view the current temperature and weather description for that city.

## Contributing

Contributions to this project are welcome. Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/)
- [HTMX](https://htmx.org/)
- [Leaflet.js](https://leafletjs.com/)
- [OpenWeatherMap API](https://openweathermap.org/api)

