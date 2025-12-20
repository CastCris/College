from begin.xtensions import flask

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
        from database.session import session_SQL, session_query, session_SQL, model_from_name, model_from_tuple

        ##
        user = session_query(User, **pkUser)[0]
        topics_raw = {}
        
        if user.authorized(roleEmployer):
            topics_raw["Room"] = session_SQL("""
                SELECT * FROM \"Room\"
                ORDER BY RANDOM()
                LIMIT 10
            """)

        topics_json = {}
        for topic, value in topics_raw.items():
            topics_json[topic] = []
            for i in value:
                model = model_from_name(topic)
                instance = model_from_tuple(model, i)
                topics_json[topic].append(instance.load_json())

        return flask.render_template('/management/management.html', topics=topics_json)
