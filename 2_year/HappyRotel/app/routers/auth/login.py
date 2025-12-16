from begin.xtensions import flask, flask_wtf, wtforms as wtf
from wtforms.validators import InputRequired, length

##
filter_strip = lambda value: str.strip(filter_strip) if value else None
    

class FormLogin(flask_wtf.FlaskForm):
    userEmail = wtf.EmailField(
            'User Email'
            , id='login_form_user_email'
            , validators=[InputRequired(), length(255)]
            , filters=[filter_strip]
            )

    userPassword = wtf.PasswordField(
            'User Password'
            , id='login_form_user_password'
            , validators=[InputRequired(), length(155)]
            , filters=[filter_strip]
            )

    submit = wtf.SubmitField()


##
def register_app(app:object)->None:

    ##
    @app.route("/login/display")
    def login_display()->object:
        from begin.globals import Captcha

        ##
        form_login = FormLogin()
        form_captcha = Captcha.FormCaptchaIMG()

        return flask.render_template('login.html', form_login=form_login, form_captcha=form_captcha)

    @app.route("/login/auth", methods=['POST'])
    def login_auth()->None:
        from begin.globals import Messages, Cookie, Captcha, Crypt, Response, flask_auth
        from database.methods import User, UserInfos, Token, TokenType
        from database.session import session_insert, session_query, model_get

        ## Forms check
        if flask.request.method != 'POST':
            return flask.jsonify({
                'message': Messages.Request.Error.invalid_method.json
            })

        form_login = FormLogin()
        form_captcha = FormCaptcha()
        if not form_login.validate_on_submit() or not form_captcha.validate_on_submit():
            return flask.jsonify({
                'message': Messages.Login.Error.Request.invalid_fields.json
            })

        ## Captcha
        response_captcha = Captcha.verify(forms_captcha, 'img')
        if not response_captcha.json["valid_captcha"]:
            return flask.jsonify({
                'message': response_captcha.json["message"]
            })

        ## User validation
        userInfos = session_query(UserInfos, email=forms_user_email)
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


        if not user[0].password_auth(forms_user_password):
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
        Response.merge_cookies(response, response_captcha)

        return response
