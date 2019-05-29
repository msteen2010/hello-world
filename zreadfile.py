file = open("sessions.txt", "r")
for line in file:
    field = line.split(",")
    session_id = field[0]
    session_name  = field[1]
    session_time  = field[2]
    session_presenter  = field[3]
    session_description  = field[4]
    print(session_id + " " + session_name + " " + session_time + " " + session_presenter + " " + session_description) 
