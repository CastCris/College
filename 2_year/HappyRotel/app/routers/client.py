from begin.xtensions import flask

##
def client_generate_sid()->None:
    import base64
    import uuid

    ##
    if not flask.session.get("sid", None) is None:
        return 

    # sid = base64.b64encode(uuid.uuid4().bytes).decode()
    sid =uuid.uuid4().bytes
    flask.session["sid"] = sid

def client_cookies_check()->object|None:
    from begin.globals import Router, Cookie

    ##
    if Router.PATH_IGNORED(flask.request.path):
        return None

    for i in flask.request.cookies.keys():
        print('cookie: ', i, flask.request.cookies.keys())
        print('session: ', flask.session.keys())
        if i == "session":
            continue

        if Cookie.valid(i):
            continue

        response = flask.make_response(flask.redirect("/"))
        Cookie.delete_all(response)
        return response

##
def register_app(app:object, **kwargs)->None:

    @app.before_request
    def before_request()->object|None:
        client_generate_sid()

        print(flask.session.get("csrf_token"))
        response_cookies_check = client_cookies_check()
        if response_cookies_check:
            return response_cookies_check
