from celery import Celery
import yaml
from task.task import Task
from task.task_builder import parse_object
from context.CeleryRuntimeContext import CeleryRuntimeContext

celeryInstance = Celery('tasks',
                        backend='redis://localhost:6379/0',
                        broker='redis://localhost:6379/0')

@celeryInstance.task
def crawling(yamlString, res_set):
    context = CeleryRuntimeContext()
    task_source = yaml.load(yamlString)
    task = parse_object(task_source)
    task.execute(context, "", res_set)
    return res_set