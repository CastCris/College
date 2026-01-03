from begin.xtensions import flask
from begin.globals import roleAdmin, ManagerUser, Globals

##
FIELD_FROM_TOPIC = lambda topic: 'room' if topic.startswith('Room') else 'user' if topic.startswith('User') else None

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
        from database.session import session_SQL, session_query, model_from_name

        ##
        if not field in Globals.FIELD_TOPICS:
            flask.abort(404)

        if not topic in Globals.TOPICS_ABLE:
            flask.abort(404)

        ##
        TOPICS_ABLE = Globals.FIELD_TOPICS[field]

        ##
        instancesJson = []
        if not topic in TOPICS_ABLE:
            flask.abort(404)

        ##
        model = model_from_name(topic)
        instances_id = session_SQL(f"""
        SELECT id FROM \"{topic}\"
        ORDER BY RANDOM()
        LIMIT 10
        """).all()

        instances = [ session_query(model, id=instance_id[0])[0] for instance_id in instances_id ]
        instancesJson = [ instance.load_json() for instance in instances ]

        return flask.render_template(
            'management/management.html'
            , fields_able=Globals.FIELD_TOPICS
            , topics_able=TOPICS_ABLE

            , items=instancesJson
            , topic=topic
        )


    ## Management item display
    @app.route("/management/item/<topic>/<item_arg>")
    @ManagerUser.required_login
    def management_itemTopic_arg_display(pkUser, topic:str, item_arg:str)->object:
        if not topic in Globals.TOPICS_ABLE:
            flask.abort(404)

        field = FIELD_FROM_TOPIC(topic)
        return flask.redirect(
            flask.url_for(
                "management_itemField_arg_display"
                , item_field=field
                , topic=topic
                , item_arg=item_arg
                )
        )

    @app.route("/management/item/<item_field>/<topic>/<item_arg>")
    @ManagerUser.required_login
    def management_itemField_arg_display(pkUser, item_field:str, topic:str, item_arg:str)->object:
        from database.methods import Room
        from database.session import session_query, model_from_name

        ##
        if not item_field in Globals.FIELD_TOPICS:
            flask.abort(404)

        if not topic in Globals.TOPICS_ABLE:
            flask.abort(404)

        ##
        if item_field == 'room':
            return flask.redirect(
                flask.url_for(
                    "management_item_room_topic_id_display"
                    , topic=topic
                    , room_id=item_arg
                )
            )

        if item_field == 'user':
            return flask.redirect(
                flask.url_for(
                    "management_item_user_topic_id_display"
                    , topic=topic
                    , user_id=item_arg
                )
            )
