ANSI_COLOR_RED = '\033[91m'
ANSI_COLOR_NULL = '\033[0m'

## Message
class Message():
    def __init__(self, type:str, content:str):
        self.type = type
        self.content = content

    @property
    def json(self)->dict:
        return {
            "content": self.content,
            "type": self.type
        }

class MError(Message):
    def __init__(self, content:str)->None:
        self.content=content
        self.type = Error.js_class

## Error & Succcess
class Error():
    js_class="log_message_erro"

    def print(func_name:str, e:object)->None:
        print(f"{func_name} {ANSI_COLOR_RED}ERROR{ANSI_COLOR_NULL}: {e}")

class Success():
    js_class = "log_message_ok"

## Captcha
class Captcha():
    class Error(Error):
        invalid = Message(
            content="Invalid Captcha",
            type=Error.js_class
        )
        invalid_type = Message(
            content="Invalid Catpcha type",
            type=Error.js_class
        )
        not_requested = Message(
            content="Captcha not requested",
            type=Error.js_class
        )

    class Success(Success):
        ok = Message(
            content="Valid captcha",
            type=Success.js_class
        )

## Request
class Request():
    class Error(Error):
        internal = Message(
            content="Something goes wrong",
            type=Error.js_class
        )

        invalid_method = Message(
            content="Method not allow",
            type=Error.js_class
        )
        invalid_fields = Message(
            content="Invalid fields",
            type=Error.js_class
        )


        missing_fields = Message(
            content="Missing fields",
            type=Error.js_class
        )
        empty_fields = Message(
            content="Please, fill all required fields",
            type=Error.js_class
        )

        def invalid_client_behavior(timestamp):
            import time

            date = time.localtime(timestamp)

            return f"Because of your behavior, you cannot try sign after {date.tm_hour}:{date.tm_min}:{date.tm_sec}"

## Login
class Login():
    class Error(Error):
        user_not_found = Message(
            content="User not found",
            type=Error.js_class
        )
        invalid_user_password = Message(
            content="User password incorrect",
            type=Error.js_class
        )
        user_already_logged = Message(
            content="User already logged",
            type=Error.js_class
        )

    class Request(Request):
        pass

    class Success(Success):
        pass

## Sign
class Sign():
    class Error(Error):
        user_already_exists = Message(
            content = 'This user already exists',
            type = Error.js_class
        )

    class Request(Request):
        pass
