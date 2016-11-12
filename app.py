# ---- Calendar 24 assignment ---- #


import requests
from pprint import pformat

# import the Flask class from the flask package
from flask import Flask


# Config.
TOKEN = 'Token 0fde9f26fe8bf272cbc1336218999b620abe98b8'
EVENT_ID = '1d2e3220f23ec79c8b547302d1deabe9_14770730218531'


# Create the application object.
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World! "


def get_event_subscriptions(event_id):
    """Helper func for "events_with_subscriptions" ."""

    headers = {
        'Accept': 'application/json',
        'Content-type': 'application/json',
        'Authorization': TOKEN
    }
    payload = {'event_ids': str([event_id])}
    http_url = 'https://demo.calendar42.com/api/v2/event-subscriptions/'

    try:
        resp = requests.get(http_url, headers=headers, params=payload)
    except:
        print('GET Request to "Get the event details" FAILED ')
        raise
    else:
        print(resp.status_code)
        # import pdb; pdb.set_trace()
        if resp.status_code == 200:
            event_det = resp.json().get('data')
            return event_det
        else:
            raise ValueError('No data')


def get_event_details(event_id):
    """Helper func for "events_with_subscriptions". """

    headers = {
        'Accept': 'application/json',
        'Content-type': 'application/json',
        'Authorization': TOKEN
    }

    http_url = 'https://demo.calendar42.com/api/v2/events/' + event_id
    try:
        resp = requests.get(http_url, headers=headers)
    except:
        print('GET Request to "Get the event details" FAILED ')
        raise
    else:
        print(resp.status_code)
        # import pdb; pdb.set_trace()
        if resp.status_code == 200:
            event_det = resp.json().get('data')
            if len(event_det) == 1:
                return event_det[0]
            else:
                raise ValueError('Too much data')
        else:
            raise ValueError('No data')


# dynamic route
@app.route('/events-with-subscriptions/<event_id>/')
def events_with_subscriptions(event_id):
    """Func docs here."""

    try:
        event_details = get_event_details(event_id)
    except ValueError:
        print('Error while getting EVENT DETAILS: ', event_id)
        # TODO: see what to retrn if no data is found.
        return
    else:
        # Do stuff with data
        print(pformat(event_details))
        _id = event_details.get('id')
        title = event_details.get('title')

    try:
        event_subs = get_event_subscriptions(event_id)
    except ValueError:
        print('Error while getting EVENT SUBSCRIPTIONS for event ', event_id)
    else:
        names = event_subs

    return 'id = %s , title = %s \n\n %s' % (_id, title, names)


# start the development server using the run() method
if __name__ == "__main__":
    app.run()
