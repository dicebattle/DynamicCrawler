from context.abstract_context import RuntimeContext
from task.task import Task
from task.task_builder import parse_object


class MapTask(Task):
    def __init__(self, option, flatten: bool):
        super().__init__(option)
        self.flatten = flatten

    def execute(self, context: RuntimeContext, input_value, result_set: dict):
        if not isinstance(input_value, list):
            raise Exception("invalidated type input_value. it is not list type.")
        res = []
        for i in input_value:
            x = self.get_option_val(context, i, result_set)
            if self.flatten and isinstance(x, list):
                res.extend(x)
            else:
                res.append(x)
        return res

    @classmethod
    def get_task(cls, command: str, option):
        if command == "$flat_map":
            flatten = True
        else:
            flatten = False
        opt_task = parse_object(option)
        return MapTask(opt_task, flatten)
