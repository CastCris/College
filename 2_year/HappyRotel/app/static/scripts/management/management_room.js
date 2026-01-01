import * as global from "../globals.js"

//
const layout_1 = new global.Layout_1();
const page = new global.Page();

//
const FORMS_ROOM = new global.Element(page, {
    "id": "formsRoom"
});

const BUTT_SUBMIT = new global.Element(page, {
    "id": "formsRoom_button_submit"
});

//
BUTT_SUBMIT.addEventListener('click', (e) => {
    e.preventDefault();

    const form_data = page.forms_validation(FORMS_ROOM);
    if(!form_data)
        return;

    console.log(form_data);
    fetch(`/management/item/room/Room/${form_data.get("room_id")}/auth`, {
        method: 'POST'
        //, headers: { 'Content-Type': 'application/json; charset=utf-8' }
        //, body: JSON.stringify(Object.fromEntries(form_data))
        , body: form_data
    })
    .then(response => response.json())
    .then(data => {
        const message = data["message"];
        page.LOGS.INSERT(message);
    });
});
