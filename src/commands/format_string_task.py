from commands.literal_task import LiteralTask
from context.abstract_context import RuntimeContext
from task.task import Task
from task.task_builder import parse_object

class FormatStringTask(Task):
    def __init__(self, format_: str, args: list):
        super().__init__(args)
        self.format = format_
    def execute(self, context: RuntimeContext, input_value, result_set: dict):
        return self.format % tuple(self.get_option_val(context, input_value, result_set))
    @classmethod
    def get_task(cls, command: str, option):
        format_ = option.get("$format", None)
        args = option.get("$args", None)
        if not isinstance(format_, str):
            raise Exception("format should be string type")
        if not isinstance(args, list):
            raise Exception("args should be implicit list type")
        args = LiteralTask.get_task("$literal", args)
        return FormatStringTask(format_, args)
