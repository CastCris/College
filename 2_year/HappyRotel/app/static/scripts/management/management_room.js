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
    console.log('AAA');

    const form_data = page.forms_validation(FORMS_ROOM);
    if(!form_data)
        return;

    console.log(form_data);
    fetch(`/management/room/${form_data.get("roomTag")}/auth`, {
        method: 'POST'
        , headers: { 'Content-Type': 'application/json; charset=utf-8' }
        , body: JSON.stringify(Object.fromEntries(form_data))
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
    });
});

//
page.elements_init();
