from begin.xtensions import flask
from begin.globals import flask_auth

##
class FormsLogin():
    pass

##
def register_app(app:object)->None:

    ##
    @app.route("/login/display")
    def login_display()->object:
        return flask.render_template('login.html')

    @app.route("/login/auth", methods=['POST'])
    @flask_auth.login
    def login_auth()->None:
        from begin.globals import Messages, Cookie, Captcha, Crypt, Response
        from database.methods import User, UserInfos, Token, TokenType
        from database.session import session_insert, session_query, model_get


        ##
        if flask.request.method != 'POST':
            return flask.jsonify({
                'message': Messages.Request.Error.invalid_method.json
            })

        forms = flask.request.json

        forms_user_email = forms.get("user_email", None)
        forms_user_password = forms.get("user_password", None)

        forms_captcha = forms.get("captcha")

        if None in [ forms_user_email, forms_user_password, forms_captcha]:
            return flask.jsonify({
                'message': Messages.Request.Error.missing_fields
            })

        ##
        response_captcha = Captcha.verify(forms_captcha, 'img')
        if not response_captcha.json["valid_captcha"]:
            return flask.jsonify({
                'message': response_captcha.json["message"]
            })

        ##
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

        ##
        response = flask.make_response({
            "href_link": "/",
            "approved": True
        })
        Response.merge_cookies(response, response_captcha)

        return response
