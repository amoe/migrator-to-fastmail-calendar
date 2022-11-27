import datetime
from google_calendar_auth_boilerplate import authboilerplate
import json

service = authboilerplate()

now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time

collection = []
next_page_token = None

while True:
    fields = {
        'calendarId': 'primary',
        'maxResults': 2500,
        'singleEvents': False,
#        'timeMin': now,
#        'orderBy': 'startTime',
#        'maxTime': now
    }

    if next_page_token:
        fields['pageToken'] = next_page_token

    print("Doing request")
    events_result = service.events().list(**fields).execute()
    collection.extend(events_result.get('items'))
    
    next_page_token = events_result.get('nextPageToken')
    if not next_page_token:
        break

    
# Prints the start and name of the next 10 events
print("Size of result =", len(collection))

with open('out.json', 'w') as f:
    json.dump(collection, f)

# for event in collection:
#     print(event)
#     start = event['start'].get('dateTime', event['start'].get('date'))
#     print(start, event['summary'])
