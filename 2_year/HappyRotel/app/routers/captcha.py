from begin.xtensions import flask

##
def register_app(app:object, **kwargs)->None:

    @app.route("/captcha/generate/<token_type>", methods=['POST'])
    def captcha_generate(token_type:str)->object:
        from begin.globals import CaptchaFlask, Messages
        
        ##
        if flask.request.method != 'POST':
            return flask.jsonify({
                'message': Messages.Request.Error.invalid_method.json
            })

        json = flask.request.json
        csrf_token = json["csrf_token"]

        return CaptchaFlask.generate(token_type, csrf_token)
