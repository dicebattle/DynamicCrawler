from numbers import Number

from commands import CommonTask
from commands.get_result_task import GetResultTask
from context.TestRuntimeContext import TestRuntimeContext
from task.task import Task
from task.task_array import TaskArray
from task.task_builder import parse_object

ctx = TestRuntimeContext()


def test_task_builder():
    assert isinstance(parse_object("hello"), str)
    assert isinstance(parse_object("$as"), Task) and not isinstance(parse_object("$as"), GetResultTask)
    assert isinstance(parse_object("$$res"), GetResultTask)

    assert isinstance(parse_object(3), Number)
    assert isinstance(parse_object(3.5), Number)

    t = parse_object({"$as": "abc"})
    assert isinstance(t, CommonTask)

    t = parse_object({"$command": "$as", "$use": "abc"})
    assert isinstance(t, CommonTask)
    assert t.command == "$as"
    assert isinstance(t.option, CommonTask)
    assert t.option.command == "$use"
    assert t.get_option_val(ctx, "", {}) == "abc"

    ta = parse_object(["a", "b", "c", "d"])
    assert isinstance(ta, TaskArray)
    assert ta.execute(ctx, "", {}) == "d"

    t = parse_object(["$use", "aaa", "bbb"])

    assert not isinstance(t, TaskArray)
    assert isinstance(t, CommonTask)
    assert isinstance(t.option, TaskArray)
    assert t.get_option_val(ctx, "", {}) == "bbb"
    assert t.execute(ctx, "", {}) == "bbb"
