"""
任务管理器
"""

from typing import List

from .task import Task


class TaskManager:

    def __init__(self):

        self.tasks: List[Task] = []

    def add(self, task: Task):

        self.tasks.append(task)

    def clear(self):

        self.tasks.clear()

    def run(self):

        for task in self.tasks:

            task.run()