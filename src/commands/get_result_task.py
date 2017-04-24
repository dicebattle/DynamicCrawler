from context.abstract_context import RuntimeContext
from task.task import Task


class GetResultTask(Task):
    def __init__(self, key: str):
        super().__init__(None)
        self.key = key

    def execute(self, context: RuntimeContext, input_value, result_set: dict):
        if self.key == "$self":
            return input_value
        return result_set[self.key]

    @classmethod
    def get_task(cls, command: str, option):
        if command.startswith("$$"):
            if command[3] == "$":
                raise Exception("invalidated key")
            return GetResultTask(command[2:])
        else:
            return GetResultTask(command)
