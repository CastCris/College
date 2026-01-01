from begin.xtensions import flask, flask_wtf, wtforms as wtf
from wtforms.validators import InputRequired, length, StopValidation

from begin.globals import flask_auth, Forms, roleAdmin, ManagerUser, Globals

##
OPTIONS_SQL = """
SELECT opt_1.tag, opt_1.id, opt_2.tag, opt_2.id
FROM \"RoomStatus\" AS opt_1
JOIN \"RoomStatus\" AS opt_2
ON opt_1.value = opt_2.value
AND opt_1.tag < opt_2.tag
"""

OPTIONS_SQL_GET = lambda tags: f"""
SELECT SUM(
    CASE WHEN positive 
        THEN value
    ELSE 
        0
    END
) AS value
FROM \"RoomStatus\"
WHERE id IN ({ ','.join([ f"'{i}'" for i in tags ]) })
"""

##
class FormRoomStatusItems(flask_wtf.FlaskForm):
    def __init__(self, *args, **kwargs)->None:
        from database.methods import Room
        from database.session import session_SQL, session_query


        ##
        formData = kwargs.get("formdata")
        options = session_SQL(OPTIONS_SQL).all()

        for row in options:
            opt1_tag, opt1_id = row[0], row[1]
            opt2_tag, opt2_id = row[2], row[3]

            field_name = f"roomStatus_choice_{opt1_tag}_{opt2_tag}"
            field = wtf.SelectField(
                f"{opt1_tag}/{opt2_tag}"
                , choices=[
                    (opt1_id, opt1_tag)
                    , (opt2_id, opt2_tag)
                ]
            )

            Forms.add_field(self.__class__, field_name, field)

        ##
        super().__init__(*args, **kwargs)

    ##
    def populate(self, room_id:str)->None:
        from database.methods import Room
        from database.session import session_query

        ##
        room = session_query(Room, id=room_id)[0]
        room_status = room.get_status()

        fields_name = self._fields.keys()
        for status in room_status:
            for field_name in fields_name:
                if not status in field_name:
                    continue

                getattr(self, field_name).data = status
                break

    ##
    def validate(self, extra_validators=None)->bool:
        from database.methods import RoomStatus
        from database.session import session_SQL

        ##
        if not super().validate(extra_validators):
            return False

        """
        options = session_SQL(OPTIONS_SQL).all()
        print('roomStauts_validate: ', options, self._fields)
        if len(list(self._fields.keys()))-1 != len(options):
            return False

        for i in range(len(list(self._fields.keys()))):
            key = list(self._fields.keys())[i]
            if key == "csrf_token":
                continue

            # print('roomStatus_key: ', key)

            field = self._fields[key]
            field_choices = field.choices

            option_row = i-1
            for j in range(len(options[option_row])):
                option = options[option_row][j]
                print('roomStatus_option: ', field_choices[j], option)
                if not option in field_choices[j]:
                    field.errors.append('Invalid room status option')
                    return False
        """

        return True

