# In this silly game there are two numbers, one blue, one red
# Players click buttons to make the numbers go up or down
# The server stores the numbers and returns them when the browser asks for them

# The javascript code in the "static" directory
#  is run by the browser and periodically requests updates
#  to the red and blue numbers
#  by invoking the /getupdate/ API endpoint 

from flask import Flask
from flask import render_template
import json

app = Flask(__name__)

red_number = 1
blue_number = 1

@app.route('/')
def homepage():
    return render_template("number-game.html")

#Returns the state of the Game with the given Game Number
@app.route('/getupdate/')
def returnNumbers():
    global red_number
    global blue_number

    my_dict = {}
    my_dict['red'] = red_number
    my_dict['blue'] = blue_number 

    return json.dumps(my_dict)

#Updates the blue number +1
@app.route('/blueUp/')
def blue_up():
    global blue_number

    blue_number += 1
    return blue_number

    
#Updates the blue number -1
@app.route('/blueDown/')
def blue_down():
    global blue_number

    blue_number -= 1
    return blue_number

#Updates the red number +1
@app.route('/redUp/')
def red_up():
    global red_number

    red_number += 1
    return red_number


#Updates the red number -1
@app.route('/redDown/')
def red_down():
    global red_number

    red_number -= 1
    return red_number

# This flask server will use port 5555
if __name__ == '__main__':
    my_port = 5555
    app.run(host='0.0.0.0', port = my_port) 
