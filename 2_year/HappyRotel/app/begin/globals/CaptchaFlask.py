from begin.globals import Captcha
from begin.xtensions import flask_wtf, wtforms as wtf
from wtforms.validators import InputRequired, length, ValidationError

##
filter_str = lambda value: value.strip() if value else None

class FlaskFormCaptchaIMG(flask_wtf.FlaskForm):
    captcha = wtf.StringField(
        'Captcha'
        , validators=[InputRequired(), length(max=50)]
        , filters=[filter_str]
    )

    def validate_captcha(self, field)->None|object:
        print('crsf_token: ', self.csrf_token.data)
        captcha_result = verify(field.data, 'IMG', self.csrf_token.data)
        captcha_result_json = captcha_result.json
        if captcha_result_json.get("valid_captcha", None):
            return

        raise ValidationError(captcha_result_json.get("message")["content"])

##
def generate_img(csrf_token:str)->object:
    from begin.xtensions import flask
    from begin.globals import Crypt
    from io import BytesIO

    ##
    captcha_instance = Captcha.Image()
    captcha_token = Captcha.generate_code_img()
    captcha_img = captcha_instance.generate(captcha_token)
    # captcha_img = captcha_instance.generate('gggggg999')

    print('token: ', captcha_token)

    img_io = BytesIO()
    captcha_img.save(img_io, 'PNG')
    img_io.seek(0)

    #
    Captcha.token_save(captcha_token, 'img', csrf_token)
    response = flask.make_response(flask.send_file(img_io, mimetype="image/png", download_name="captcha.png"))

    return response

def generate(token_type:str, csrf_token:str)->object:
    token_type = token_type.upper()

    if token_type == "IMG":
        return generate_img(csrf_token)

    return flask.jsonify({
        Messages.Captcha.Error.invalid_type.json
    })

# Validation
def verify(token_input:str, token_type:str, csrf_token:str)->object:
    from begin.xtensions import flask
    from begin.globals import Messages

    ##
    captcha_token = Captcha.token_get(token_type, csrf_token)
    if captcha_token is None:
        return flask.jsonify({
            "valid_captcha": False,
            "message": Messages.Captcha.Error.not_requested.json
        })

    valid = Captcha.token_auth(token_input, token_type, csrf_token)
    msg = Messages.Captcha.Error.invalid.json if not valid else Messages.Captcha.Success.ok.json

    if valid:
        print('verify: ', token_type, csrf_token)
        Captcha.token_del(token_type, csrf_token)

    response = flask.make_response(flask.jsonify({
        "valid_captcha": valid,
        "message": msg
    }))
    
    return response
