import unicodedata
def remove_marked_str(string:str)->str:
    text_formated=unicodedata.normalize('NFD',string)
    text_no_marked=[i for i in text_formated if not unicodedata.combining(i)]
    return ''.join(text_no_marked)

