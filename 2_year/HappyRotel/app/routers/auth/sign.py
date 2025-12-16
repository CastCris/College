from begin.xtensions import flask, flask_wtf, wtforms as wtf
from wtforms.validators import InputRequired, length, ValidationError

from begin.globals import Forms, CaptchaFlask

##
class FormSign(CaptchaFlask.FlaskFormCaptchaIMG):
    userName = wtf.StringField(
        'User Name'
        , validators=[InputRequired(), length(max=255)]
        , filters=[Forms.filter_str]
    )

    userEmail = wtf.EmailField(
        'User Email'
        , validators=[InputRequired(), length(max=255)]
        , filters=[Forms.filter_str]
    )

    userPassword = wtf.PasswordField(
        'User Password'
        , validators=[InputRequired(), length(min=8, max=30)]
        , filters=[Forms.filter_str]
    )
    userPasswordCheck = wtf.PasswordField(
        'User Password Check'
        , validators=[InputRequired(), length(min=8, max=30)]
        , filters=[Forms.filter_str]
    )

    ##
    def validate_userPasswordCheck(self, field)->None|object:
        print(self.userPassword.data, self.userPasswordCheck.data)
        if self.userPassword.data == self.userPasswordCheck.data:
            return

        raise ValidationError('The password not match')

##
def register_app(app:object)->None:

    @app.route("/sign/display")
    def sign_display()->object:
        form_sign = FormSign()
        return flask.render_template('sign.html', form_sign=form_sign)

    @app.route("/sign/auth", methods=['POST'])
    def sign_auth()->object:
        from begin.globals import Messages, Captcha, Response
        from database.methods import User, UserInfos
        from database.session import session_insert, session_query, model_get

        ## Validation
        form_sign = FormSign()
        if not form_sign.validate_on_submit():
            form_errors = Forms.forms_errors(form_sign)
            return flask.jsonify({
                'message': Messages.Message(
                    content = form_errors[0],
                    type = Messages.Sign.Error.js_class
                ).json
            })

        ##
        userName = form_sign.userName
        userEmaill = form_sign.userEmail
        userPassword = form_sign.userPassword

        captcha = form_sign.captcha

        ##
        userInfos = session_query(UserInfos, email=userEmail)
        
        return '{}'
