from begin.xtensions import flask, flask_wtf, wtforms as wtf
from wtforms.validators import InputRequired, length, StopValidation

from begin.globals import flask_auth, Forms, roleAdmin

##
class FormRoom(flask_wtf.FlaskForm):
    roomType = wtf.SelectField(
        'Room Type'
    )
    roomLocation = wtf.SelectField(
        'Room Location'
    )
    roomStatus = wtf.SelectMultipleField(
        'Room Status'
    )

    def __init__(self, **kwargs)->None:
        from database.methods import RoomType, RoomStatus, RoomLocation
        from database.session import session_query, model_get

        ##
        super().__init__(**kwargs)

        roomTypes = session_query(RoomType)
        roomLocations = session_query(RoomLocation)
        roomStatus = session_query(RoomStatus)
        
        self.roomType.choices = [
            (model_get(roomType, "tag")[0]) for roomType in roomTypes
        ]
        self.roomLocation.choices = [
            (model_get(roomLocation, "tag")[0]) for roomLocation in roomLocations
        ]
        self.roomStatus.choices = [
            (model_get(status, "tag")[0]) for status in roomStatus
        ]

##
def register_app(app:object, **kwargs)->None:
    managerUser = kwargs["managerUser"]

    @app.route("/management/room/<room_id>/display")
    @managerUser.required_permission(roleAdmin)
    def management_room_display(pkUser, room_id:str)->object:
        formsRoom = FormRoom()
        return flask.render_template('management/room.html', formsRoom=formsRoom)

    @app.route("/management/room/<room_id>/auth", methods=['POST'])
    @managerUser.required_permission(roleAdmin)
    def management_room_auth(pkUser, room_id:str)->object:
        from begin.globals import Messsages

        from database.methods import Room
        from database.session import session_update

        ##
        formsRoom = FormRoom()
        if not formsRoom.validate_on_submit():
            forms_errors = Forms.forms_errors(formsRoom)
            return flask.jsonify({
                    'message': Messages.Message(
                        content=forms_errors[0]
                        , type=Messsages.Error.js_class
                    )
                })

        print('Hello!')
        return '{}'
