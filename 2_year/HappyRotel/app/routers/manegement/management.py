from begin.xtensions import flask
from begin.globals import roleAdmin, roleEmployer

##
def register_app(app:object, **kwargs)->None:
    managerUser = kwargs.get("managerUser")

    @app.route("/management/display")
    @managerUser.required_login
    def management_display(pkUser:dict)->object:
        from begin.globals import roleEmployer
        from database.methods import (
            User
            , Room, RoomStatus, RoomType, RoomLocation
        )
        from database.session import session_query, session_query_SQL, model_from_name, model_from_tuple

        ##
        user = session_query(User, **pkUser)[0]
        topics_raw = {}
        
        if user.authorized(roleEmployer):
            topics_raw["Room"] = session_query_SQL(
                Room
                , """
                SELECT id FROM \"Room\"
                ORDER BY RANDOM()
                LIMIT 10
                """
            )

        topics_json = {}
        for topic, instances in topics_raw.items():
            topics_json[topic] = []
            for i in instances:
                topics_json[topic].append(i.load_json())

        return flask.render_template('/management/management.html', topics=topics_json)

    @app.route("/management/item/<item_type>/<item_tag>")
    @managerUser.required_permission(roleEmployer)
    def management_item_display(pkUser, item_type:str, item_tag:str)->object:
        from database.methods import Room
        from database.session import session_query, model_get, model_from_name

        ##
        item_model = model_from_name(item_type)
        if item_model is None:
            flask.abort(404)

        item_instance = session_query(item_model, tag=item_tag)[0]
        if item_instance is None:
            flask.abort(500)

        if not item_instance:
            flask.abort(404)

        ##
        if item_type == "Room":
            return flask.redirect(flask.url_for("management_room_display", room_tag=item_tag))
