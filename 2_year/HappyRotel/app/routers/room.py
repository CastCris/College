from begin.xtensions import flask

##
def register_app(app:object, **kwargs)->None:

    @app.route('/rooms/load')
    def rooms_load()->object:
        from database.methods import Room
        from database.session import session_query, session_SQL, model_from_tuple
        import random

        ##
        rooms_chosen = [ session_query(Room, id=row[0])[0]
            for row in session_SQL("""
                SELECT id FROM \"Room\"
                ORDER BY RANDOM()
                LIMIT 10
            """).all()
        ]

        ##
        rooms_infos = []
        for room in rooms_chosen:
            rooms_infos.append(room.load_json())

        return flask.jsonify({
            'rooms': rooms_infos
        })

    @app.route('/rooms/view')
    def rooms_view()->object:
        rooms_infos = rooms_load().json["rooms"]
        print('room_infos: ', rooms_infos, flush=True)

        return flask.render_template('index.html', rooms_infos=rooms_infos)
