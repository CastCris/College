from begin.xtensions import flask
from begin.globals import flask_auth

##
def register_app(app:object, **kwargs)->None:
    managerUser = kwargs.get("managerUser")

    @app.route("/logout/auth")
    @managerUser.required_login
    def logout_auth(pkUser)->object:
        from begin.globals import Cookie

        ##
        response = flask.make_response(flask.redirect("/"))
        for i in flask.request.cookies.keys():
            Cookie.delete(response, i)
    
        managerUser.logout()

        return response
