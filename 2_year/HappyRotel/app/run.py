from begin.xtensions import *
from begin.globals import Router

from database.session import *

##
app = flask.Flask(__name__)

Router.register(app)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
