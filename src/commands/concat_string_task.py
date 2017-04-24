from context.abstract_context import RuntimeContext
from task.task import Task
from task.task_builder import parse_object


class ConcatStringTask(Task):
    def __init__(self, options: list):
        super().__init__(None)
        self.options = options

    def execute(self, context: RuntimeContext, input_value, result_set: dict):
        results = map(lambda task: self.get_or_execute(context, input_value, result_set, task), self.options)
        return "".join(results)

    @classmethod
    def get_task(cls, command: str, option):
        if not isinstance(option, list):
            raise Exception("invalidated option type. concat tasks only implicit list type.")
        opt_tasks = list(map(lambda x: parse_object(x), option))
        return ConcatStringTask(opt_tasks)
