from context.TestRuntimeContext import TestRuntimeContext
from task.task import Task
from task.task_builder import parse_object
import yaml

ctx = TestRuntimeContext()

class DummyTask(Task):
    def execute(ctx, self, input_value, result_set: dict):
        return input_value

    @classmethod
    def get_task(cls, command: str, option):
        return DummyTask(option)


def test_task():
    url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=news&oquery=%ED%85%8C%EC%8A%A4%ED%8A%B8&ie=utf8&query=%EB%AC%B8%EC%9E%AC%EC%9D%B8"
    res_set = {
        "inp_url": url
    }
    context = TestRuntimeContext()
    task_source = None
    with open("../../test.yaml", 'r') as stream:
        try:
            task_source = yaml.load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    print(task_source)
    task = parse_object(task_source)
    task.execute(context, "", res_set)
    print(res_set)
