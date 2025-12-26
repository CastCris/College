from begin.globals import Captcha, Forms
from begin.xtensions import flask_wtf, wtforms as wtf
from wtforms.validators import InputRequired, length, StopValidation

##
class CaptchaFlaskFormBase(flask_wtf.FlaskForm):
    captchaToken = wtf.StringField(
        'Captcha'
        , validators=[InputRequired(), length(max=50)]
        , filters=[Forms.filter_str]
    )

    captchaType = wtf.HiddenField(
        'Captcha Type'
        , validators=[InputRequired(), length(max=4)]
        , filters=[Forms.filter_str]
    )

    ##
    def validate(self, extra_validators=None)->bool:
        if not super().validate(extra_validators):
            return False

        if not self.validate_captcha():
            return False

        return True

    def validate_captcha(self)->bool:
        # print('csrf_token: ', form.csrf_token.data)
        captcha_result = CaptchaFlask.verify(self.captchaToken.data)
        captcha_result_json = captcha_result.json

        print('captcha_result: ', captcha_result_json)
        if not captcha_result_json.get("valid_captcha", False):
            self.captchaToken.errors.append(captcha_result_json["message"]["content"])

        return captcha_result_json.get("valid_captcha", False)

##
class CaptchaFlask(Captcha):
    class FormIMG(CaptchaFlaskFormBase):
        def __init__(self, **kwargs)->None:
            super().__init__(**kwargs)

            self.captchaType.data  = 'IMG'

    ##
    @staticmethod
    def client_token_key_gen()->str:
        from begin.xtensions import flask

        ##
        forms = flask.request.json
        print('forms: ', forms)
        prefix = "token:captcha:{}:{}"

        csrf_token = forms["csrf_token"]
        captcha_type = forms["captchaType"].upper()

        print('key parameters: ', prefix.format(captcha_type, csrf_token))

        return prefix.format(captcha_type, csrf_token)

    # Validation
    @classmethod
    def verify(cls, token_input:str)->object:
        from begin.xtensions import flask
        from begin.globals import Messages

        ##
        captcha_token = cls.client_token
        if captcha_token is None:
            return flask.jsonify({
                "valid_captcha": False,
                "message": Messages.Captcha.Error.not_requested.json
            })

        valid = cls.client_token_auth(token_input)
        msg = Messages.Captcha.Error.invalid.json if not valid else Messages.Captcha.Success.ok.json

        if valid:
            Captcha.client_token_del()

        response = flask.make_response(flask.jsonify({
            "valid_captcha": valid,
            "message": msg
        }))
        
        return response

    ## Generation
    @classmethod
    def InitApp(cls, app:object)->None:
        @app.route("/captcha/generate/IMG")
        def captcha_generate_img()->object:
            from begin.xtensions import flask
            from begin.globals import Crypt
            from io import BytesIO

            ##
            captcha_instance = cls.Image()
            captcha_token = cls.code_img_generate()
            captcha_img = captcha_instance.generate(captcha_token)
            # captcha_img = captcha_instance.generate('gggggg999')

            print('token: ', captcha_token)

            img_io = BytesIO()
            captcha_img.save(img_io, 'PNG')
            img_io.seek(0)

            #
            cls.client_token_save(captcha_token)
            response = flask.make_response(flask.send_file(img_io, mimetype="image/png", download_name="captcha.png"))

            return response

        @app.route("/captcha/generate", methods=['POST'])
        def captcha_generate()->object:
            from begin.xtensions import flask
            from begin.globals import Messages

            ##
            if flask.request.method != 'POST':
                return flask.jsonify({
                    'message': Messages.Captcha.Request.Error.invalid_method
                })

            # print(cls.client_token_key)
            if not cls.client_token_key_valid:
                return flask.jsonify({
                    'message': 'Missing csrf / captcha type'
                })

            ##
            forms = flask.request.json
            token_type = forms["captchaType"].upper()

            if token_type == "IMG":
                return captcha_generate_img()

            return flask.jsonify({
                'message': Messages.Captcha.Error.invalid_type.json
            })
