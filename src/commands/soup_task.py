from bs4 import BeautifulSoup
from requests import Response

from context.abstract_context import RuntimeContext
from task.task import Task
from task.task_builder import parse_object


class SoupTask(Task):
    def __init__(self, command: str, option):
        super().__init__(option)
        self.command = command

    def execute(self, context: RuntimeContext, input_value, result_set: dict):
        html = self.get_option_val(context, input_value, result_set)

        if isinstance(html, Response):
            html = html.content

        return BeautifulSoup(html, "lxml")

    @classmethod
    def get_task(cls, command: str, option):
        opt_t = parse_object(option)
        return SoupTask(command, opt_t)
