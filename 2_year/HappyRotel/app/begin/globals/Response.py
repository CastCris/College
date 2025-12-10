from begin.xtensions import flask

##
# def merge_json_responses(*args)->object:
def merge_cookies(response_receiver:object, *args)->None:
    from begin.globals import Cookie
    from functools import reduce
    from operator import concat

    ##
    for i in args:
        for cookie_raw in i.headers.getlist('Set-Cookie'):
            Cookie.define_from_string(response_receiver, cookie_raw)
