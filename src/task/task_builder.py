import numbers

from task.task import Task
from task.task_array import TaskArray


def parse_object(value):
    if isinstance(value, str):
        return parse_string(value)
    if isinstance(value, numbers.Number):
        return parse_number(value)
    if isinstance(value, list):
        return parse_list(value)
    if isinstance(value, dict):
        return parse_dict(value)
    if isinstance(value, Task):
        return value
    if value is None:
        return None


def parse_dict(dict_val: dict):
    import src.commands as cmd
    if dict_val.get("$command"):
        dt = dict_val.copy()
        del dt["$command"]
        return cmd.get_command_task(dict_val["$command"], dt)  # _축약형 task
    return cmd.extract_commands_from_dict(dict_val)


def parse_list(list_val):
    import src.commands as cmd
    if len(list_val) == 0:
        return None
    if isinstance(list_val[0], str) and list_val[0].startswith("$"):
        return cmd.get_command_task(list_val[0], list_val[1:])
    return TaskArray.get_task("", list_val)


def parse_string(str_val: str):
    import src.commands as cmd
    if str_val.startswith("$$"):
        from commands.get_result_task import GetResultTask
        return GetResultTask.get_task(str_val, None)
    elif str_val.startswith("$"):
        return cmd.get_command_task(str_val, None)
    else:
        return str_val


def parse_number(num_val):
    return num_val
