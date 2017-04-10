from context.abstract_context import RuntimeContext
from task.task import Task
from task.task_builder import parse_object


class TaskArray(Task):
    def __init__(self, task_list):
        self.task_list = task_list

    def execute(self, context: RuntimeContext, input_value, result_set: dict):
        last_input = input_value
        for task in self.task_list:
            if isinstance(task, Task):
                last_input = task.execute(context, last_input, result_set)
            else:
                last_input = task

        return last_input

    @classmethod
    def get_task(cls, command: str, option):
        if not isinstance(option, list):
            raise Exception("task array taske only list type for option")

        task_list = list(map(lambda x: cls.gen_task(x), option))
        return TaskArray(task_list)

    @classmethod
    def gen_task(cls, value):
        if isinstance(value, Task):
            return value
        return parse_object(value)
