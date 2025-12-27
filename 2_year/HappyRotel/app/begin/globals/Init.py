def app_up_credentials(app:object)->None:
    import database

    from begin.xtensions import flask_session
    from begin.globals import Seeds, Router, CaptchaFlask, Config, CookieSession
    from begin.globals.flask_auth import ManagerUser

    ##
    ManagerUser.InitApp(app)
    CaptchaFlask.InitApp(app)
    CookieSession.InitApp(app)

    Seeds = Seeds()
    Seeds.cultivate()

    print(ManagerUser)
    Router.register(app)

def flask_app(__context__:str, **kwargs)->None:
    from begin.globals import Init, Config, CookieSession, CaptchaFlask
    from begin.xtensions import flask, flask_session

    import os

    ##
    app = flask.Flask(__context__, **kwargs)
    app.config.from_object(Config)

    app.jinja_env.globals["load_cookie"] = CookieSession.get

    ##
    # If DEBUG flask options is enable, let this statement
    if os.environ.get("WERKZEUG_RUN_MAIN") == "true":
        app_up_credentials(app)

    # Or, if that options isn't enabled, uncomment the statement below and comment the up statement
    # app_up_credentials()

    app.run(debug=True, host='0.0.0.0', port=5000)
    flask_session.Session(app)
