filter_str = lambda value: value.strip() if value else None

forms_errors = lambda *forms: [
        ': '.join([ form[tag].label.text, ', '.join(errors)])
    for form in forms
    for tag, errors in form.errors.items()
]

# def add_field(forms, forms_data, field, field_name):
def add_field(forms, field_name, field)->None:
    if hasattr(forms, field_name):
        return

    setattr(forms, field_name, field)
