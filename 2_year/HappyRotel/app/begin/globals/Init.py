def app_up_credentials(app:object)->None:
    from database import session, methods
    from begin.globals import Seeds, Router
    
    ##
    Seeds.cultivate()
    Router.register(app)

def flask_app(__context__:str, **kwargs)->None:
    from begin.globals import Init, Config, Cookie
    from begin.xtensions import flask, flask_session

    import os

    ##
    app = flask.Flask(__context__, **kwargs)
    app.config.from_object(Config)

    app.jinja_env.globals["Cookie"] = Cookie

    ##
    # If DEBUG flask options is enable, let this statement
    if os.environ.get("WERKZEUG_RUN_MAIN") == "true":
        app_up_credentials(app)

    # Or, if that options isn't enabled, uncomment the statement below and comment the up statement
    # app_up_credentials()

    app.run(debug=True, host='0.0.0.0', port=5000)
    flask_session.Session(app)
