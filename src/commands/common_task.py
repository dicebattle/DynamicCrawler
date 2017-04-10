from context.abstract_context import RuntimeContext
from task.task import Task
from task.task_builder import parse_object


class CommonTask(Task):
    def __init__(self, command: str, option):
        super().__init__(option)
        self.command = command

    def execute(self, context: RuntimeContext, input_value, result_set: dict):
        pass

    def get_value(self, context, input_value, result_set):
        pass

    @classmethod
    def get_task(cls, command: str, option):
        opt_task = parse_object(option)
        return CommonTask(command, opt_task)
