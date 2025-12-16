import * as global from './globals.js'

//
const layout_2 = new global.Layout_2();
const page = new global.Page();

let timeout_captcha_generate = null;

//
const FORMS_USER = new global.Element(page, {
    id: "sign_form_user"
});
const FORMS_CAPTCHA = new global.Element(page, {
    id: "sign_form_captcha"
});

const IMG_CAPTCHA = new global.Element(page, {
    'id': "sign_form_captcha_image"
})

const BUTT_CAPTCHA_GENERATE = new global.Element(page, {
    'id': "sign_form_captcha_button_generate"
});
const BUTT_SUBMIT = new global.Element(page, {
    'id': "sign_form_button_submit"
});

//
BUTT_CAPTCHA_GENERATE.addEventListener('click', (e) => {
    e.preventDefault();

    //
    clearTimeout(timeout_captcha_generate);
    timeout_captcha_generate = setTimeout(() => {
        global.captcha_generate_IMG(IMG_CAPTCHA.get_object());
    }, 200);
});

BUTT_SUBMIT.addEventListener('click', (e) => {
    e.preventDefault();

    //
    const forms = global.forms_validation(FORMS_USER.get_object(), FORMS_CAPTCHA.get_object());
    if(!forms)
        return;

    fetch('/sign/auth', {
        method: 'POST',
        headers: {'Content-Type': 'application/json; charset=utf-8'},

        body: JSON.stringify(Object.fromEntries(forms))
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
    });

});

//
page.elements_init(Object.keys(window));

//
global.captcha_generate_IMG(IMG_CAPTCHA.get_object());
