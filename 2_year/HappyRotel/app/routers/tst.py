from begin.xtensions import flask
from begin.globals import flask_auth

## Role
roleEmployer= flask_auth.Role({
    "MANAGE_INVOICE": 4,
    "MANAGE_RESERVERS": 8
    })

##
def register_app(app:object, **kwargs)->None:
    managerUser = kwargs.get("managerUser")

    @app.route("/login/required")
    @managerUser.required_login
    def login_required(pkUser)->object:
        return f"You have permission to access this page! This is your id:{pkUser}"

    @app.route("/permission/employer/int")
    @managerUser.required_permission(12)
    def permission_employer_int(pkUser)->object:
        return f"You have permission to access this page! This is your id:{pkUser}"

    @app.route("/permission/employer/role")
    @managerUser.required_permission(roleEmployer)
    def permission_employer_role(pkUser)->object:
        return f"You have permission to access this page! This is your id:{pkUser}"
