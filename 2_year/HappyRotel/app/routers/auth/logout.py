from begin.xtensions import flask

##
def register_app(app:object)->None:

    @app.route("/logout/auth")
    def logout_auth()->object:
        from begin.globals import Cookie

        ##
        response = flask.make_response(flask.redirect("/"))
        for i in flask.request.cookies.keys():
            Cookie.delete(response, i)

        return response
