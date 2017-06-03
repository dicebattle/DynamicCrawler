from context.abstract_context import RuntimeContext


class CeleryRuntimeContext(RuntimeContext):
    def __init__(self):
        self.cookie_dict = None

    def get_last_cookie_dict(self):
        return self.cookie_dict

    def set_cookie_dict(self, cookie_dict):
        self.cookie_dict = cookie_dict
