from context.TestRuntimeContext import TestRuntimeContext
from task.task import Task
from task.task_array import TaskArray


class DummyConcatTask(Task):
    def execute(self, context, input_value, result_set: dict):
        return input_value + " " + self.get_option_val(TestRuntimeContext(), input, result_set)


def test_task_array():
    ta = TaskArray([
        DummyConcatTask("everybody"),
        DummyConcatTask("nice"),
        DummyConcatTask("to"),
        DummyConcatTask("meet"),
        DummyConcatTask("you!"),
    ])

    assert ta.execute(TestRuntimeContext(), "Hello", {}) == "Hello everybody nice to meet you!"