class FormRoom(flask_wtf.FlaskForm):
    room_id = wtf.HiddenField(
        'Room Id'
        , validators=[InputRequired(), length(max=32)]
        , filters=[Forms.filter_str]
    )

    roomType = wtf.SelectField(
        'Room Type'
    )
    roomLocation = wtf.SelectField(
        'Room Location'
    )

    roomStatus = wtf.FormField(
        FormRoomStatusItems
    )

    def __init__(self, *args, **kwargs)->None:
        from database.methods import RoomType, RoomLocation
        from database.session import session_query

        ##
        super().__init__(*args, **kwargs)

        roomTypes = session_query(RoomType.id, RoomType.tag)
        roomLocations = session_query(RoomLocation.id, RoomLocation.tag)

        ##
        self.roomType.choices = [
            (id, tag) for id, tag in roomTypes
        ]

        self.roomLocation.choices = [
            (id, tag) for id, tag in roomLocations
        ]

        ##
        if not kwargs.get("room_id") is None:
            room_id = kwargs.get("room_id")
            self.populate(room_id)
        
    ##
    def populate(self, room_id)->None:
        from database.methods import Room, RoomType, RoomLocation
        from database.session import session_query, instance_get

        ##
        roomType_id, roomLocation_id = session_query(Room.roomType_id, Room.roomLocation_id, id=room_id)[0]

        ##
        self.room_id.data = room_id
        self.roomType.data = roomType_id
        self.roomLocation.data= roomLocation_id

        self.roomStatus.populate(room_id)

    ##
    def validate_roomTag(self, field)->None:
        from database.methods import Room
        from database.session import session_query

        room = session_query(Room, id=field.data)
        if room is None:
            raise StopValidation('Interval server error')

        if not room:
            raise StopValidation('Room not found')

    def validate_roomType(self, field)->None:
        from database.methods import RoomType
        from database.session import session_query

        roomType = session_query(RoomType, id=field.data)
        if roomType is None:
            raise StopValidation('Interval server error')

        if not roomType:
            raise StopValidation('This room type doesn\'eixsts ')

    def validate_roomLocation(self, field)->None:
        from database.methods import RoomLocation
        from database.session import session_query

        roomLocation = session_query(RoomLocation, id=field.data)
        if roomLocation is None:
            raise StopValidation('Internal server error')

        if not roomLocation:
            raise StopValidation('This location doens\' exists')


class FormRoomType(flask_wtf.FlaskForm):
    roomType_id = wtf.HiddenField(
        'RoomType Id'
        , validators=[InputRequired(), length(max=32)]
        , filters=[Forms.filter_str]
    )

    roomType_tag = wtf.StringField(
        'RoomType tag'
        , validators=[InputRequired(), length(min=1, max=155)]
        , filters=[Forms.filter_str]
    )
    roomType_description = wtf.StringField(
        'RoomType Description'
        , validators=[InputRequired(), length(min=1, max=155)]
        , filters=[Forms.filter_str]
    )
    roomType_capacity = wtf.IntegerField(
        'RoomType capacity'
        , validators=[InputRequired()]
    )
    roomType_price = wtf.FloatField(
        'RoomType price'
        , validators=[InputRequired()]
    )

    ##
    def __init__(self, *args, **kwargs)->None:
        super().__init__(*args, **kwargs)

        if not kwargs.get("room_id") is None:
            room_id = kwargs.get("room_id")
            self.populate(room_id)

    def populate(self, room_id)->None:
        from database.methods import RoomType
        from database.session import session_query

        
        room_tag, room_description, room_capacity, room_price = session_query(RoomType.tag, RoomType.description, RoomType.capacity, RoomType.price, id=room_id)[0]

        self.roomType_id.data = room_id
        self.roomType_tag.data = room_tag
        self.roomType_description.data = room_description
        self.roomType_capacity.data = room_capacity
        self.roomType_price.data = room_price

    ##
    def validate_roomType_id(self, field)->None:
        from database.methods import RoomType
        from database.session import session_query

        room = session_query(RoomType, id=field.data)
        if not room:
            raise StopValidation("Invalid RoomType")

    def validate_roomType_capacity(self, field)->None:
        if field.data < 1 or field.data > 100:
            raise StopValidation('Invalid capacity value')

    def validate_roomType_price(self, field)->None:
        if field.data < 1 or field.data > 10000:
            raise StopValidation('Invalid price value')

