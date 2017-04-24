from context.abstract_context import RuntimeContext
from task.task import Task
from task.task_builder import parse_object


class GetTask(Task):
    def __init__(self, command: str, option):
        super().__init__(option)
        self.command = command

    def execute(self, context: RuntimeContext, input_value, result_set: dict):
        opt = self.option_val

        if opt is None:
            opt = self.option

        if isinstance(opt, int) or isinstance(opt, str):
            return self.get_by_number_or_string(input_value, opt)
        if isinstance(opt, list):
            return self.get_by_list(input_value, opt)
        if isinstance(opt, dict):
            return self.get_by_dict(input_value, opt)
        if isinstance(opt, Task):
            return self.get_by_task(context, input_value, opt, result_set)

        raise Exception("invalidated option value. unknown type : ." + str(type(opt)))

    @staticmethod
    def get_by_number_or_string(inp: list, opt):
        return inp[opt]

    @staticmethod
    def get_by_list(inp: list, opt: list):
        return list(map(lambda x: inp[x], opt))

    @staticmethod
    def get_by_dict(inp: list, opt: dict):
        from_ = opt.get("from", 0)
        until = opt.get("until", len(inp))
        step = opt.get("step", 1)
        return inp[from_:until:step]

    @staticmethod
    def get_by_task(context: RuntimeContext, inp: list, opt: Task, result_set):
        for i in inp:
            if opt.execute(context, i, result_set):
                return i
        return None

    @classmethod
    def get_task(cls, command: str, option):
        opt_task = parse_object(option)
        return GetTask(command, opt_task)
