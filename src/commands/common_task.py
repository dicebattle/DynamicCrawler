from context.abstract_context import RuntimeContext
from task.task import Task
from task.task_builder import parse_object


class CommonTask(Task):
    def __init__(self, command: str, option):
        super().__init__(option)
        self.command = command

    def execute(self, context: RuntimeContext, input_value, result_set: dict):
        if self.command == "$use":
            value = self.get_value(context, input_value, result_set)
            return value

        if self.command == "$use_list":
            value = self.get_value(context, input_value, result_set)
            if not isinstance(value, list):
                value = [value]
            return value

        if self.command == "$as":
            key = self.get_option_val(context, input_value, result_set)
            if isinstance(key, str) and key.startswith("$"):
                raise Exception("the key can not be started with $")
            result_set[key] = input_value
            return input_value

    def get_value(self, context, input_value, result_set):
        if self.option_val == "$self":
            return input_value
        else:
            return self.get_option_val(context, input_value, result_set)

    @classmethod
    def get_task(cls, command: str, option):
        opt_task = parse_object(option)
        return CommonTask(command, opt_task)
