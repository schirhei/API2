from pydantic import BaseModel
from datetime import datetime

class SunTimes(BaseModel):
    sunrise: datetime
    sunset: datetime
    astronomical_twilight_begin: datetime
    astronomical_twilight_end: datetime
    now: datetime
