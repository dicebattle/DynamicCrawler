from commands.bs_find_task import BSFindTask
from commands.bs_select_task import BSSelectTask
from commands.common_task import CommonTask
from commands.http_task import HttpTask
from commands.soup_task import SoupTask
from task.task_array import TaskArray

__COMMAND_PRIORITY = [
    "$use",
    "$use_list",
    "$as",

    "$http",
    "$soup"

    "$find",
    "$find_all",
    "$find_parent",
    "$find_parents",
    "$find_next_siblings",
    "$find_next_sibling",
    "$find_previous_siblings",
    "$find_previous_sibling",
    "$find_all_next",
    "$find_next",
    "$find_all_previous",
    "$find_previous",
    "$select",
    "$select_one",
]

__COMMAND_PRIORITY_DICT = dict(map(lambda x: (x[1], x[0]), enumerate(__COMMAND_PRIORITY)))
__COMMAND_PRIORITY_DICT["as"] = 999999999999999999


__TASK_GENERATOR = {
    "$use": CommonTask.get_task,
    "$use_list": CommonTask.get_task,
    "$as": CommonTask.get_task,

    "$http": HttpTask.get_task,
    "$soup": SoupTask.get_task,

    "$find": BSFindTask.get_task,
    "$find_all": BSFindTask.get_task,
    "$find_parent": BSFindTask.get_task,
    "$find_parents": BSFindTask.get_task,
    "$find_next_siblings": BSFindTask.get_task,
    "$find_next_sibling": BSFindTask.get_task,
    "$find_previous_siblings": BSFindTask.get_task,
    "$find_previous_sibling": BSFindTask.get_task,
    "$find_all_next": BSFindTask.get_task,
    "$find_next": BSFindTask.get_task,
    "$find_all_preivous": BSFindTask.get_task,
    "$find_previous": BSFindTask.get_task,
    "$select": BSSelectTask.get_task,
    "$select_one": BSSelectTask.get_task,
}


def extract_commands_from_dict(value: dict):
    if value.get("$command"):  # defence code.
        raise Exception("Invalidated command : $command. It should had filtered in parse_dict.")

    non_command_opt = dict(filter(lambda kv: not kv[0].startswith("$"), value.items()))
    command_list = list(filter(lambda kv: kv[0].startswith("$"), value))
    if sum(1 for x in command_list if x not in __COMMAND_PRIORITY) > 0:
        raise Exception("not supported command. : " + str(command_list))

    command_list = list(sorted(command_list, key=lambda x: __COMMAND_PRIORITY_DICT[x]))
    if len(command_list) == 0:
        return non_command_opt  # implicit literal dict

    command_list = list(map(lambda cmd: __TASK_GENERATOR[cmd](cmd, value[cmd]), command_list))
    if len(command_list) == 1:
        return command_list[0]
    else:
        return TaskArray(command_list)


def get_command_task(command: str, option):
    task_gen = __TASK_GENERATOR.get(command)
    if not task_gen:
        raise Exception("not supported command. " + command)
    return task_gen(command, option)
