import os
import uuid
from flask import Flask

app = Flask(__name__)
my_uuid = str(uuid.uuid1())

BLUE = "#777799"
GREEN = "#99CC99"

COLOR = BLUE

@app.route('/')
def mainmenu():

    return """
    <html>
    <center><h1><font color="white">Dell Technologies SE</h1>
    <a href="floorplan.html">Show floor plan</a>
    <br>
    <a href="agenda.html">The Agenda</a>
    </br>
    </center>
    </body>
    </html>
    """.format(COLOR,my_uuid,)

@app.route('/floorplan.html')
def floorplan():

    return """
    <html>
    <body bgcolor="{}">
    <img src="/static/floorplan.jpg">
    <br></br>
    <a href="/">Return to main menu</a>
    </body>
    </html>
    """.format(COLOR,my_uuid,)

@app.route('/agenda.html')
def agenda():

    return """
    <html>
    <body>
     <h1><u>Event Agenda</u></h1>
     <h2>
     <ul>
       <li>09:00 - The wornderful world of Cloud Native
       <li>10:00 - DevOps demystified
       <li>11:00 - Agile for Dummies
     </ul>
     </h2>
    <br></br>
    <a href="/">Return to main menu</a>
    <br></br>
     Hi, I'm GUID: {}
    </body>
    </html>
    """.format(COLOR,my_uuid,)

if __name__ == "__main__":
	app.run(debug=False,host='0.0.0.0', port=int(os.getenv('PORT', '5000')))
