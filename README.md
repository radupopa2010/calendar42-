# Solution for the calendar24 assignment.

To solve this assignment I use Flask.
I've chosen this framework because it's lightweight and because I never had the opportunity to use Django. 

TOKEN = '0fde9f26fe8bf272cbc1336218999b620abe98b8'
EVENT_ID = '1d2e3220f23ec79c8b547302d1deabe9_14770730218531'


## Initail Requirements:
_A. Get the event details (including title)_

```
curl --request GET \
--header "Accept: application/json" \
--header "Content-type: application/json" \
--header "Authorization: Token 0fde9f26fe8bf272cbc1336218999b620abe98b8" \
"https://demo.calendar42.com/api/v2/events/1d2e3220f23ec79c8b547302d1deabe9_14770730218531/"
```

_B. Get the event subscriptions (participants including the name)_
```
curl --request GET \
--header "Accept: application/json" \
--header "Content-type: application/json" \
--header "Authorization: Token 0fde9f26fe8bf272cbc1336218999b620abe98b8" \
--globoff \
"https://demo.calendar42.com/api/v2/event-subscriptions/?event_ids=[1d2e3220f23ec79c8b547302d1deabe9_14770730218531]"
```

_C. Combine and cache results_

_D. Expected final Response on /events-with-subscriptions/$EVENT_ID/_
```
# The combination of the two calls should result in the following JSON data structure
{
"id": "$EVENT_ID",
"title": "Test Event",
"names": ["Bob", "Ella"]
}
```

# View it in action:

1. Clone the repository.

2. Install requirements.

```
pip install -r requirements.txt
```
3. Run the development server:
```
python app.py
```
4. Open the webbrowser
```
http://127.0.0.1:5000/events-with-subscriptions/1d2e3220f23ec79c8b547302d1deabe9_14770730218531/
```