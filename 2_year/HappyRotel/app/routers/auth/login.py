from begin.xtensions import flask, flask_wtf, wtforms as wtf
from wtforms.validators import InputRequired, length

from begin.globals import Forms, CaptchaFlask

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


##
def register_app(app:object)->None:

    ##
    @app.route("/login/display")
    def login_display()->object:
        from begin.globals import Captcha

        ##
        form_login = FormLogin()
        return flask.render_template('login.html', form_login=form_login)

    @app.route("/login/auth", methods=['POST'])
    def login_auth()->None:
        from begin.globals import Messages, Cookie, Captcha, Response, flask_auth
        from database.methods import User, UserInfos
        from database.session import session_query, model_get

        ##
        form_login = FormLogin()
        if not form_login.validate_on_submit():
            form_errors = Forms.forms_errors(form_login)
            return flask.jsonify({
                'message': Messages.Message(
                    content = form_errors[0]
                    , type =  Messages.Login.Error.js_class
                ).json
            })

        ##
        forms_captcha = form_login.captcha.data
        forms_userEmail = form_login.userEmail.data
        forms_userPassword = form_login.userPassword.data

        ## User validation
        userInfos = session_query(UserInfos, email=forms_userEmail)
        if userInfos is None:
            return flask.jsonify({
                'message': Messages.Request.Error.internal.json
            })

        if not len(userInfos):
            return flask.jsonify({
                'message': Messages.Login.Error.user_not_found.json
            })


        user = session_query(User, userInfos_id=userInfos[0].id) 
        if user is None:
            return flask.jsonify({
                'message': Messages.Request.Error.interval.json
            })


        if not user[0].password_auth(forms_userPassword):
            return flask.jsonify({
                'message': Messages.Login.Error.invalid_user_password.json
            })

        ## Login
        login = flask_auth.login(user[0])
        if not login:
            return flask.jsonify({
                'message': Messages.Login.Error.user_already_logged.json
            })

        ## Response OK
        response = flask.make_response({
            "href_link": "/",
        })
        Cookie.define(response, "user_name", model_get(userInfos[0], "cipher_name")[0], max_age=60*60*24*7)

        return response
