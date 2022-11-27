import json
import pprint
from datetime import date, datetime
from dateutil import parser

colors = {
    'teal': '#098578',
    'purple': '#9c27b0',
    'yellow': '#e8ae0c',
    'green': '#7cb342',
    'blue': '#2196f3',
    'red': '#d93531',
    'orange': '#f57c00'
}

# if we fail to map then fall back to yellow
mappings = {
    '7': 'blue',
    '5': 'yellow',
    '3': 'yellow',
    '1': 'purple',
    '2': 'green',
    '4': 'yellow',
    '6': 'red',
    '8': 'yellow',
    '9': 'blue',
}




with open('out.json', 'r') as f:
    data = json.load(f)

class ConvertError(Exception):
    pass

#            "dateTime": "2011-07-07T13:00:00+01:00",
#             "date": "2013-06-13"

# Or also ones with start and end dates.



def convert(gcal: dict):
    result = {}
    
    status = gcal['status']
    if status != 'confirmed':
        raise ConvertError(f'unknown status {status}')

    summary = gcal['summary']
    start = gcal['start']
    end = gcal['end']

    result['summary'] = summary

    is_date_based_event = 'date' in start and 'date' in end
    is_datetime_based_event = 'dateTime' in start and 'dateTime' in end

    if not (is_date_based_event ^ is_datetime_based_event):
        raise Exception('weirdly formatted event')

    
    if is_datetime_based_event:
        result['dtstart'] = parser.isoparse(start['dateTime'])
        result['dtend'] = parser.isoparse(end['dateTime'])
    elif 'date' in start:
        result['dtstart'] = date.fromisoformat(start['date'])
        result['dtend'] = date.fromisoformat(end['date'])
    else:
        raise ConvertError(f'unrecognized start {start!r}')

    recurrence = gcal.get('recurrence')
    if recurrence is not None:
        if len(recurrence) != 1:
            raise ConvertError('weird recurrence spec')

        rrule = recurrence[0]
        result['rrule'] = map_rrule(rrule)

    gcal_color = gcal.get('colorId')
    if gcal_color is None:
        result['color'] = colors['red']
    else:
        result['color'] = colors[mappings[gcal_color]]
        
    # except KeyError:
        
    return result

def map_rrule(rrule):
    remaining = rrule.removeprefix('RRULE:')
    pairs = remaining.split(';')
    result = {}
    
    for x in pairs:
        k, v = x.split('=', maxsplit=1)
        if k == 'UNTIL':
            if 'T' in v:
                v = parser.isoparse(v)
            else:
                v = parser.isoparse(v).date()
                
        result[k] = v
        
    return result


def get_mapped_calendar():
    converted = []

    for x in data:
        try:
            y = convert(x)
            converted.append(y)
        except ConvertError as e:
            print(e)

    return converted


if __name__ == '__main__':
    mappedcal = get_mapped_calendar()
    print(mappedcal)
