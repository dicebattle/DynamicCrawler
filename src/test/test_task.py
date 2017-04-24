from context.TestRuntimeContext import TestRuntimeContext
from task.task import Task

ctx = TestRuntimeContext()


class DummyTask(Task):
    def execute(ctx, self, input_value, result_set: dict):
        return input_value

    @classmethod
    def get_task(cls, command: str, option):
        return DummyTask(option)


def test_task():
    t = DummyTask.get_task("cmd", "option")
    assert isinstance(t, Task)
    assert t.execute(ctx, "input", {}) == "input"
    assert t.option_val == "option"
    assert t.get_option_val(None, "input", {}) == "option"

    tt = DummyTask.get_task("cmd2", t)
    assert tt.option_val is None
    assert tt.get_option_val(None, "input2", {}) == "input2"