class FormRoomLocation(flask_wtf.FlaskForm):
    roomLocation_id = wtf.HiddenField(
        'Room Location id'
    )

    roomLocation_tag = wtf.StringField(
        'Room Location tag'
        , validators=[InputRequired(), length(min=1, max=155)]
        , filters=[Forms.filter_str]
    )
    roomLocation_tagPrefix = wtf.StringField(
        'Room Location tag prefix'
        , validators=[InputRequired(), length(min=1, max=3)]
        , filters=[Forms.filter_str]
    )
    roomLocation_tagSuffix = wtf.StringField(
        'Room Location tag suffix'
        , validators=[length(max=3)]
        , filters=[Forms.filter_str]
    )

    ##
    def __init__(self, *args, **kwargs)->None:
        super().__init__(*args, **kwargs)

        if not kwargs.get("room_id") is None:
            room_id = kwargs.get("room_id")
            self.populate(room_id)

    ##
    def populate(self, room_id)->None:
        from database.methods import RoomLocation
        from database.session import session_query

        room_tag, room_tagPrefix, room_tagSuffix = session_query(RoomLocation.tag, RoomLocation.tag_prefix, RoomLocation.tag_suffix, id=room_id)[0]

        self.roomLocation_id.data = room_id
        self.roomLocation_tag.data = room_tag
        self.roomLocation_tagPrefix.data = room_tagPrefix
        self.roomLocation_tagSuffix.data = room_tagSuffix

    ##
    def validate_roomLocation_id(self, field)->None:
        from database.methods import RoomLocation
        from database.session import session_query

        room = session_query(RoomLocation.id, id=field.data)
        if not room:
            raise StopValidation('Invalid room id')


    def validate_roomLocation_tagPrefix(self, field)->None:
        from database.methods import RoomLocation
        from database.session import session_query

        roomLocation_id = session_query(RoomLocation.id, tag_prefix=field.data)
        if not roomLocation_id:
            return

        if roomLocation_id[0][0] != self.roomLocation_id.data:
            raise StopValidation('This tag prefix already exist')

    def validate_roomLocation_tagSuffix(self, field)->None:
        from database.methods import RoomLocation
        from database.session import session_query

        if not field.data:
            return

        roomLocation_id = session_query(RoomLocation.id, tag_suffix=field.data)
        if not roomLocation_id:
            return

        if roomLocation_id[0][0] != self.roomLocation_id.data:
            raise StopValidation('This tag suffix already exist')

class FormRoomStatus(flask_wtf.FlaskForm):
    roomStatus_1_id = wtf.HiddenField(
        'Room Status Id Instance 1'
        , validators=[InputRequired(), length(max=16)]
        , filters=[Forms.filter_str]
    )
    roomStatus_2_id = wtf.HiddenField(
        'Room Status Id Instance 2'
        , validators=[InputRequired(), length(max=16)]
        , filters=[Forms.filter_str]
    )

    roomStatus_1_tag = wtf.StringField(
        'Room Status Tag Instance 1'
        , validators=[InputRequired(), length(min=1, max=155)]
        , filters=[Forms.filter_str]
    )
    roomStatus_2_tag = wtf.StringField(
        'Room Status Tag Instance 2'
        , validators=[InputRequired(), length(min=1, max=155)]
        , filters=[Forms.filter_str]
    )

    ##
    def __init__(self, *args, **kwargs)->None:
        super().__init__(*args, **kwargs)

        if not kwargs.get("room_id") is None:
            room_id = kwargs.get("room_id")
            self.populate(room_id)

    ##
    def populate(self, room_id:str)->None:
        from database.methods import RoomStatus
        from database.session import session_query, session_SQL

        room_1_id, room_1_tag, room_1_value  = session_query(RoomStatus.id, RoomStatus.tag, RoomStatus.value, id=room_id)[0]
        room_2_id, room_2_tag = session_SQL(f"""
        SELECT id, tag FROM \"RoomStatus\"
        WHERE value = {room_1_value} AND id <> '{room_1_id}'
        """).all()[0]

        self.roomStatus_1_id.data = room_1_id
        self.roomStatus_2_id.data = room_2_id

        self.roomStatus_1_tag.data = room_1_tag
        self.roomStatus_2_tag.data = room_2_tag

    ##
    def validate_roomStatus_1_id(self, field)->None:
        from database.methods import RoomStatus
        from database.session import session_query

        if not session_query(RoomStatus.id, id=field.data):
            raise StopValidation('Invalid Room Status Id Instance 1')

    def validate_roomStatus_2_id(self, field)->None:
        from database.methods import RoomStatus
        from database.session import session_query

        if not session_query(RoomStatus.id, id=field.data):
            raise StopValidation('Invalid Room Status Id Instance 2')


    def validate_roomStatus_1_tag(self, field)->None:
        from database.methods import RoomStatus
        from database.session import session_query

        roomStatus_1_id = session_query(RoomStatus.id, tag=field.data)
        if not roomStatus_1_id:
            return

        if roomStatus_1_id[0][0] != self.roomStatus_1_id.data:
            raise StopValidation('The Instance 1 tag already exist')

    def validate_roomStatus_2_tag(self, field)->None:
        from database.methods import RoomStatus
        from database.session import session_query

        roomStatus_2_id = session_query(RoomStatus.id, tag=field.data)
        if not roomStatus_2_id:
            return

        if roomStatus_2_id[0][0] != self.roomStatus_2_id.data:
            raise StopValidation('The Instance 2 tag already exist')
    
