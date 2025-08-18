from controllers.time_controller import get_time_of_day

hour_in_seconds = 3600
minute_in_seconds = 60

def get_temperature(sun_times):
    time_of_day = get_time_of_day(sun_times)
    if (time_of_day == "day"):
        temperature = get_day_temperature()
    elif (time_of_day == "dawn"):
        temperature = get_dawn_temperature(sun_times)
    elif (time_of_day == "dusk"):
        temperature = get_dusk_temperature(sun_times) 
    elif (time_of_day == "night"):
        temperature = get_night_temperature()

    return temperature

def get_day_temperature():
    return 6000

def get_night_temperature():
    return 2700

def get_dawn_temperature(sun_times):
    twilight_total = (sun_times.sunrise.hour - sun_times.astronomical_twilight_begin.hour) * hour_in_seconds + \
                         (sun_times.sunrise.minute - sun_times.astronomical_twilight_begin.minute) * minute_in_seconds + \
                         (sun_times.sunrise.second - sun_times.astronomical_twilight_begin.second)
        
    sunrise_progress = (sun_times.now.hour - sun_times.astronomical_twilight_begin.hour) * hour_in_seconds + \
                        (sun_times.now.minute - sun_times.astronomical_twilight_begin.minute) * minute_in_seconds + \
                        (sun_times.now.second - sun_times.astronomical_twilight_begin.second)

    temperature = int(get_night_temperature() + (sunrise_progress / (twilight_total / (get_day_temperature() - get_night_temperature()))))
    return temperature

def get_dusk_temperature(sun_times):
    twilight_total = (sun_times.astronomical_twilight_end.hour - sun_times.sunset.hour) * hour_in_seconds + \
                         (sun_times.astronomical_twilight_end.minute - sun_times.sunset.minute) * minute_in_seconds + \
                         (sun_times.astronomical_twilight_end.second - sun_times.sunset.second)
        
    sunset_progress = (sun_times.now.hour - sun_times.sunset.hour) * hour_in_seconds + \
                        (sun_times.now.minute - sun_times.sunset.minute) * minute_in_seconds + \
                        (sun_times.now.second - sun_times.sunset.second)

    temperature = int(get_day_temperature() - (sunset_progress / (twilight_total / (get_day_temperature() - get_night_temperature()))))
    return temperature