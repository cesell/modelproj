""" timezone.py is based on Real Python book.  It explains how to use time and timezones to stamp events.
"""
import datetime
from dateutil import tz
from dateutil.zoneinfo import get_zonefile_instance


def add_tz(dt: datetime, zone: str) -> datetime:
    """add_tz datetime doesnt assign a time zone.  This function shows how to do it.

    Args:
        dt (datetime): original datetime
        zone (str): desired zone 

    Returns:
        datetime: a new datetime with the zone assigned
    """

    return dt.replace(tzinfo=tz.gettz(zone))


if __name__ == '__main__':

    now = datetime.datetime.now()
    now_with_tz = add_tz(now, 'Europe/Paris')
    print(
        f'Date and Time = {now_with_tz},\nassigned time zone = {now_with_tz.tzinfo}')
    print(f'Date and Time={now} \nlocal time zone = {tz.gettz().tzname(now)}')
    zones = list(get_zonefile_instance().zones)
    print('Other zones', sorted(zones)[:5])
