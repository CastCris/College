filter_str = lambda value: value.strip() if value else None

forms_errors = lambda *forms: [
        ': '.join([ form[tag].label.text, ', '.join(errors)])
    for form in forms
    for tag, errors in form.errors.items()
]
