# In this silly game there are two numbers, one blue, one red
# Players click buttons to make the numbers go up or down
# The server stores the numbers and returns them when the browser asks for them

# The javascript code in the "static" directory
#  is run by the browser and periodically requests updates
#  to the red and blue numbers
#  by invoking the /getupdate/ API endpoint

# We use Flask support for Websockets to faciliate two-way communication

from flask import Flask
from flask import render_template
from flask_sock import Sock
from threading import Lock
import json
import sys
import time
import random

app = Flask(__name__)

# Setup Web Sockets for this app
sock = Sock(app)

#Dictionary of Room Data
#The dictionary key is the room number
# ... the dictionary value is another dictionary (to be converted into JSON)
# ... the inner dictionary has keys 'red', 'blue', and 'names'
room_data = {}

#Dictionary of Web Sockets
#The dictionary key is a pair (room_num, player_name)
# ... the dictionary value is a WebSocket object for that room/player pair
web_sockets = {}

@app.route('/')
def homepage():
    return render_template("homepage.html")

#Requests a Room Number of a Room for the player to join
@app.route('/requestRoomNum/<name>')
def requestRoom(name):
    done = False

    # Pick a random Room number
    # Check and make sure that player name isn't already in the room
    while (not done):
        room_num = random.randint(1,9)
        if room_num in room_data:
            data_dict = room_data[room_num]
            if (name in data_dict['names']):
                done = False
            else:
                done = True
        else:
            done = True
        
    my_dict = {}
    my_dict['num'] = str(room_num)

    return json.dumps(my_dict)


#Route to Display a Game Room
#<num> is the room number, <name> is the player's name
@app.route('/gameRoom/<num>/<name>')
def gameRoom(num, name):
    global room_data
    
    #initialize the room data if it doesn't exist
    if not (num in room_data):
        data = {}
        data['red'] = 1
        data['blue'] = 1
        data['names'] = [ name ]
        room_data[num] = data
    else:
        data = room_data[num]
        data['names'].append(name)

    notify_sockets(num)

    return render_template("number-game.html")



#Returns the state of the Game with the given Room Number
@app.route('/getupdate/<num>')
def returnData(num):
    global room_data

    if num in room_data:
        data_dict = room_data[num]
    else:
        data_dict = { 'red':'0', 'blue':'0', 'names':[] } 
        
    return json.dumps(data_dict)


#Updates the blue number +1
@app.route('/blueUp/<num>')
def blue_up(num):
    global room_data

    room_dict = room_data[num]

    room_dict['blue'] += 1

    notify_sockets(num)

    return json.dumps(room_dict)

    
#Updates the blue number -1
@app.route('/blueDown/<num>')
def blue_down(num):
    global room_data

    room_dict = room_data[num]

    room_dict['blue'] -= 1

    notify_sockets(num)

    return json.dumps(room_dict)

#Updates the red number +1
@app.route('/redUp/<num>')
def red_up(num):
    global room_data

    room_dict = room_data[num]

    room_dict['red'] += 1

    notify_sockets(num)

    return json.dumps(room_dict)


#Updates the red number -1
@app.route('/redDown/<num>')
def red_down(num):
    global room_data

    room_dict = room_data[num]

    room_dict['red'] -= 1

    notify_sockets(num)

    return json.dumps(room_dict)


#This function tries to notify each of the browser clients
# It is called whenever anything has changed and the browsers need to update
def notify_sockets(room):
    global web_sockets

    dead_sockets = []
    
    for num, name  in web_sockets:
        ws = web_sockets[(num, name)]
        if num == room:
            try:
                ws.send("Update")
            except:
                dead_sockets.append( (num,name) )
                
    for num, name in dead_sockets:
        leave_room(num,name)

                
# This funciton is called when a player leaves a room 
@app.route('/leaveroom/<num>/<name>')
def leave_room(num, name):
    global web_sockets
    global room_data
    
    #Remove the WebSocket from the global dictionary
    if (num,name) in web_sockets:
        del web_sockets[(num,name)]

    #Remove the player from the list of names in the room
    if num in room_data:
        data_dict = room_data[num]
        if name in data_dict['names']:
            data_dict['names'].remove(name)

    notify_sockets(num)
    return "Player: " + name + " Left"

                
#This listens for incoming websocket connections
#ws is the varible that stores the web socket object
@sock.route('/openSocket/<num>/<name>')
def open_socket(ws,num,name):
    global web_sockets
    
    #sys.stderr.write("WebSocket Connection Opened! " + num + " " + name + "\n")
    
    # Add this to the global websocket dictionary
    web_sockets[(num,name)]=ws
    
    # We want to keep the socket open as long as the browser client is active
    while True:
        time.sleep(10)
    
    return ""


# This flask server will use port 5555
if __name__ == '__main__':
    my_port = 5555
    app.run(host='0.0.0.0', port = my_port) 
