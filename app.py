# ---- Flask Hello World ---- #

# import the Flask class from the flask package
from flask import Flask


# Config.
TOKEN = 'demo+7832657@calendar42.com/0fde9f26fe8bf272cbc1336218999b620abe98b8/'
EVENT_ID = '1d2e3220f23ec79c8b547302d1deabe9_14770730218531'


# Create the application object.
app = Flask(__name__)


@app.route("/")
@app.route("/hello")
# define the view using a function, which returns a string
def hello_world():
    return "Hello, World!, radu "


# dynamic route
@app.route("/test/<search_query>")
def search(search_query):
    return search_query


@app.route('/events-with-subscriptions/<EVENT_ID>/')
def events_with_subscriptions(EVENT_ID):
    """Func docs here."""
    return EVENT_ID


# start the development server using the run() method
if __name__ == "__main__":
    app.run()
