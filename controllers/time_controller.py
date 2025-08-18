import requests
from datetime import datetime, timezone
from models.SunTimes import SunTimes

def get_sun_times(lat, lng):
    response = requests.get(f'http://api.sunrise-sunset.org/json?lat={lat}&lng={lng}&formatted=0').json()
    sun_times = SunTimes(sunrise=datetime.strptime(response['results']['sunrise'], "%Y-%m-%dT%H:%M:%S%z"),
                         sunset=datetime.strptime(response['results']['sunset'], "%Y-%m-%dT%H:%M:%S%z"),
                         astronomical_twilight_begin=datetime.strptime(response['results']['astronomical_twilight_begin'], "%Y-%m-%dT%H:%M:%S%z"),
                         astronomical_twilight_end=datetime.strptime(response['results']['astronomical_twilight_end'], "%Y-%m-%dT%H:%M:%S%z"),
                         now=datetime.now(timezone.utc))
    return sun_times

def get_time_of_day(sun_times):
    if (sun_times.sunrise < sun_times.now < sun_times.sunset):
        time_of_day = "day"
    elif (sun_times.astronomical_twilight_begin < sun_times.now < sun_times.sunrise):
        time_of_day = "dawn"
    elif (sun_times.sunset < sun_times.now < sun_times.astronomical_twilight_end):
        time_of_day = "dusk"
    elif (sun_times.astronomical_twilight_end < sun_times.now or sun_times.now < sun_times.astronomical_twilight_begin):
        time_of_day = "night"
    else:
        raise ValueError
    return time_of_day

