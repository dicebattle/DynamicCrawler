from context.abstract_context import RuntimeContext
from task.task import Task
from task.task_builder import parse_object


class BSSelectTask(Task):
    def __init__(self, command: str, option):
        super().__init__(option)
        self.command = command

    def execute(self, context: RuntimeContext, input_value, result_set: dict):
        method = getattr(input_value, self.command[1:])
        value = self.get_option_val(context, input_value, result_set)
        if not isinstance(value, str):
            raise Exception("select command accepts only string type.")
        return method(value)

    @classmethod
    def get_task(cls, command: str, option):
        opt_task = parse_object(option)
        return BSSelectTask(command, opt_task)
