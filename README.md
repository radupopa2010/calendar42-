# calendar42- Solution for the calendar24 assignment.

I will use Flask.# calendar42-

_A. Get the event details (including title)_
```
curl --request GET \
--header "Accept: application/json" \
--header "Content-type: application/json" \
--header "Authorization: Token $TOKEN" \
"https://demo.calendar42.com/api/v2/events/$EVENT_ID/" 