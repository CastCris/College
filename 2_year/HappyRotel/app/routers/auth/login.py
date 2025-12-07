from begin.xtensions import flask

##
def register_app(app:object)->None:

    ##
    @app.route("/login/display")
    def login_display()->object:
        return flask.render_template('login.html')

    @app.route("/login/auth", methods=['POST'])
    def login_auth()->None:
        from begin.globals import Messages, Captcha
        from database.methods import User, UserInfos, Token
        from database.session import session_insert, session_query


        ##
        if flask.request.methods != 'POST':
            return flask.jsonify({
                'message': Messages.Request.Error.invalid_method.json
            })

        forms = flask.request.json

        forms_user_name = forms["user_name"]
        forms_user_email = forms["user_email"]
        forms_user_password = forms["user_password"]

        forms_captcha = forms["captcha"]

        ##
        response = Captcha.verify(forms_captcha).json
        print('response: ', response)
        if not response["validity"]:
            return flask.jsonify({
                'message': response["message"]
            })

        ##
        userInfos = session_query(UserInfos, name=forms_user_name)
        user = session_query(User, userInfos_id=userInfos.id)

        if userInfos and not len(userInfos):
            return flask.jsonify({
                'message': Messages.Login.Error.user_not_found.json
            })

        if None in [ user, userInfos ]:
            return flask.jsonify({
                'message': Messages.Request.Error.internal.json
            })

        ##
        if not user.password_auth(forms_user_password):
            return flask.jsonify({
                'message': Messages.Login.Error.invalid_user_password
            })

        return '{}'
