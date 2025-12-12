from begin.xtensions import flask
from begin.globals import flask_auth

##
def register_app(app:object)->None:

    @app.route("/login/required")
    @flask_auth.login_required
    def login_required()->object:
        return "You have permission to access this page!"
