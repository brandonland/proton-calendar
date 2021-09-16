from proton.api import Session, ProtonError
from getpass import getpass
from pprint import pprint
import os
import json


API_BASEURL = 'https://calendar.protonmail.com/api'
CALENDAR_V1 = os.path.join(API_BASEURL, 'calendar/v1')


def start_session():
    global proton_session = Session(
        api_url=api_url,
        appversion="WebCalendar_4.4.7",
        TLSPinning=False,
        user_agent="",
    )

    proton_session.authenticate(input('Username: '), getpass())

    global session_dump = proton_session.dump()
    global session_data = session_dump['session_data']

    if 'twofactor' in session_data['Scope']:
        proton_session.provide_2fa(input('Enter 2FA code: '))
        session_data = session_dump['session_data']

    print('\nSession started!\n')
    pprint(session_dump)


session_file_exists = os.path.exists('./session.json')
session_file_empty =  os.stat('./session.json').st_size == 0

if session_file_exists and not session_file_empty:
    # TODO: Load session by session.json file
    pass
else:
    with open('session.json', 'w') as o:
    o.write(session_json)
    start_session()

global session_json = json.dumps(session_dump, indent=4)


# TODO
def query_calendars():
    req = {
        'url': CALENDAR_V1,
        'method': 'get',
    }
    pass


# TODO
def get_calendar(calendar_id):
    req = {
        'url': f'{CALENDAR_V1}/{calendar_id}',
        'method': 'get',
    }


# TODO
def get_event(calendar_id, event_id):
    req = {
        'url': f'{CALENDAR_V1}/{calendar_id}/events/{event_id}',
        'method': 'get',
    }


# TODO
def create_event(calendar_id, event_data):
    req = {
        'url': f'{CALENDAR_V1}/{calendar_id}/events',
        'method': 'post',
        'data': event_data,
    }


