"""Solution for Calendar 24 assignment."""

import requests

from flask import Flask, jsonify
from flask_caching import Cache


# Config.
TOKEN = 'Token 0fde9f26fe8bf272cbc1336218999b620abe98b8'

# Create the application object.
app = Flask(__name__)

# Cache setup
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

# error handling
app.config["DEBUG"] = True


@app.route("/")
def hello_world():
    return "Hello, World!"


def get_event_subscriptions(event_id):
    """Helper func for "events_with_subscriptions".
    Returns list of dicts.
    """

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
        if resp.status_code == 200:
            event_det = resp.json().get('data')
            return event_det
        else:
            raise ValueError('No data')


def get_event_details(event_id):
    """Helper func for "events_with_subscriptions".
    Returns event details dict.
    """

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
# cache for 4.2 minutes
@cache.cached(timeout=4.2 * 60)
def events_with_subscriptions(event_id):
    """Return events with subscriptions as JSON."""

    try:
        event_details = get_event_details(event_id)
    except ValueError:
        print('Error while getting EVENT DETAILS: ', event_id)
        return "Event Details Not Found", 404
    else:
        # Do stuff with data.
        _id = event_details.get('id')
        title = event_details.get('title')

    try:
        event_subs = get_event_subscriptions(event_id)
    except ValueError:
        print('Error while getting EVENT SUBSCRIPTIONS for event ', event_id)
        return "Event Subscriptions Not Found", 404
    else:
        # Get list of names from all subscriptions objects.
        names_u = [
            ea_obj.get('subscriber').get('first_name') for ea_obj in event_subs
        ]

    names = [str(x) for x in names_u]
    res = dict(
        id=_id,
        title=title,
        names=names
    )
    return jsonify(res)


# start the development server
if __name__ == "__main__":
    app.run()
