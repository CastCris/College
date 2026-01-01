from begin.xtensions import flask

##
def register_app(app:object, **kwargs)->None:

    @app.route('/rooms/load')
    def rooms_load()->object:
        from database.methods import Room
        from database.session import session_query_SQL, model_from_tuple
        import random

        ##
        """
        rooms_chosen = [ session_query(Room, id=row[0])[0]
            for row in session_SQL(\"\"\"
                SELECT id FROM \"Room\"
                ORDER BY RANDOM()
                LIMIT 10
            \"\"\").all()
        ]
        """

        rooms_chosen = session_query_SQL(
            Room 
            , """
            SELECT * FROM \"Room\"
            ORDER BY RANDOM()
            LIMIT 10
            """
        )

        ##
        roomsJson = []
        for room in rooms_chosen:
            roomsJson.append(room.load_json())

        return flask.jsonify({
            'rooms': roomsJson
        })

    @app.route('/rooms/view')
    def rooms_view()->object:
        roomsJson = rooms_load().json["rooms"]
        print('room_infos: ', roomsJson, flush=True)

        return flask.render_template('index.html', roomsJson=roomsJson)
