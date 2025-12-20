from begin.xtensions import flask, flask_wtf, wtforms as wtf
from wtforms.validators import InputRequired, length, StopValidation

from begin.globals import flask_auth, Forms, CaptchaFlask

##
class FormLogin(CaptchaFlask.FlaskFormCaptchaIMG):
    userEmail = wtf.EmailField(
        'User Email'
        , validators=[InputRequired(), length(max=255)]
        , filters=[Forms.filter_str]
    )

    userPassword = wtf.PasswordField(
        'User Password'
        , validators=[InputRequired(), length(max=30)]
        , filters=[Forms.filter_str]
    )

    def validate_userEmail(self, field)->None:
        from database.methods import UserInfos
        from database.session import session_query

        userInfos = session_query(UserInfos.id, email=field.data)
        if userInfos is None:
            raise StopValidation('Internal Server Error')

        if not len(userInfos):
            raise StopValidation('User not found')

    def validate_userPassword(self, field)->None:
        from database.methods import User, UserInfos
        from database.session import session_query, model_get

        ##
        self.validate_userEmail(self.userEmail)

        userInfos = session_query(UserInfos.id, email=self.userEmail.data)[0]
        user = session_query(User, userInfos_id=userInfos[0])[0]
        
        if not user.password_auth(field.data):
            raise StopValidation('Wrong user password')


##
def register_app(app:object, **kwargs)->None:
    managerUser = kwargs.get("managerUser")

    ##
    @app.route("/login/display")
    @managerUser.required_logout
    def login_display()->object:
        from begin.globals import Captcha

        ##
        form_login = FormLogin()
        return flask.render_template('auth/login.html', form_login=form_login)

    @app.route("/login/auth", methods=['POST'])
    @managerUser.required_logout
    def login_auth()->None:
        from begin.globals import Messages, Cookie, Captcha, Response, flask_auth
        from database.methods import User, UserInfos
        from database.session import session_query, model_get

        ##
        form_login = FormLogin()
        if not form_login.validate_on_submit():
            form_errors = Forms.forms_errors(form_login)
            print('form_errors: ', form_errors)
            return flask.jsonify({
                'message': Messages.Message(
                    content = form_errors[0]
                    , type =  Messages.Login.Error.js_class
                ).json
            })

        ##
        forms_userEmail = form_login.userEmail.data
        userInfos = session_query(UserInfos, email=forms_userEmail)[0]
        user = session_query(User, userInfos_id=model_get(userInfos, "id"))[0]

        login = managerUser.login(user)

        ##
        response = flask.make_response({
            "href_link": flask.url_for("index"),
        })
        Cookie.define(response, "user_name", model_get(userInfos, "cipher_name")[0], max_age=60*60*24*7)

        return response
