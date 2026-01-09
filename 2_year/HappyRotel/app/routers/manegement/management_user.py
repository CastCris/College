from begin.xtensions import flask, flask_wtf, wtforms as wtf
from begin.globals import ManagerUser, roleAdmin, Forms, Globals

from wtforms.validators import InputRequired, length, StopValidation

##
USER_PERMISSIONS_GET_VALUE = lambda ids: f"""
SELECT 
CASE 
    WHEN BOOL_OR(value = 0) THEN 0
    ELSE SUM(value) 
END AS value
FROM \"UserPermission\"
WHERE id IN ({', '.join([ f"'{id}'" for id in ids ])})
"""

USER_PERMISSIONS_SUM_VALUE = """
SELECT SUM(value) FROM \"UserPermission\"
"""

##
class FormUserBase(flask_wtf.FlaskForm):
    field = wtf.HiddenField(
        'Field'
    )

    topic = wtf.HiddenField(
        'Topic'
    )

    id_field = wtf.HiddenField(
        'Id field'
    )

    def __init__(self, *args, **kwargs)->None:
        super().__init__(*args, **kwargs)

        self.field.data = 'user'
        if not kwargs.get("topic") is None:
            self.topic.data = kwargs.get("topic")


class FormUser(FormUserBase):
    user_id = wtf.HiddenField(
        'User Id'
        , validators=[InputRequired(), length(max=32)]
        , filters=[Forms.filter_str]
    )

    user_password = wtf.PasswordField(
        'User new password'
        , validators=[length(max=155)]
    )

    user_password_check = wtf.PasswordField(
        'User new password check'
        , validators=[length(max=155)]
    )

    user_permissions = wtf.SelectMultipleField(
        'User Permissions'
    )

    ##
    def __init__(self, *args, **kwargs)->None:
        from database.methods import UserPermission
        from database.session import session_query

        ##
        super().__init__(*args, **kwargs)

        userPermissions = session_query(UserPermission.id, UserPermission.tag)

        self.user_permissions.choices = [
            (row[0], row[1]) for row in userPermissions
        ]

        ##
        if not kwargs.get("user_id") is None:
            user_id = kwargs.get("user_id")
            self.populate(user_id)

    ##
    def populate(self, user_id:str)->None:
        from database.methods import User
        from database.session import session_query

        user = session_query(User, id=user_id)[0]

        self.user_id.data = user_id
        self.user_permissions.data = user.permissions_json.keys()

    ##
    def validate_user_id(self, field)->None:
        from database.methods import User
        from database.session import session_query

        if not session_query(User, id=field.data):
            raise StopValidation('Invalid user id')

    def validate_user_password_check(self, field)->None:
        from database.methods import User
        from database.session import session_query

        ##
        self.validate_user_id(self.user_id)

        if not field.data == self.user_password.data:
            raise StopValidation('The passwords not macth')

        user = session_query(User, id=self.user_id.data)[0]
        if user.password_auth(field.data):
            raise StopValidation('The password can be equal to the current')
        

    def validate_user_permissions(self, field)->None:
        from database.methods import User, UserPermission
        from database.session import session_query, session_SQL, instance_get

        ##
        self.validate_user_id(self.user_id)

        for choice in field.data:
            if not session_query(UserPermission.id, id=choice):
                raise StopValidation('Invalid user permission choie')

        user = session_query(User, id=self.user_id.data)[0]
        user_permissions = instance_get(user, "permissions")[0]
        user_permissions_new = session_SQL(USER_PERMISSIONS_GET_VALUE(field.data)).all()[0][0]

        permissions_sum_all = session_SQL(USER_PERMISSIONS_SUM_VALUE).all()[0][0]

        print('user_permissions: ', user, user_permissions, user_permissions_new)

        if user_permissions == permissions_sum_all:
            users_admin = session_query(User, permissions=permissions_sum_all)
            if len(users_admin) == 1 and user_permissions_new != permissions_sum_all:
                raise StopValidation('Must have, at leat, one admin user')

class FormUserInfos(FormUserBase):
    userInfos_id = wtf.HiddenField(
        'UserInfos Id'
        , validators=[InputRequired(), length(max=32)]
        , filters=[Forms.filter_str]
    )

    userInfos_name = wtf.StringField(
        'User Name'
        , validators=[InputRequired(), length(min=3, max=155)]
        , filters=[Forms.filter_str]
    )
    userInfos_email = wtf.EmailField(
        'User Email'
        , validators=[InputRequired(), length(min=11, max=255)]
        , filters=[Forms.filter_str]
    )

    ##
    def __init__(self, *args, **kwargs)->None:
        super().__init__(*args, **kwargs)

        if not kwargs.get("user_id") is None:
            user_id = kwargs.get("user_id")
            self.populate(user_id)

    ##
    def populate(self, user_id:str)->None:
        from database.methods import UserInfos
        from database.session import session_query, instance_get

        userInfos = session_query(UserInfos, id=user_id)[0]
        userInfos_json = userInfos.load_json()

        self.userInfos_id.data = userInfos_json["id"]
        self.userInfos_name.data = userInfos_json["name"]
        self.userInfos_email.data = userInfos_json["email"]

    def validate_userInfos_id(self, field)->None:
        from database.methods import UserInfos
        from database.session import session_query

        if not session_query(UserInfos, id=field.data):
            raise StopValidation('Invalid UserInfos id')

