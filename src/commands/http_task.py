from urllib.parse import urljoin

import requests

from context.abstract_context import RuntimeContext
from task.task import Task
from task.task_builder import parse_object


class HttpTask(Task):
    def __init__(self, url_t, method, header_t, cookie_t, body_t, join_url_t):
        super().__init__(None)
        self.body_t = body_t
        self.method = method
        self.header_t = header_t
        self.url_t = url_t
        self.cookie_t = cookie_t
        self.join_url_t = join_url_t

    def execute(self, context: RuntimeContext, input_value, result_set: dict):
        url = self.url_t
        if isinstance(url, Task):
            url = url.execute(context, input_value, result_set)

        method = self.method
        headers = self.header_t
        if isinstance(headers, Task):
            headers = headers.execute(context, input_value, result_set)

        cookies = self.cookie_t
        if isinstance(cookies, Task):
            cookies.execute(context, input_value, result_set)

        body = self.body_t
        if isinstance(body, Task):
            body = body.execute(context, input_value, result_set)

        join_url = self.join_url_t
        if isinstance(join_url, Task):
            join_url = join_url.execute(context, input_value, result_set)

        if join_url:
            url = urljoin(join_url,url)

        if method == "get":
            return requests.get(url, headers=headers, cookies=cookies)
        else:
            return requests.post(url, data=body, headers=headers, cookies=cookies)

    @classmethod
    def get_task(cls, command: str, option):
        url_t = parse_object(option.get("$url", "$url"))
        header_t = parse_object(option.get("$header", None))
        method = option.get("$method", "get")
        body_t = parse_object(option.get("$body", None))
        cookie_t = parse_object(option.get("$cookie", None))
        join_url_t = parse_object(option.get("$join_with", None))
        return HttpTask(url_t, method, header_t, cookie_t, body_t, join_url_t)
