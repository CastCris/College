from begin.xtensions import flask

##
def merge(*args)->object:
    from begin.globals import Cookie
    from functools import reduce
    from operator import concat

    ##
    data = reduce(concat, [ i.get_data(as_text=True) for i in args ])
    response = flask.make_response(data)

    for i in args:
        """
        for header, value in i.headers.items():
            if header == 'Set-Cookie':
                continue

            print(header, value)
            response.headers.setdefault(header, value)
        """

        for cookie_raw in i.headers.getlist('Set-Cookie'):
            Cookie.define_from_string(response, cookie_raw)

    print(response.headers.getlist('Set-Cookie'))

    return response
