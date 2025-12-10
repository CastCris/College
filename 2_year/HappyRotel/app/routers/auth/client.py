from begin.xtensions import flask

##
def generate_sid()->str:
    import base64
    import uuid

    return base64.b64encode(uuid.uuid4().bytes).decode()

##
def client_cookie_check()->None|object:
    from begin.globals import Cookie, Router

    ##
    if Router.PATH_IGNORED(flask.request.path):
        return

    for i in flask.request.cookies.keys():
        if Cookie.valid(i):
            continue

        response = flask.make_response()
        for i in flask.request.cookies.keys():
            Cookie.delete(response, i)

        return response

    return None

##
def register_app(app:object)->None:

    @app.before_request
    def before_request()->object|None:
        from begin.globals import Response, Router

        ##
        if Router.PATH_IGNORED(flask.request.path):
            return

        response_cookie_check = client_cookie_check()
        response = None

        if response_cookie_check:
            response = flask.make_response(flask.redirect("/"))
            Response.merge_cookies(response, response_cookie_check)

        return response
