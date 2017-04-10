from abc import ABCMeta, abstractmethod

from context.abstract_context import RuntimeContext


class Task(metaclass=ABCMeta):
    def __init__(self, option):
        self.option = option
        self.option_val = None
        if not isinstance(option, Task):
            self.option_val = option

    def get_option_val(self, context: RuntimeContext, input_value, result_set: dict):
        if self.option_val is None:
            return self.option.execute(context, input_value, result_set)
        return self.option_val

    @staticmethod
    def get_or_execute(context: RuntimeContext, input_value, result_set: dict, task):
        if task is None:
            return None
        if isinstance(task, Task):
            return task.execute(context, input_value, result_set)
        return task

    @abstractmethod
    def execute(self, context: RuntimeContext, input_value, result_set: dict):
        return input_value

    @classmethod
    def get_task(cls, command: str, option):
        return Task(option)
