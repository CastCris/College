from begin.xtensions import *
from begin.globals import Router, Seeds

from database.session import *

import time

##
app = flask.Flask(__name__)

time_init = time.time()
Seeds.cultivate()
time_end = time.time()


Router.register(app)

if __name__ == '__main__':
    print('Seeds runtime: ', time_end - time_init)
    app.run(debug=True, host='0.0.0.0', port=5000)
