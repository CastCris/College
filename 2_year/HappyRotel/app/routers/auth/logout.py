from begin.xtensions import flask
from begin.globals import flask_auth

##
def register_app(app:object)->None:

    @app.route("/logout/auth")
    @flask_auth.login_required
    def logout_auth(pkUser)->object:
        from begin.globals import Cookie

        ##
        response = flask.make_response(flask.redirect("/"))
        for i in flask.request.cookies.keys():
            Cookie.delete(response, i)
    
        flask_auth.logout()

        return response
