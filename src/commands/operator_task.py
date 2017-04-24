from context.abstract_context import RuntimeContext
from task.task import Task
from task.task_builder import parse_object


class OperatorTask(Task):
    def __init__(self, command: str, option):
        super().__init__(option)
        self.command = command

    def execute(self, context: RuntimeContext, input_value, result_set: dict):
        if self.command == "$+":
            return input_value + self.get_option_val(context, input_value, result_set)
        if self.command == "$-":
            return input_value - self.get_option_val(context, input_value, result_set)
        if self.command == "$*":
            return input_value * self.get_option_val(context, input_value, result_set)
        if self.command == "$/":
            return input_value / self.get_option_val(context, input_value, result_set)
        if self.command == "$%":
            return input_value % self.get_option_val(context, input_value, result_set)
        if self.command == "$is":
            return input_value is self.get_option_val(context, input_value, result_set)
        if self.command == "$in":
            return input_value in self.get_option_val(context, input_value, result_set)
        if self.command == "$is_not":
            return input_value is not self.get_option_val(context, input_value, result_set)
        if self.command == "$==":
            return input_value == self.get_option_val(context, input_value, result_set)
        if self.command == "$!=":
            return input_value != self.get_option_val(context, input_value, result_set)
        if self.command == "$>":
            return input_value > self.get_option_val(context, input_value, result_set)
        if self.command == "$>=":
            return input_value >= self.get_option_val(context, input_value, result_set)
        if self.command == "$<":
            return input_value < self.get_option_val(context, input_value, result_set)
        if self.command == "$<=":
            return input_value <= self.get_option_val(context, input_value, result_set)

    @classmethod
    def get_task(cls, command: str, option):
        opt_task = parse_object(option)
        return OperatorTask(command, opt_task)

