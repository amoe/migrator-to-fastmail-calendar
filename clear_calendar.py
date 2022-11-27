import caldav
import pdb
from datetime import datetime, timedelta, date
from icalendar.prop import vDuration
import json
import mapcal

# Needs the pip3 version of caldav not the debian version.

# url = 'https://caldav.fastmail.com/dav/principals/user/amoe@solasistim.net/'
url = 'https://caldav.fastmail.com/dav/'


fastmail_username = os.environ['FASTMAIL_USERNAME']
fastmail_password = os.environ['FASTMAIL_PASSWORD']

with caldav.DAVClient(url=url, username=fastmail_username, password=fastmail_password) as client:
    my_principal = client.principal()

    calendars = my_principal.calendars()
    the_c = [c for c in calendars if c.name == 'Main'][0]
    for i, e in enumerate(the_c.events()):
        print("Deleting event", i)
        e.delete()
