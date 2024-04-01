import json
import random

from flask import Flask

app = Flask(__name__)

@app.route('/random')
def get_random():
    rand_num = random.randint(6,6)
    the_dictionary = {}
    the_dictionary['version']=0
    the_dictionary['rand']=rand_num

    return json.dumps(the_dictionary)

if __name__ == '__main__':
    app.run(port=5000)
