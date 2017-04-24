from context.abstract_context import RuntimeContext
from task.task import Task
from task.task_builder import parse_object


class DropTask(Task):
    def __init__(self, options: list):
        super().__init__(None)
        self.options = options

    def execute(self, context: RuntimeContext, input_value, result_set: dict):
        drops = list(map(lambda task: self.get_or_execute(context, input_value, result_set, task), self.options))
        result = []
        for x in range(len(input_value)):
            if x not in drops:
                result.append(input_value[x])
        return result

    @classmethod
    def get_task(cls, command: str, option):
        if not isinstance(option, list):
            option = [option]
        opt_tasks = list(map(lambda x: parse_object(x), option))
        return DropTask(opt_tasks)
