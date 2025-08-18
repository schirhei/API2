from datetime import datetime
from models.SunTimes import SunTimes

dawn_example = SunTimes(sunrise=datetime.strptime('2025-08-18T17:36:33+00:00', "%Y-%m-%dT%H:%M:%S%z"),
                        sunset=datetime.strptime('2025-08-19T05:10:12+00:00', "%Y-%m-%dT%H:%M:%S%z"),
                        astronomical_twilight_begin=datetime.strptime('2025-08-18T16:23:49+00:00', "%Y-%m-%dT%H:%M:%S%z"),
                        astronomical_twilight_end=datetime.strptime('2025-08-19T06:22:56+00:00', "%Y-%m-%dT%H:%M:%S%z"),
                        now=datetime.strptime('2025-08-18T16:38:39+00:00', "%Y-%m-%dT%H:%M:%S%z"))

day_example = SunTimes(sunrise=datetime.strptime('2025-08-18T10:08:07+00:00', "%Y-%m-%dT%H:%M:%S%z"),
                        sunset=datetime.strptime('2025-08-18T15:46:36+00:00', "%Y-%m-%dT%H:%M:%S%z"),
                        astronomical_twilight_begin=datetime.strptime('2025-08-18T08:27:47+00:00', "%Y-%m-%dT%H:%M:%S%z"),
                        astronomical_twilight_end=datetime.strptime('2025-08-19T01:31:12+00:00', "%Y-%m-%dT%H:%M:%S%z"),
                        now=datetime.strptime('2025-08-18T12:19:06+00:00', "%Y-%m-%dT%H:%M:%S%z"))

dusk_example = SunTimes(sunrise=datetime.strptime('2025-08-18T02:26:07+00:00', "%Y-%m-%dT%H:%M:%S%z"),
                        sunset=datetime.strptime('2025-08-18T15:46:36+00:00', "%Y-%m-%dT%H:%M:%S%z"),
                        astronomical_twilight_begin=datetime.strptime('2025-08-18T00:58:10+00:00', "%Y-%m-%dT%H:%M:%S%z"),
                        astronomical_twilight_end=datetime.strptime('2025-08-18T17:14:34+00:00', "%Y-%m-%dT%H:%M:%S%z"),
                        now=datetime.strptime('2025-08-18T16:22:03+00:00', "%Y-%m-%dT%H:%M:%S%z"))

night_example = SunTimes(sunrise=datetime.strptime('2025-08-18T14:39:58+00:00', "%Y-%m-%dT%H:%M:%S%z"),
                        sunset=datetime.strptime('2025-08-19T04:06:10+00:00', "%Y-%m-%dT%H:%M:%S%z"),
                        astronomical_twilight_begin=datetime.strptime('2025-08-18T13:08:50+00:00', "%Y-%m-%dT%H:%M:%S%z"),
                        astronomical_twilight_end=datetime.strptime('2025-08-19T05:37:18+00:00', "%Y-%m-%dT%H:%M:%S%z"),
                        now=datetime.strptime('2025-08-18T10:19:44+00:00', "%Y-%m-%dT%H:%M:%S%z"))
