from begin.xtensions import flask
from begin.globals import ManagerUser, roleEmployer

##
def register_app(app:object, **kwargs)->None:
    @app.route("/login/required")
    @ManagerUser.required_login
    def login_required()->object:
        return f"You have permission to access this page! This is your data:{flask.session.get("user")}"

    @app.route("/logout/required")
    @ManagerUser.required_logout
    def logout_required()->object:
        return "You is logoutted"

    @app.route("/permission/employer/int")
    @ManagerUser.required_permission(12)
    def permission_employer_int()->object:
        return f"You have permission to access this page! This is your data:{flask.session.user}"

    @app.route("/permission/employer/role")
    @ManagerUser.required_permission(roleEmployer)
    def permission_employer_role()->object:
        return f"You have permission to access this page! This is your data:{flask.session.user}"
