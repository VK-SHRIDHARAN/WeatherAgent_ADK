import requests
from google.adk.tools.base_tool import BaseTool
from pydantic import BaseModel, Field
import os

# Load API key from environment
OPEN_WEATHER_KEY = os.getenv("OPEN_WEATHER_KEY")

class WeatherInput(BaseModel):
    city: str = Field(..., description="City name to fetch weather")

class WeatherTool(BaseTool):
    name: str = "weather_tool"
    description: str = "Get current weather for any city"

    args_schema = WeatherInput

    def run(self, args: WeatherInput):
        if not OPEN_WEATHER_KEY:
            return "API key not found. Please set OPEN_WEATHER_KEY in .env"

        url = (
            f"https://api.openweathermap.org/data/2.5/weather?q={args.city}"
            f"&appid={OPEN_WEATHER_KEY}&units=metric"
        )

        r = requests.get(url)
        data = r.json()

        if data.get("cod") != 200:
            return f"Error: {data.get('message')}"

        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]

        return f"Weather in {args.city}: {temp}°C, {desc}"
