from begin.xtensions import flask
from begin.globals import flask_auth

## Role
roleEmployer= flask_auth.Role({
    "MANAGE_INVOICE": 4,
    "MANAGE_RESERVERS": 8
    })

##
def register_app(app:object)->None:

    @app.route("/login/required")
    @flask_auth.login_required
    def login_required(userPk)->object:
        return f"You have permission to access this page! This is your id:{userPk}"

    @app.route("/permission/employer/int")
    @flask_auth.permissions_required(12)
    def permission_employer_int(userPk)->object:
        return f"You have permission to access this page! This is your id:{userPk}"

    @app.route("/permission/employer/role")
    @flask_auth.permissions_required(roleEmployer)
    def permission_employer_role(userPk)->object:
        return f"You have permission to access this page! This is your id:{userPk}"
