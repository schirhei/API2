from fastapi import FastAPI
import uvicorn
import requests
from datetime import datetime, timezone

app = FastAPI()


@app.get("/night-time-temperature")
async def get_night_time_temperature(lat, lng):
    sun_events = get_sun_events()
    now = datetime.now().time()
    temperature = get_temperature(now, sun_events)
    return {"temperature": temperature}


def get_sun_events():
    response = requests.get('http://api.sunrise-sunset.org/json?lat={lat}&lng={lng}&formatted=0').json()
    sun_events = {}
    sun_events['sunrise'] = datetime.strptime(response['results']['sunrise'], "%Y-%m-%dT%H:%M:%S%z").time()
    sun_events['sunset'] = datetime.strptime(response['results']['sunset'], "%Y-%m-%dT%H:%M:%S%z").time()
    sun_events['astronomical_twilight_begin'] = datetime.strptime(response['results']['astronomical_twilight_begin'], "%Y-%m-%dT%H:%M:%S%z").time()
    sun_events['astronomical_twilight_end'] = datetime.strptime(response['results']['astronomical_twilight_end'], "%Y-%m-%dT%H:%M:%S%z").time()
    return sun_events


def get_temperature(now, sun_events):
    if (sun_events['sunrise'] < now < sun_events['sunset']):
        #if now is during the day
        temperature = 6000
    elif (sun_events['astronomical_twilight_begin'] < now < sun_events['sunrise']):
        # if now is during dawn
        twilight_total = (sun_events['sunrise'].hour - sun_events['astronomical_twilight_begin'].hour) * 3600 + \
                         (sun_events['sunrise'].minute - sun_events['astronomical_twilight_begin'].minute) * 60 + \
                         (sun_events['sunrise'].second - sun_events['astronomical_twilight_begin'].second)
        
        sunrise_progress = (now.hour - sun_events['astronomical_twilight_begin'].hour) * 3600 + \
                           (now.minute - sun_events['astronomical_twilight_begin'].minute) * 60 + \
                           (now.second - sun_events['astronomical_twilight_begin'].second)
        
        temperature = int(2700 + (sunrise_progress / (twilight_total / 3300)))
    elif (sun_events['sunset'] < now < sun_events['astronomical_twilight_end']):
        # if now is at dusk
        twilight_total = (sun_events['astronomical_twilight_end'].hour - sun_events['sunset'].hour) * 3600 + \
                         (sun_events['astronomical_twilight_end'].minute - sun_events['sunset'].minute) * 60 + \
                         (sun_events['astronomical_twilight_end'].second - sun_events['sunset'].second)
        
        sunset_progress = (now.hour - sun_events['sunset'].hour) * 3600 + \
                          (now.minute - sun_events['sunset'].minute) * 60 + \
                          (now.second - sun_events['sunset'].second)
        
        temperature = int(6000 - (sunset_progress / (twilight_total / 3300)))
    else:
        # if now is at night
        temperature = 2700

    return temperature

if __name__ == "__main__":
    uvicorn.run(app)

