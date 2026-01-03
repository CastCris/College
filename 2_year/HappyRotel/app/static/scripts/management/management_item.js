import * as global from '../globals.js'

//
const layout_1 = new global.Layout_1();
const page = new global.Page();

//
const FORMS_USER = new global.Element(page, {
    'id': "formsItem"
});

//
FORMS_USER.addEventListener('submit', e => {
    e.preventDefault();

    //
    const formData = page.forms_validation(FORMS_USER)
    if(!formData)
        return;

    console.log(formData);
    fetch(`/management/item/${formData.get("field")}/${formData.get("topic")}/auth`, {
        method: 'POST'
        , body: formData
    })
    .then(response => response.json())
    .then(data => {
        const message = data["message"];
        page.LOGS.INSERT(message);
    });
});