##
def register_app(app:object, **kwargs)->None:

    @app.route("/management/item/room/<topic>/tag/<room_tag>/display")
    @ManagerUser.required_permission(roleAdmin)
    def management_item_room_topic_tag_display(pkUser, topic:str, room_tag:str)->object:
        from database.session import session_query, model_from_name

        ##
        if not topic in Globals.FIELD_TOPICS['room']:
            flask.abort(404)

        model = model_from_name(topic)
        room_id = session_query(model.id, tag=room_tag)
        if room_id is None:
            flask.abort(500)

        if not room_id:
            flask.abort(4040)
        
        return flask.redirect(flask.url_for("management_item_room_topic_id_display", topic=topic, room_id=room_id[0][0]))

    @app.route("/management/item/room/<topic>/id/<room_id>/display")
    @ManagerUser.required_permission(roleAdmin)
    def management_item_room_topic_id_display(pkUser, topic:str, room_id:str)->object:
        from database.session import session_query, model_from_name

        ##
        if not topic in Globals.FIELD_TOPICS['room']:
            flask.abort(404)

        ##
        model = model_from_name(topic)
        if not model:
            flask.abort(404)

        room = session_query(model.id, id=room_id)
        if room is None:
            flask.abort(500)

        if not room:
            flask.abort(404)

        ##
        roomJson = None
        formsRoom = None
        forms_class = None
        template_path = ''

        if topic == 'Room':
            forms_class = FormRoom
            template_path = 'management/room/management_room.html'

        if topic == 'RoomType':
            forms_class = FormRoomType
            template_path = 'management/room/management_roomType.html'

        if topic == 'RoomLocation':
            forms_class = FormRoomLocation
            template_path = 'management/room/management_roomLocation.html'

        if topic == 'RoomStatus':
            forms_class = FormRoomStatus
            template_path = 'management/room/management_roomStatus.html'

        ##
        room_instance = session_query(model, id=room_id)[0]
        roomJson = room_instance.load_json()
        formsRoom = forms_class(room_id=room_id)

        return flask.render_template(template_path, formsRoom=formsRoom, roomJson=roomJson)


    ## Auth management auth
    @app.route("/management/item/room/Room/<room_id>/auth", methods=['POST'])
    @ManagerUser.required_permission(roleAdmin)
    def management_item_Room_auth(pkUser, room_id:str)->object:
        from begin.globals import Messages

        from database.methods import Room, RoomType, RoomLocation
        from database.session import session_SQL, session_query, instance_update

        ##
        formsRoom = FormRoom()
        # print('form: ', flask.request.form)
        if not formsRoom.validate_on_submit():
            # print(formsRoom.errors)
            forms_errors = Forms.forms_errors(formsRoom)
            return flask.jsonify({
                'message': Messages.MError(forms_errors[0]).json
            })

        ##
        room_id = formsRoom.room_id.data
        roomType_id = formsRoom.roomType.data
        roomLocation_id = formsRoom.roomLocation.data
        roomStatus = [ field.data for field_name, field in formsRoom.roomStatus._fields.items() if field_name != "csrf_token" ]
        
        ##
        status_value = session_SQL(OPTIONS_SQL_GET(roomStatus)).all()[0][0]

        room = session_query(Room, id=room_id)[0]
        # print('room: ', room, roomType_id, roomLocation_id, status_value)
        # print('room: ', room_id, roomType, roomLocation, roomStatus)
        instance_update(
            room
            , roomType_id = roomType_id
            , roomLocation_id = roomLocation_id
            , status_value = status_value
        )
        # print('status_value: ', status_value)

        return flask.jsonify({
            'message': Messages.MSuccess('Operation success completed').json
        })

    @app.route("/management/item/room/RoomType/<room_id>/auth", methods=['POST'])
    @ManagerUser.required_permission(roleAdmin)
    def management_item_RoomType_auth(pkUser, room_id:str)->object:
        from begin.globals import Messages

        from database.methods import RoomType
        from database.session import session_query, instance_update

        ##
        formsRoom = FormRoomType()
        if not formsRoom.validate_on_submit():
            forms_errors = Forms.forms_errors(formsRoom)
            return flask.jsonify({
                'message': Messages.MError(forms_errors[0]).json
            })

        roomType_id = formsRoom.roomType_id.data
        roomType_tag = formsRoom.roomType_tag.data
        roomType_description = formsRoom.roomType_description.data
        roomType_capacity = formsRoom.roomType_capacity.data
        roomType_price = formsRoom.roomType_price.data

        ##
        roomType = session_query(RoomType, id=roomType_id)[0]
        print('roomType: ', roomType, roomType_tag, roomType_description, roomType_capacity, roomType_price)
        instance_update(
            roomType
            , tag = roomType_tag
            , description = roomType_description
            , capacity = roomType_capacity
            , price = roomType_price
        )

        return flask.jsonify({
            'message': Messages.MSuccess('Operation completed').json
        })

    @app.route("/management/item/room/RoomLocation/<room_id>/auth", methods=['POST'])
    @ManagerUser.required_permission(roleAdmin)
    def management_item_RoomLocation_auth(pkUser, room_id:str)->object:
        from begin.globals import Messages

        from database.methods import RoomLocation
        from database.session import session_query, instance_update

        ##
        formsRoom = FormRoomLocation()
        if not formsRoom.validate_on_submit():
            forms_errors = Forms.forms_errors(formsRoom)
            return flask.jsonify({
                'message': Messages.MError(forms_errors[0]).json
            })

        roomLocation_id = formsRoom.roomLocation_id.data
        roomLocation_tag = formsRoom.roomLocation_tag.data
        roomLocation_tagPrefix = formsRoom.roomLocation_tagPrefix.data
        roomLocation_tagSuffix = formsRoom.roomLocation_tagSuffix.data or ''

        print('roomLocation: ', roomLocation_id, roomLocation_tag, roomLocation_tagPrefix, roomLocation_tagSuffix)

        ##
        roomLocation = session_query(RoomLocation, id=roomLocation_id)[0]
        instance_update(
            roomLocation
            , tag = roomLocation_tag
            , tag_prefix = roomLocation_tagPrefix
            , tag_suffix = roomLocation_tagSuffix
        )

        return flask.jsonify({
            'message': Messages.MSuccess('Operation completed').json
        })

    @app.route("/management/item/room/RoomStatus/<room_id>/auth", methods=['POST'])
    @ManagerUser.required_permission(roleAdmin)
    def management_item_RoomStatus_auth(pkUser, room_id:str)->object:
        from begin.globals import Messages

        from database.methods import RoomStatus
        from database.session import session_query, instance_update

        ##
        formsRoom = FormRoomStatus()
        if not formsRoom.validate_on_submit():
            forms_errors = Forms.forms_errors(formsRoom)
            return flask.jsonify({
                'message': Messages.MError(forms_errors[0]).json
            })

        roomStatus_1_id = formsRoom.roomStatus_1_id.data
        roomStatus_2_id = formsRoom.roomStatus_2_id.data

        roomStatus_1_tag = formsRoom.roomStatus_1_tag.data
        roomStatus_2_tag = formsRoom.roomStatus_2_tag.data

        ##
        roomStatus_1 = session_query(RoomStatus, id=roomStatus_1_id)[0]
        roomStatus_2 = session_query(RoomStatus, id=roomStatus_2_id)[0]

        instance_update(
            roomStatus_1
            , tag = roomStatus_1_tag
        )

        instance_update(
            roomStatus_2
            , tag = roomStatus_2_tag
        )

        return flask.jsonify({
            'message': Messages.MSuccess('Operation Completed').json
        })
