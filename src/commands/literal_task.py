from context.abstract_context import RuntimeContext
from task.task import Task
from task.task_builder import parse_object
import numbers


class LiteralTask(Task):
    def __init__(self, option):
        super().__init__(None)
        self.option = option
    def execute(self, context: RuntimeContext, input_value, result_set: dict):
        option = self.option
        if isinstance(option, dict):
            return dict(map(lambda x: (x, self.get_or_execute(context, input_value, result_set, option[x])), option))
        elif isinstance(option, list):
            return list(map(lambda task: self.get_or_execute(context, input_value, result_set, task), option))
        else:
            return option
    @classmethod
    def get_task(cls, command: str, option):
        if not option:
            raise Exception("option value is None")
        if command == "$literal_rec":
            return cls.check_option(option)
        if isinstance(option, dict):
            new_dict = dict(map(lambda x: (cls.check_option(x), parse_object(option[x])), option))
            return LiteralTask(new_dict)
        elif isinstance(option, list):
            new_list = list(map(lambda x: parse_object(x), option))
            return LiteralTask(new_list)
        elif isinstance(option, numbers.Number):
            return list(map(lambda x: cls.check_option(x), option))
        elif isinstance(option, str):
            if option.startswith("$"):
                raise Exception("unable to use command in literal")
            else:
                return option
        raise Exception("unsupported type : " + str(type(option)))
    @classmethod
    def check_option(cls, option):
        if isinstance(option, dict):
            return dict(map(lambda x: (cls.check_option(x), cls.check_option(option[x])), option))
        elif isinstance(option, list):
            return list(map(lambda x: cls.check_option(x), option))
        elif isinstance(option, numbers.Number):
            return option
        elif isinstance(option, str):
            if option.startswith("$"):
                raise Exception("unable to use command in literal")
            else:
                return option
        raise Exception("unsupported type : " + str(type(option)))