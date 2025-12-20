##
class Test():
    def __init__(self)->None:
        import random

        # query_1 = session_query(RoomInfos.id, RoomInfos.hashed_tag, location="Terrain")
        # query_2 = session_query(RoomInfos)

        # print('query_1: ', len(query_1))
        # print('query_2: ', len(query_2))

        admin_permissions = session_SQL("""
        SELECT up.tag, up.value, u.id FROM \"UserPermission\" AS up
        LEFT JOIN \"User\" AS u ON (( u.permissions & up.value) = up.value)
        WHERE u.permissions = 15
        """).all()
        print('admin_permissions: ')
        for i in admin_permissions:
            print(i)

        random_room_id = random.choice(session_query(Room.id))[0]
        random_room_status = session_SQL(f"""
        SELECT r.id, r.status_value, rs.name, rs.value, rs.positive FROM "RoomStatus" AS rs
        LEFT JOIN \"Room\" AS r ON
        (( r.status_value & rs.value ) = rs.value AND rs.positive = TRUE )
        OR
        (( r.status_value & rs.value ) <> rs.value AND rs.positive = FALSE)
        WHERE r.id = '{random_room_id}'
        """).all()

        print(f'Room {random_room_id} status: ')
        for i in random_room_status:
            print(i)
