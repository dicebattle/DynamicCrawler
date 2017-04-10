from context.abstract_context import RuntimeContext
from task.task import Task


class BSFindTask(Task):
    def __init__(self, command: str, option):
        super().__init__(option)
        self.command = command

    def execute(self, context: RuntimeContext, input_value, result_set: dict):
        method = getattr(input_value, self.command[1:])
        tag = self.option.get("$tag", None)
        attr = self.option.get("$attr", None)
        rec = self.option.get("$rec", True)
        return method(tag, attr, rec)

    @classmethod
    def get_task(cls, command: str, option):
        return BSFindTask(command, option)
