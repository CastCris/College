import * as global from './globals.js'

//
const layout_2 = new global.Layout_2();
const page = new global.Page();

let timeout_captcha_generate = null;

//
const FORMS_USER = new global.Element(page, {
    'id': "form_user"
});
const FORMS_CAPTCHA = new global.Element(page, {
    'id': "form_captcha"
});


const IMG_CAPTCHA = new global.Element(page, {
    'id': "form_captcha_image"
});


const BUTT_CAPTCHA_GENERATE = new global.Element(page, {
    'id': "form_captcha_button_generate"
});
const BUTT_SUBMIT = new global.Element(page, {
    'id': "form_button_submit"
});

//
BUTT_CAPTCHA_GENERATE.addEventListener('click', (e) => {
    e.preventDefault();

    //
    clearTimeout(timeout_captcha_generate);
    timeout_captcha_generate = setTimeout(() => {
        page.captcha_generate_IMG(IMG_CAPTCHA);
    }, 200);
});

BUTT_SUBMIT.addEventListener('click', (e) => {
    e.preventDefault();

    //
    const forms = page.forms_validation(FORMS_USER, FORMS_CAPTCHA);
    if(!forms)
        return;

    fetch('/login/auth', {
        method: 'POST',
        headers: {'Content-Type': 'application/json; charset=utf-8'},

        body: JSON.stringify(Object.fromEntries(forms))
    })
    .then(response => {
        console.log(response)
        if(response.redirected){
            /*
            console.log(response, response.url);
            window.location.href = response.url;
            return;
            */
            throw new Error("Redirected", {
                cause: response.url
            });
        }

        return response.json()
    })
    .then(data => {
        const message = data["message"];
        page.LOGS.INSERT(message);
    })
    .catch(err => {
        if(err.message == "Redirected"){
            window.location.href = err.cause
            return
        }

        console.log(err);
    });


});

//
page.captcha_generate_IMG(IMG_CAPTCHA);
