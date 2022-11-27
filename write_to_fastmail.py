import os
import caldav
import pdb
from datetime import datetime, timedelta, date
from icalendar.prop import vDuration
import json
import mapcal



# Needs the pip3 version of caldav not the debian version.

# url = 'https://caldav.fastmail.com/dav/principals/user/amoe@solasistim.net/'
url = 'https://caldav.fastmail.com/dav/'

# my_event = my_new_calendar.save_event(
#     dtstart=datetime.datetime(2020,5,17,8),
#     dtend=datetime.datetime(2020,5,18,1),
#     summary="Do the needful",
#     rrule={'FREQ': 'YEARLY'))


fastmail_username = os.environ['FASTMAIL_USERNAME']
fastmail_password = os.environ['FASTMAIL_PASSWORD']

with caldav.DAVClient(url=url, username=fastmail_username, password=fastmail_password) as client:
    my_principal = client.principal()

    calendars = my_principal.calendars()
    the_c = [c for c in calendars if c.name == 'Main'][0]


# BEGIN:VCALENDAR
# VERSION:2.0
# CALSCALE:GREGORIAN
# PRODID:-//CyrusIMAP.org/Cyrus 
#  3.7.0-alpha0-1115-g8b801eadce-fm-20221102.001-g8b801ead//EN
# BEGIN:VEVENT
# UID:836cd37f-4832-4fb8-8a1d-c98accbb7575
# SEQUENCE:0
# DTSTAMP:20221111T073200Z
# CREATED:20221111T073200Z
# DTSTART;VALUE=DATE:20221116
# DURATION:P1D
# PRIORITY:0
# SUMMARY:Dave's event
# STATUS:CONFIRMED
# TRANSP:TRANSPARENT
# X-APPLE-DEFAULT-ALARM;VALUE=BOOLEAN:TRUE
# END:VEVENT
# END:VCALENDAR

    # no need to fuck with durations, just use either 'date' or 'datetime' here.
    
#     event = {
#         'dtstart': date(2022, 11, 18),
#         'color': '#e12162',
#         'summary': "Dave's event from python",
# #        'created': datetime(2022, 11, 18, 1, 2, 3)
#         'duration': vDuration(timedelta(days=1))
#     }

    # event = {
    #     'dtstart': datetime(2022,11,28, 9, 30),
    #     'dtend': datetime(2022,11,29, 11, 30),
    #     'summary': "Dave's multi day event",
    # }
   
    # the_c.save_event(**event)

    new_events = mapcal.get_mapped_calendar()
    for i, event in enumerate(reversed(new_events)):
        print("creating event", i)
        the_c.save_event(**event)

    # for e in events:
    #     print(e.data)
