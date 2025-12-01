from begin.xtensions import flask

##
def register_app(app:object)->None:

    @app.route('/')
    def index()->None:
        return flask.render_template('index.html')
