import os
import uuid
from flask import Flask

#update on Thursday morning

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
      <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <!-- Latest compiled and minified CSS -->
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">
      </head>
      <body>
        <div class="container-fluid">
            <div class="col-sm-12" style="background-image:url(static/cloud.png)" align="center">
            <h1>Dell Technologies SE Conference</h3>
            <p>The Best presales conference - ever!</p>
        </div>

        <div class="col-sm-6" align="center">
            <h2>Agenda</h2>
            <p>This will help you</p>
            <p>plan your day</p>
            <a href="agenda.html"><img src="static/agenda icon.png" width="100" height="100"></a>
        </div>

        <div class="col-sm-6" align="center">
            <h2>Floor plan</h2>
            <p>Get directions to your</p>
            <p>favourite sessions</p>
            <a href="floorplan.html"><img src="static/map icon.png" width="100" height="100"></a>
        </div>
        
    </div>
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
