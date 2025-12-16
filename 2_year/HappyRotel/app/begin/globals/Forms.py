filter_str = lambda value: value.strip() if value else None

forms_errors = lambda *forms: [
    ': '.join([ tag, ', '.join(value) ])
    for i in range(len(forms))
    for tag, value in forms[i].errors.items() 
]
