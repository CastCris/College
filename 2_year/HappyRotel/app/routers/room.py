from begin.xtensions import flask
from database import *

##
def register_app(app:object, **kwargs)->None:

    @app.route('/rooms/load')
    def rooms_load()->object:
        import random

        rooms = set(session_query(Room))
        rooms_chosen = []
        while len(rooms_chosen) < 10 and len(rooms):
            room_choice = random.choice(list(rooms))

            rooms_chosen.append(model_get_columns_value(room_choice))
            rooms.remove(room_choice)

        rooms_infos = []
        for room in rooms_chosen:
            print('room: ', room, flush=True)
            room_type = model_get_columns_value(session_query(RoomType, id=room["roomType_id"])[0])
            room_infos = model_get_columns_value(session_query(RoomInfos, id=room["roomInfos_id"])[0])
            room_status = session_SQL(f"""
            SELECT rs.name FROM \"Room\" as r
            LEFT JOIN \"RoomStatus\" AS rs ON 
                (
                (( r.status_value & rs.value ) = rs.value AND rs.positive = TRUE)
                OR
                (( r.status_value & rs.value ) <> rs.value AND rs.positive = FALSE)
                )
            WHERE r.id = '{room["id"]}'
            """).all()
            # print('room_infos: ', room_infos)

            rooms_infos.append({
                'tag': room_infos["tag"],

                'type': room_type["tag"],
                'price': room_type['price'],
                'description': room_type["description"],

                'location': room_infos["location"],
                'capacity': room_type["capacity"],
                'status': room_status[0][0]
            })

        return flask.jsonify({
            'rooms': rooms_infos
        })

    @app.route('/rooms/view')
    def rooms_view()->object:
        rooms_infos = rooms_load().json["rooms"]
        print('room_infos: ', rooms_infos, flush=True)

        return flask.render_template('index.html', rooms_infos=rooms_infos)
