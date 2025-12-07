import { Layout_2, Page, Element } from './globals.js'

//
const layout_2 = new Layout_2();
const page = new Page();

//
const FORMS_USER = new Element(page, {
    'id': "login_form_user"
});
const tFORMS_CAPTCHA = new Element(page, {
    'id': "login_form_captcha"
});



const BUTT_CAPTCHA_GENERATE = new Element(page, {
    'id': "login_form_catpcha_IMG_button_generate",
});
const BUTT_SUBMIT = new Element(page, {
    'id': "login_form_button_submit"
});

//
BUTT_CAPTCHA_GENERATE.addEventListener('click', (e) => {
    e.preventDefault();

    //
    console.log('AAA');
});

BUTT_SUBMIT.addEventListener('click', (e) => {
    e.preventDefault();

    //
    console.log('Submit');
});

//
console.log(page);
page.elements_init(Object.keys(window));
