import * as global from "../globals.js"

//
const layout = new global.Layout_1();
const page = new global.Page();

//
const FORMS_ROOM = new global.Element(page, {
    'id': "formsRoom"
});

const BUTT_SUBMIT = new global.Element(page, {
    'id': "formsRoom_button_submit"
});

//
BUTT_SUBMIT.addEventListener('click', e => {
    e.preventDefault();

    //
    const formData = page.forms_validation(FORMS_ROOM);
    if(!formData)
        return;

    console.log(formData);
    fetch(`/management/item/room/RoomLocation/${formData.get("roomLocation_id")}/auth`, {
        method: 'POST'
        , body: formData
    })
    .then(response => response.json())
    .then(data => {
        const message = data["message"];
        page.LOGS.INSERT(message);
    })
});
