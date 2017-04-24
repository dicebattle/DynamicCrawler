from context.abstract_context import RuntimeContext
from task.task import Task


class GetAttrTask(Task):
    def __init__(self, command: str, option):
        super().__init__(option)
        self.command = command

    def execute(self, context: RuntimeContext, input_value, result_set: dict):
        return getattr(input_value, self.option)

    @classmethod
    def get_task(cls, command: str, option):
        if not isinstance(option, str):
            raise Exception("option should be str type")
        return GetAttrTask(command, option)
