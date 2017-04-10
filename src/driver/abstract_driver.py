from abc import ABCMeta, abstractmethod


class AbstractDriver(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __del__(self):
        pass

    @abstractmethod
    def load_webpage(self, url):
        pass