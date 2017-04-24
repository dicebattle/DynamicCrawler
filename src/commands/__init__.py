from commands.and_or_task import AndTask
from commands.and_or_task import OrTask
from commands.bs_find_task import BSFindTask
from commands.bs_select_task import BSSelectTask
from commands.common_task import CommonTask
from commands.concat_string_task import ConcatStringTask
from commands.drop_task import DropTask
from commands.filter_task import FilterTask
from commands.get_attr_task import GetAttrTask
from commands.get_task import GetTask
from commands.http_task import HttpTask
from commands.map_task import MapTask
from commands.mk_string_task import MkStringTask
from commands.operator_task import OperatorTask
from commands.replace_string_task import ReplaceStringTask
from commands.soup_task import SoupTask
from commands.union_task import UnionTask
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

    "$filter",
    "$filter_not",
    "$get",
    "$map",
    "$flat_map",
    "$union",
    "$drop",

    "$or",
    "$and",

    "$+",
    "$/",
    "$-",
    "$*",
    "$%",
    "$is",
    "$in",
    "$is_not",
    "$==",
    "$!=",
    "$>",
    "$>=",
    "$<",
    "$<=",

    "$concat",
    "$mk_string",
    "$replace",
    "$replace_once",

    "$get_attr",
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

    "$filter": FilterTask.get_task,
    "$filter_not": FilterTask.get_task,
    "$get": GetTask.get_task,
    "$map": MapTask.get_task,
    "$flat_map": MapTask.get_task,
    "$union": UnionTask.get_task,
    "$drop": DropTask.get_task,

    "$or": OrTask.get_task,
    "$and": AndTask.get_task,

    "$+": OperatorTask.get_task,
    "$/": OperatorTask.get_task,
    "$-": OperatorTask.get_task,
    "$*": OperatorTask.get_task,
    "$%": OperatorTask.get_task,
    "$is": OperatorTask.get_task,
    "$in": OperatorTask.get_task,
    "$is_not": OperatorTask.get_task,
    "$==": OperatorTask.get_task,
    "$!=": OperatorTask.get_task,
    "$>": OperatorTask.get_task,
    "$>=": OperatorTask.get_task,
    "$<": OperatorTask.get_task,
    "$<=": OperatorTask.get_task,

    "$concat": ConcatStringTask.get_task,
    "$mk_string": MkStringTask.get_task,
    "$replace": ReplaceStringTask.get_task,
    "$replace_once": ReplaceStringTask.get_task,

    "$get_attr": GetAttrTask.get_task,
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
