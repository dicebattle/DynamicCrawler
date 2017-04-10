from abc import ABCMeta, abstractmethod


class RuntimeContext(metaclass=ABCMeta):
    def __init__(self):
        self.cookie_dict = None

    def get_last_cookie_dict(self):
        return self.cookie_dict

    def set_cookie_dict(self, cookie_dict):
        self.cookie_dict = cookie_dict
