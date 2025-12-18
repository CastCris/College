from begin.xtensions import flask

##
def register_app(app:object, **kwargs)->None:

    @app.route('/')
    def index()->None:
        return flask.redirect(flask.url_for("rooms_view"))
