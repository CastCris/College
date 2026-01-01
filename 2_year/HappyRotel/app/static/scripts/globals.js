// Validations

export function fieldSetData(...fieldSet){
    const data = {};
    for(const i of fieldSet){
        const inputs = i.querySelectorAll('input, select, textarea');

        for(const j of inputs){
            data[j.name] = data[j.name] || []
            data[j.name].push(j.value);
        }
    }

    return data;
}


// Internal
/*
function instanceMethods(instance){
    return Object.getOwnPropertyNames(instance.__proto__).filter(
        funcName => funcName != "constructor"
    )
}

function instanceAttributes(instance){
    return Object.getOwnPropertyNames(instance)

function instanceProperties(instance){
    return [ ...(instanceMethods(instance)), ...(instanceAttributes(instance)) ]
}
*/

// Layouts / Message 
export class Layout_1{
    constructor(){
        this.TAGS_NAMES = [ ...(document.getElementsByTagName("*")) ];

        this.ELEMENTS_BY_CLASS = {};
        this.ELEMENTS_BY_TAG = {};
        this.ELEMENT_BY_ID = {};

        this.TAGS_NAMES.forEach( (i) => {
            if(!(i.className in Object.keys(this.ELEMENTS_BY_CLASS)) && i.className)
                this.ELEMENTS_BY_CLASS[i.className] = [ ...(document.getElementsByClassName(i.className)) ];

            if(!(i.tagName in Object.keys(this.ELEMENTS_BY_TAG)) && i.tagName)
                this.ELEMENTS_BY_TAG[i.tagName.toLowerCase()] = [ ...(document.getElementsByTagName(i.tagName)) ];

            if(!(i.id in Object.keys(this.ELEMENT_BY_ID)) && i.id)
                this.ELEMENT_BY_ID[i.id] = document.getElementById(i.id);
        })

        //
        this.CSS_VARS = window.getComputedStyle(document.body);

        //
        this.resize_timeout;

        window.addEventListener('resize', () => {
            clearTimeout(this.resize_timeout);

            this.resize_timeout = setTimeout(() =>{
                this.set_dynamic_classNames();
            }, 200);
        });

        this.set_dynamic_classNames();
    }

    set_dynamic_classNames(){
        const className_by_tagName= (element, prefix) => {
            return `${prefix}__${element.tagName.toLowerCase()}`
        };

        const className_by_id = (element, prefix) => {
            return `${prefix}__${element.id}`
        };

        const classNames_by_classes = (element, prefix) => {
            const classNames = [];
            const regex = new RegExp(`^${prefix}__.*`);

            for(const i of element.classList){
                if(regex.test(i)){
                    classNames.push(i);
                    continue;
                }

                classNames.push(`${prefix}__${i}`);
            }

            return classNames;
        }

        //
        const vp_ratio = this.get_screen_ratio();
        const prefixes = [ "reduce", "expand" ];
        const index = ( vp_ratio >= 1 ) + 0;

        const prefix_remove = prefixes[!index + 0];
        const prefix_add = prefixes[index];

        //
        for(const i of Object.keys(this.ELEMENTS_BY_TAG)){
            this.ELEMENTS_BY_TAG[i].forEach((j) => {
                if(j.classList.length){
                    j.classList.remove(...(classNames_by_classes(j, prefix_remove)));
                    j.classList.add(...(classNames_by_classes(j, prefix_add)));
                }

                // j.classList.remove(className_by_tagName(j, prefix_remove));
                j.classList.add(className_by_tagName(j, prefix_add));

                if(j.id){
                    // j.classList.remove(className_by_id(j, prefix_remove));
                    j.classList.add(className_by_id(j, prefix_add));
                }

            });
        }
    }

    get_screen_ratio(){
        return window.screen.width / window.screen.height;
    }
}

export class Layout_2 extends Layout_1{
    constructor(){
        super();
    }
}

