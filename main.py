from fastapi import FastAPI
import uvicorn

from controllers.time_controller import get_sun_times
from controllers.temperature_controller import get_temperature

app = FastAPI()

@app.get("/night-time-temperature")
async def get_night_time_temperature(lat, lng):
    sun_events = get_sun_times(lat, lng)
    temperature = get_temperature(sun_events)
    return {"temperature": temperature}

if __name__ == "__main__":
    uvicorn.run(app)