class FormUserPermission(FormUserBase):
    userPermission_id = wtf.HiddenField(
        'UserPermission Id'
        , validators=[InputRequired(), length(max=32)]
        , filters=[Forms.filter_str]
    )

    userPermission_tag = wtf.StringField(
        'User Permission tag'
        , validators=[InputRequired(), length(max=155)]
        , filters=[Forms.filter_str]
    )


    ##
    def __init__(self, *args, **kwargs)->None:
        super().__init__(*args, **kwargs)

        if not kwargs.get("user_id") is None:
            user_id = kwargs.get("user_id")
            self.populate(user_id)

    ##
    def populate(self, user_id:str)->None:
        from database.methods import UserPermission
        from database.session import session_query

        userPermission = session_query(UserPermission, id=user_id)[0]
        userPermission_json = userPermission.load_json()

        self.userPermission_id.data = userPermission_json["id"]
        self.userPermission_tag.data = userPermission_json["tag"]

    ##
    def validate_userPermission_id(self, field)->None:
        from database.methods import UserPermission
        from database.session import session_query

        if not session_query(UserPermission, id=field.data):
            raise StopValidation('Invalid UserPermission id')

    def validate_userPermission_tag(self, field)->None:
        from database.methods import UserPermission
        from database.session import session_query

        ##
        self.validate_userPermission_id(self.userPermission_id)

        userPermission_id = session_query(UserPermission.id, tag=field.data)
        if userPermission_id and userPermission_id[0][0] != self.userPermission_id.data:
            raise StopValidation('This tag already exists')

##
def register_app(app:object, **kwargs)->None:

    @app.route("/management/item/user/<topic>/id/<user_id>/display")
    @ManagerUser.required_permission(roleAdmin)
    def management_item_user_topic_id_display(pkUser, topic:str, user_id:str)->object:
        from database.session import model_from_name, session_query

        if not topic in Globals.FIELD_TOPICS['user']:
            flask.abort(404)

        model = model_from_name(topic)
        user = session_query(model, id=user_id)
        if user is None:
            flask.abort(500)

        if not user:
            flask.abort(404)

        ##
        formsUser_class = None
        template_path = ''
        userJson = None

        if topic == 'User':
            formsUser_class = FormUser
            template_path = 'management/user/management_user.html'

        if topic == 'UserInfos':
            formsUser_class = FormUserInfos
            template_path = 'management/user/management_userInfos.html'

        if topic == 'UserPermission':
            formsUser_class = FormUserPermission
            template_path = 'management/user/management_userPermission.html'

        formsUser = formsUser_class(
            user_id = user_id
            , topic=topic
        )
        userJson = user[0].load_json()

        return flask.render_template(
            template_path
            , formsUser = formsUser
            , userJson = userJson
        )

    @app.route("/management/item/user/User/auth", methods=['POST'])
    @ManagerUser.required_permission(roleAdmin)
    def management_item_user_User_auth(pkUser)->object:
        from begin.globals import Messages

        from database.methods import User, UserPermission
        from database.session import session_query, session_SQL, instance_update

        ##
        formsUser = FormUser()
        if not formsUser.validate_on_submit():
            forms_errors = Forms.forms_errors(formsUser)
            return flask.jsonify({
                'message': Messages.MError(forms_errors[0]).json
            })

        user_id = formsUser.user_id.data
        user_password = formsUser.user_password.data
        user_permissions = formsUser.user_permissions.data

        ##
        user = session_query(User, id=user_id)[0]
        user_permission_value = session_SQL(
            USER_PERMISSIONS_GET_VALUE(user_permissions)
        ).all()[0][0]

        instance_update(
            user
            , password=user_password
            , permissions = user_permission_value
        )


        return flask.jsonify({
            'message': Messages.MSuccess('Operation completed').json
        })

    @app.route("/management/item/user/UserInfos/auth", methods=['POST'])
    @ManagerUser.required_permission(roleAdmin)
    def management_item_user_UserInfos_auth(pkUser)->object:
        from begin.globals import Messages

        from database.methods import UserInfos
        from database.session import session_query, instance_update

        ##
        formsUser = FormUserInfos()
        if not formsUser.validate_on_submit():
            forms_errors = Forms.forms_errors(formsUser)
            return flask.jsonify({
                'message': Messages.MError(forms_errors[0]).json
            })

        ##
        userInfos_id = formsUser.userInfos_id.data
        userInfos_name = formsUser.userInfos_name.data
        userInfos_email = formsUser.userInfos_email.data

        ##
        userInfos = session_query(UserInfos, id=userInfos_id)[0]

        instance_update(
            userInfos
            , name = userInfos_name
            , email = userInfos_email
        )

        return flask.jsonify({
            'message': Messages.MSuccess('Operation complated').json
        })

    @app.route("/management/item/user/UserPermission/auth", methods=['POST'])
    @ManagerUser.required_permission(roleAdmin)
    def management_item_user_UserPermission_auth(pkUser)->object:
        from begin.globals import Messages

        from database.methods import UserPermission
        from database.session import session_query, instance_update

        formsUser = FormUserPermission()
        if not formsUser.validate_on_submit():
            forms_errors = Forms.forms_errors(formsUser)
            return flask.jsonify({
                'message': Messages.MError(forms_errors[0]).json
            })

        userPermission_id = formsUser.userPermission_id.data
        userPermission_tag = formsUser.userPermission_tag.data

        ##
        userPermission = session_query(UserPermission, id=userPermission_id)[0]
        instance_update(
            userPermission
            , id = userPermission_id
            , tag = userPermission_tag
        )

        return flask.jsonify({
            'message': Messages.MSuccess('Operation completed').json
        })
