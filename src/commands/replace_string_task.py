import re
from context.abstract_context import RuntimeContext
from task.task import Task


class ReplaceStringTask(Task):
    def __init__(self, find, find_regex, to, replace_cnt: int):
        super().__init__(None)
        self.find = find
        self.find_regex = find_regex
        self.to = to
        self.replace_cnt = replace_cnt

    def execute(self, context: RuntimeContext, input_value, result_set: dict):
        if self.find:
            return str(input_value).replace(self.find, self.to, self.replace_cnt)
        else:
            return re.sub(self.find_regex, self.to, str(input_value), 0 if self.replace_cnt <= 0 else self.replace_cnt)

    @classmethod
    def get_task(cls, command: str, option):
        find = option.get("$find", None)
        find_regex = option.get("$find_regex", None)
        to = option.get("$to", None)
        if not (find or find_regex):
            raise Exception("invalidated argument. $find or $find_regex required.")
        if command == "$replace_once":
            return ReplaceStringTask(find, find_regex, to, 1)
        else:
            return ReplaceStringTask(find, find_regex, to, -1)
