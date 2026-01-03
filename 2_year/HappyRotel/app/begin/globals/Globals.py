## Field: topics
FIELD_TOPICS = {
    'room': [
        'Room'
        , 'RoomType'
        , 'RoomStatus'
        , 'RoomLocation'
    ]

    , 'user': [
        'User'
        , 'UserInfos'
        , 'UserPermission'
    ]

    , 'invoice': [
        'Invoice'
        , 'InvoiceItem'
        , 'InvoiceStatus'
    ]

    , 'reserve': [
        'Reserve'
        , 'ReserveCandidatea'
        , 'ReserveStatus'
    ]
}

TOPICS_ABLE = []
for field, topics in FIELD_TOPICS.items():
    TOPICS_ABLE.extend(topics)
