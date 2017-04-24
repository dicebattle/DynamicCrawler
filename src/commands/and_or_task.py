from context.abstract_context import RuntimeContext
from task.task import Task
from task.task_builder import parse_object

class AndTask(Task):
    def __init__(self, options: list):
        super().__init__(None)
        self.options = options

    def execute(self, context: RuntimeContext, input_value, result_set: dict):
        results = []
        for x in self.options:
            res = self.get_or_execute(context, input_value, result_set, x)
            if res:
                results.append(res)
            else:
                return False
        return results

    @classmethod
    def get_task(cls, command: str, option):
        if not isinstance(option, list):
            raise Exception("invalidated option type. union tasks only implicit list type.")
        opt_tasks = list(map(lambda x: parse_object(x), option))
        return AndTask(opt_tasks)


class OrTask(Task):
    def __init__(self, options: list):
        super().__init__(None)
        self.options = options

    def execute(self, context: RuntimeContext, input_value, result_set: dict):
        for x in self.options:
            res = self.get_or_execute(context, input_value, result_set, x)
            if res:
                return res
        return False

    @classmethod
    def get_task(cls, command: str, option):
        if not isinstance(option, list):
            raise Exception("invalidated option type. union tasks only implicit list type.")
        opt_tasks = list(map(lambda x: parse_object(x), option))
        return OrTask(opt_tasks)
