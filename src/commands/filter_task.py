from context.abstract_context import RuntimeContext
from task.task import Task
from task.task_builder import parse_object

class FilterTask(Task):
    def __init__(self, option, expect: bool):
        super().__init__(option)
        self.expect = expect

    def execute(self, context: RuntimeContext, input_value, result_set: dict):
        if not isinstance(input_value, list):
            raise Exception("invalidated type input_value. it is not list type.")
        res = []
        for i in input_value:
            if bool(self.get_option_val(context, i, result_set)) is self.expect:
                res.append(i)
        return res

    @classmethod
    def get_task(cls, command: str, option):
        if command == "$filter":
            expect = True
        else:
            expect = False
        opt_task = parse_object(option)
        return FilterTask(opt_task, expect)
