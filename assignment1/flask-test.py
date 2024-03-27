# This is a very simple program to test that the Flask and JSON packages are correctly installed

import flask
import json

app = flask.Flask(__name__)

@app.route('/do-stuff/<input>')
def my_function(input):
    the_dictionary = {}
    the_dictionary['name']='Matt'
    the_dictionary['stuff']=input

    return json.dumps(the_dictionary)

if __name__ == '__main__':
    host = 'localhost'
    port = 5555
    app.run(host=host, port=port, debug=True)
