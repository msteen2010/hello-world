import os
import uuid
from flask import Flask

app = Flask(__name__)
my_uuid = str(uuid.uuid1())

BLUE = "#777799"
GREEN = "#99CC99"

COLOR = BLUE

file = open("sessions.txt", "r")
sessions = file.readlines()
file.close

@app.route('/')
def mainmenu():

    return """
    <html>
    <body bgcolor="{}">
    <center><h1><font color="white">Dell Technologies SE Conference</h1>
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

    mid_html = ""

    for line in sessions:
        field = line.split(",")
        session_id = field[0]
        session_name  = field[1]
        session_time  = field[2]
        session_presenter  = field[3]
        session_description  = field[4]
        mid_html += "<tr><th>" + session_id + "</th><th>" + session_name + "</th><th>" + session_time + "</th><th>" + session_presenter + "</th><th>" + session_description + "</th></tr>"

    begin_html = """
    <html>
    <body>
    <h1><u>Event Agenda</u></h1>
    <table style="width:100%">
     """

    end_html = """
    </table>
    <br></br>
    <a href="/">Return to main menu</a>
    <br></br>
     Hi, I'm GUID: {}
    </body>
    </html>
    """

    webpage = begin_html + mid_html + end_html

    return webpage.format(COLOR,my_uuid,)

if __name__ == "__main__":
	app.run(debug=False,host='0.0.0.0', port=int(os.getenv('PORT', '5000')))
