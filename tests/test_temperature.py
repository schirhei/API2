from tests.constants import dawn_example, dusk_example
from controllers.temperature_controller import get_dawn_temperature, get_day_temperature, get_dusk_temperature, get_night_temperature

def test_get_dawn_temperature():
    temperature = get_dawn_temperature(dawn_example)
    assert temperature == 3373

def test_get_day_temperature():
    temperature = get_day_temperature()
    assert temperature == 6000

def test_get_dusk_temperature():
    temperature = get_dusk_temperature(dusk_example)
    assert temperature == 4670

def test_get_night_temperature():
    temperature = get_night_temperature()
    assert temperature == 2700