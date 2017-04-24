from context.abstract_context import RuntimeContext
from task.task import Task
from task.task_builder import parse_object


class MkStringTask(Task):
    def __init__(self, option):
        super().__init__(option)

    def execute(self, context: RuntimeContext, input_value, result_set: dict):
        if not isinstance(input_value, list):
            raise Exception("invalidated input_value type. mk_string tasks only list type for input.")
        return self.get_option_val(context, input_value, result_set).join(input_value)

    @classmethod
    def get_task(cls, command: str, option):
        opt_task = parse_object(option)
        return MkStringTask(opt_task)
