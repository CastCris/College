from begin.xtensions import flask
from begin.globals import ManagerUser, roleEmployer

##
def register_app(app:object, **kwargs)->None:
    
    @app.route("/login/required")
    @ManagerUser.required_login
    def login_required(pkUser)->object:
        return f"You have permission to access this page! This is your id:{pkUser}"

    @app.route("/permission/employer/int")
    @ManagerUser.required_permission(12)
    def permission_employer_int(pkUser)->object:
        return f"You have permission to access this page! This is your id:{pkUser}"

    @app.route("/permission/employer/role")
    @ManagerUser.required_permission(roleEmployer)
    def permission_employer_role(pkUser)->object:
        return f"You have permission to access this page! This is your id:{pkUser}"
