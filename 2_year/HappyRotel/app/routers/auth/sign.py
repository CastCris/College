from begin.xtensions import flask

##
def register_app(app:object)->None:

    @app.route("/sign/display")
    def sign_display()->object:
        return flask.render_template('sign.html')

    @app.route("/sign/auth")
    def sign_auth()->object:
        return '{}'
