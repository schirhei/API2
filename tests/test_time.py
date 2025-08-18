from tests.constants import dawn_example, day_example, dusk_example, night_example
from controllers.time_controller import get_time_of_day, get_sun_times
from models.SunTimes import SunTimes


def test_get_sun_times():
    sun_times = get_sun_times(0, 0)
    assert type(sun_times) is SunTimes

def test_get_time_of_day_dawn():
    time_of_day = get_time_of_day(dawn_example)
    assert time_of_day == 'dawn'

def test_get_time_of_day_day():
    time_of_day = get_time_of_day(day_example)
    assert time_of_day == 'day'

def test_get_time_of_day_dusk():
    time_of_day = get_time_of_day(dusk_example)
    assert time_of_day == 'dusk'

def test_get_time_of_day_night():
    time_of_day = get_time_of_day(night_example)
    assert time_of_day == 'night'
    