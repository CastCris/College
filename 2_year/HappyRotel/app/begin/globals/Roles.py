from begin.globals.flask_auth import Role

##
roleAdmin = Role({
    "MANAGE_USER": 1
    , "MANAGE_ROOM": 2
    , "MANAGE_INVOICE": 4
    , "MANAGE_RESERVE": 8
})

roleEmployer = Role([
    "MANAGE_INVOICE"
    , "MANAGE_RESERVE"
], role=roleAdmin)

roleManager = Role([
    "MANAGE_ROOM"
    , "MANAGE_INVOICE"
    , "MANAGE_RESERVE"
], role=roleAdmin)
