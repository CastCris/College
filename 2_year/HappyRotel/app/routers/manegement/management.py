from begin.xtensions import flask
from begin.globals import roleAdmin, roleEmployer, ManagerUser, Globals

##
FIELDS_ABLE = [ 'room' ]
FIELD_FROM_TOPIC = lambda topic: 'room' if topic.startswith('Room') else None

##
def register_app(app:object, **kwargs)->None:

    ## Display
    @app.route("/management")
    @ManagerUser.required_login
    def management_display(pkUser:dict)->object:
        return flask.redirect(flask.url_for("management_topic_display", topic="Room"))

    @app.route("/management/<topic>")
    @ManagerUser.required_login
    def management_topic_display(pkUser:dict, topic:str)->object:
        if not topic in Globals.TOPICS_ABLE:
            flask.abort(404)

        field = FIELD_FROM_TOPIC(topic)
        return flask.redirect(flask.url_for("management_field_display", field=field, topic=topic))

    @app.route("/management/<field>/<topic>")
    @ManagerUser.required_login
    def management_field_display(pkUser:dict, field:str, topic:str)->object:
        if not field in FIELDS_ABLE:
            flask.abort(404)

        if not topic in Globals.TOPICS_ABLE:
            flask.abort(404)

        if field == 'room':
            return flask.redirect(flask.url_for("management_roomTopic_display", topic=topic))

    @app.route("/management/room/<topic>/display")
    @ManagerUser.required_permission(roleAdmin)
    def management_roomTopic_display(pkUser:dict, topic:str)->object:
        from begin.globals import roleEmployer

        from database.methods import Room, RoomType, RoomStatus
        from database.session import session_SQL, session_query, model_from_name

        ##
        TOPICS_ABLE = [ 'Room', 'RoomType', 'RoomStatus', 'RoomLocation' ]
        roomsJson = []

        if not topic in TOPICS_ABLE:
            flask.abort(404)

        ##
        model = model_from_name(topic)
        rooms_id = session_SQL(f"""
        SELECT id FROM \"{topic}\"
        ORDER BY RANDOM()
        LIMIT 10
        """).all()

        rooms = [ session_query(model, id=room_id[0])[0] for room_id in rooms_id ]
        roomsJson = [ room.load_json() for room in rooms ]

        return flask.render_template('management/management.html', topic=topic, topics_able=TOPICS_ABLE, items=roomsJson)


    ## Management item display
    @app.route("/management/item/<topic>/tag/<item_tag>")
    @ManagerUser.required_login
    def management_itemTopic_tag_display(pkUser, topic:str, item_tag:str)->object:
        if not topic in Globals.TOPICS_ABLE:
            flask.abort(404)

        field = FIELD_FROM_TOPIC(topic)
        return flask.redirect(flask.url_for("management_itemField_tag_display", item_field=field, topic=topic, item_tag=item_tag))

    @app.route("/management/item/<item_field>/<topic>/tag/<item_tag>")
    @ManagerUser.required_login
    def management_itemField_tag_display(pkUser, item_field:str, topic:str, item_tag:str)->object:
        from database.methods import Room
        from database.session import session_query, model_from_name

        ##
        if not item_field in FIELDS_ABLE:
            flask.abort(404)

        if not topic in Globals.TOPICS_ABLE:
            flask.abort(404)

        ##
        if item_field == 'room':
            return flask.redirect(flask.url_for("management_item_room_topic_tag_display", topic=topic, room_tag=item_tag))
