from begin.xtensions import flask
from begin.globals import flask_auth, CookieSession

##
def register_app(app:object, **kwargs)->None:
    managerUser = kwargs.get("managerUser")

    @app.route("/logout/auth")
    @managerUser.required_login
    def logout_auth(pkUser)->object:
        response = flask.make_response(flask.redirect("/"))
        CookieSession.delete_all(response)
    
        managerUser.logout()
        return response
