# calendar42- Solution for the calendar24 assignment.

I will use Flask.# calendar42-

Requirement.
_A. Get the event details (including title)_
```

curl --request GET \
--header "Accept: application/json" \
--header "Content-type: application/json" \
--header "Authorization: Token $TOKEN" \
"https://demo.calendar42.com/api/v2/events/$EVENT_ID/" 

Test.

TOKEN = '0fde9f26fe8bf272cbc1336218999b620abe98b8'
EVENT_ID = '1d2e3220f23ec79c8b547302d1deabe9_14770730218531'

curl --request GET \
--header "Accept: application/json" \
--header "Content-type: application/json" \
--header "Authorization: Token 0fde9f26fe8bf272cbc1336218999b620abe98b8" \
"https://demo.calendar42.com/api/v2/events/1d2e3220f23ec79c8b547302d1deabe9_14770730218531/"


_B. Get the event subscriptions (participants including the name)_
```

curl --request GET \
--header "Accept: application/json" \   
--header "Content-type: application/json" \
--header "Authorization: Token 0fde9f26fe8bf272cbc1336218999b620abe98b8" \
--globoff \
"https://demo.calendar42.com/api/v2/event-subscriptions/?event_ids=[1d2e3220f23ec79c8b547302d1deabe9_14770730218531]"
