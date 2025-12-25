from begin.xtensions import flask, flask_wtf, wtforms as wtf
from wtforms.validators import InputRequired, length, StopValidation

from begin.globals import flask_auth, Forms, roleAdmin

##
class FormRoomStatus(flask_wtf.FlaskForm):
    def __init__(self, *args, **kwargs)->None:
        from database.session import session_SQL

        ##
        super().__init__(*args, **kwargs)

        formData = kwargs.get("formdata")

        options = session_SQL("""
            SELECT opt_1.tag, opt_2.tag
            FROM \"RoomStatus\" AS opt_1
            JOIN \"RoomStatus\" AS opt_2
            ON
            opt_1.value = opt_2.value
            AND opt_1.tag < opt_2.tag
        """).all()

        for row in options:
            opt_1 = row[0]
            opt_2 = row[1]

            field_name = f"roomStatus_choice_{opt_1}_{opt_2}"
            field = wtf.SelectField(
                f"{opt_1}/{opt_2}"
                , choices=[
                    (opt_1, opt_1)
                    , (opt_2, opt_2)
                ]
            )
            field_bound = field.bind(self, field_name)
            field_bound.process(formData)

            self._fields[field_name] = field_bound
            setattr(self, field_name, field_bound)

class FormRoom(flask_wtf.FlaskForm):
    roomTag = wtf.HiddenField(
        'Room Tag'
        , validators=[InputRequired(), length(max=10)]
        , filters=[Forms.filter_str]
    )

    roomType = wtf.SelectField(
        'Room Type'
    )
    roomLocation = wtf.SelectField(
        'Room Location'
    )
    roomStatus = wtf.FormField(FormRoomStatus)

    def __init__(self, *args, **kwargs)->None:
        from database.methods import RoomType, RoomLocation
        from database.session import session_query, model_get

        ##
        super().__init__(*args, **kwargs)

        roomTypes = session_query(RoomType)
        roomLocations = session_query(RoomLocation)
        
        self.roomType.choices = [
            (model_get(roomType, "tag")[0]) for roomType in roomTypes
        ]

        self.roomLocation.choices = [
            (model_get(roomLocation, "tag")[0]) for roomLocation in roomLocations
        ]

        self.roomTag = kwargs.get('roomTag', None)


##
def register_app(app:object, **kwargs)->None:
    managerUser = kwargs["managerUser"]

    @app.route("/management/room/<room_tag>/display")
    @managerUser.required_permission(roleAdmin)
    def management_room_display(pkUser, room_tag:str)->object:
        from database.methods import Room
        from database.session import session_query

        ##
        room = session_query(Room, tag=room_tag)
        if room is None:
            flask.abort(500)
        if not room:
            flask.abort(404)
        
        roomJson = room[0].load_json()

        ##
        formsRoom = FormRoom(roomTag=roomJson['tag'])
        return flask.render_template('management/management_room.html', formsRoom=formsRoom, roomJson=roomJson)

    @app.route("/management/room/<room_tag>/auth", methods=['POST'])
    @managerUser.required_permission(roleAdmin)
    def management_room_auth(pkUser, room_tag:str)->object:
        from begin.globals import Messages

        from database.methods import Room
        from database.session import session_update

        ##
        formsRoom = FormRoom()
        if not formsRoom.validate_on_submit():
            forms_errors = Forms.forms_errors(formsRoom)
            return flask.jsonify({
                    'message': Messages.MError(forms_errors[0]).json
                })

        print('Hello!')
        return '{}'
