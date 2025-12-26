from begin.xtensions import flask
from begin.globals import ManagerUser, CookieSession

##
def register_app(app:object, **kwargs)->None:
    @app.route("/logout/auth")
    @ManagerUser.required_login
    def logout_auth(pkUser)->object:
        response = flask.make_response(flask.redirect("/"))
        CookieSession.delete_all(response)
    
        ManagerUser.logout()
        return response
