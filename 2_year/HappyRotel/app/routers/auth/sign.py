from begin.xtensions import flask, flask_wtf, wtforms as wtf
from wtforms.validators import InputRequired, length, StopValidation

from begin.globals import flask_auth, Forms, CaptchaFlask, ManagerUser

##
class FormSign(CaptchaFlask.FormIMG):
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
    def validate_userPasswordCheck(self, field)->None:
        if self.userPassword.data == self.userPasswordCheck.data:
            return

        raise StopValidation('The password not match')

    def validate_userEmail(self, field)->None:
        from database.methods import UserInfos
        from database.session import session_query

        ##
        self.validate_userPasswordCheck(self.userPasswordCheck)
        
        userInfos = session_query(UserInfos, email=field.data)
        print('userInfos: ', userInfos, field.data)
        if userInfos is None:
            raise StopValidation("Internal server error")

        if userInfos:
            raise StopValidation("This user already exists")

    def validate(self, extra_validators=None)->bool:
        from database.methods import UserInfos, User
        from database.session import session_insert, session_query, model_get

        if not super().validate(extra_validators):
            return False

        ##
        self.validate_userEmail(self.userEmail)

        userInfos = session_insert(
            UserInfos
            , email=self.userEmail.data
            , name=self.userName.data
        )

        user = session_insert(
            User
            , userInfos_id=model_get(userInfos, "id")[0]
            , password=self.userPassword.data
            , permissions=0
        )

        return True
##
def register_app(app:object)->None:
    @app.route("/sign/display")
    @ManagerUser.required_logout
    def sign_display()->object:
        form_sign = FormSign()
        return flask.render_template('auth/sign.html', form_sign=form_sign)

    @app.route("/sign/auth", methods=['POST'])
    @ManagerUser.required_logout
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
        response = flask.make_response(flask.jsonify({
            'href_link': flask.url_for("login_display")
            })
        )
        
        return response
