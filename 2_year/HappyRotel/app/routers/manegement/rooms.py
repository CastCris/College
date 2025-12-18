from begin.xtensions import flask
from begin.globals import roleEmployer

##
def register_app(app:object, **kwargs)->None:
    managerUser = kwargs.get("managerUser")

    @app.route("/management/rooms")
    @managerUser.required_permission(roleEmployer)
    def management_rooms(pkUser)->object:
        return 'Hello!'