export class MessageLogs{
    constructor(){
        const page_layout = new Layout_1();
        const ELEMENT_BY_ID = page_layout.ELEMENT_BY_ID;

        //
        this.BOX = ELEMENT_BY_ID["message_logs"];

        this.MESSAGE_ERROR_CLASS = 'message_error';

        //
        this.CLEAN = () => {
            this.BOX.innerHTML = '';
        };

        this.ADD = (message_class, message) => {
            this.BOX.innerHTML += `
                <p class="${message_class}">${message}</p>
        `
        };

        this.INSERT = (message_obj) => {
            this.CLEAN();
            this.ADD(message_obj["type"], message_obj["content"]);
        }
    }
}

// EventListenr | Element | Page
class EventListener {
    constructor(args) {
        this.TYPE = args["type"];
        this.FUNC = args["func"];
    }
}

export class Element {
    constructor(page, args){
        this._object = args["object"] || null;
        this._objectId = args["id"];
        this._eventListeners = args["eventListeners"] || [];

        this.init();
        page.elements_add(this);

        return new Proxy(this, {
            get: (target, property, receiver) => {
                const attr_target = Reflect.get(target, property, receiver);
                const attr_object = this._object[property];

                if(attr_target && typeof attr_target == "function")
                    return attr_target.bind(target);
                else if(attr_target)
                    return attr_target;

                if(attr_object && typeof attr_object == "function")
                    return attr_object.bind(this._object(property));
                else if(attr_object)
                    return attr_object;
            },

            set: (target, property, value) => {
                if(property in target){
                    Reflect.set(target, property, value);
                    return true;
                }

                target._object[property] = value;
                return true
            }
        });
    }

    // Replace HTMLElement methods
    addEventListener(type, func){
        this._eventListeners.push(new EventListener({
            type: type,
            func: func
        }));

        if(!this._object)
            return;

        this._object.addEventListener(type, func);
    }

    // getter / setter
    get raw(){
        return this._object;
    }

    //
    init(){
        this._object = document.getElementById(this._objectId);
        console.log(this._object, this._objectId);
        if(!this._object)
            return;

        for(const i of this._eventListeners){
            // console.log(this._object, i.TYPE, i.FUNC);
            this._object.addEventListener(i.TYPE, i.FUNC);
        }
    }

    copy(){
        const elementCopy = new Element(this.page, this._objectId, {
            "eventListeners": this._eventListeners
        });

        return elementCopy;
    }

    remove(){
        delete this.page.OBJECTS[this.id]
    }
}

export class Page{
    constructor(){
        this.OBJECTS = {};
        this.LOGS = new MessageLogs();
    }

    elements_add(...elements){
        for(const i of elements)
            this.OBJECTS[i.id] = i;
    }

    elements_init(){
        for(const i of Object.values(this.OBJECTS))
            i.init()
    }

    element_create(id, args){
        const new_element = new Element(this, id, {
            "object": document.createElement(id)
        });
        args = args || {};

        for(const i in args){
            new_element[i] = args[i];
        }

        return new_element;
    }

    element_remove(id){
        this.OBJECTS[id].remove();
    }

    //
    forms_validation(...forms){
        const logs = new MessageLogs();
        const formData = new FormData();

        for(const i of forms){
            const form_raw = i.raw;
            const form_data = new FormData(form_raw);
            const fields_required =  document.querySelectorAll(`#${form_raw.id} [required]`) || [];
            // console.log(form_data, fields_required);

            for(const j of fields_required){
                const field = form_data.get(j.name)
                const field_type = typeof field;

                if(field_type == "string" && field.trim())
                    continue;

                if(field_type == "object" && field instanceof File && field.size)
                    continue;

                logs.CLEAN();
                logs.ADD(logs.MESSAGE_ERROR_CLASS, "Please, fill all required fields");

                j.focus()

                return null;
            }

            form_data.forEach((value, key) => {
                formData.append(key, value);
            });
        }

        return formData;
    }

    captcha_generate_IMG(img_source){
        csrf_token = document.getElementById("csrf_token");

        fetch('/captcha/generate', {
            method: 'POST',
            headers: {'Content-Type': 'application/json; charset=utf-8'},

            body: JSON.stringify({
                'csrf_token': csrf_token.value,
                'captchaType': 'img'
            })
        })
        .then(response => response.blob())
        .then(blob => {
            const url = URL.createObjectURL(blob);
            img_source.src = url;
        });
    }
}
