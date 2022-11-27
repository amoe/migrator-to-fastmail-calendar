import caldav
import pdb
from datetime import datetime, timedelta, date
from icalendar.prop import vDuration
import json
import mapcal

url = 'https://caldav.fastmail.com/dav/'

fastmail_username = os.environ['FASTMAIL_USERNAME']
fastmail_password = os.environ['FASTMAIL_PASSWORD']

with caldav.DAVClient(url=url, username=fastmail_username, password=fastmail_password) as client:
    my_principal = client.principal()

    calendars = my_principal.calendars()
    the_c = [c for c in calendars if c.name == 'Main'][0]

    for e in the_c.events():
         print(e.data)
