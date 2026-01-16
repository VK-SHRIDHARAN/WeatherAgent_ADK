from fastapi import FastAPI
from agent import WeatherAgent

app = WeatherAgent().get_app()
