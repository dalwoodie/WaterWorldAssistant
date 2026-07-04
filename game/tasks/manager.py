from typing import List

from core.logger.logger import logger

from .base import BaseTask


class TaskManager:

    def __init__(self):

        self.tasks: List[BaseTask] = []

    def add(self, task: BaseTask):

        logger.info(f"添加任务：{task.name}")

        self.tasks.append(task)

    def clear(self):

        self.tasks.clear()

    def run(self):

        logger.info("开始执行任务")

        for task in self.tasks:

            logger.info(f"执行任务：{task.name}")

            try:

                task.run()

                logger.info(f"完成任务：{task.name}")

            except Exception as e:

                logger.exception(
                    f"任务失败：{task.name}\n{e}"
                )

                break

        logger.info("任务执行结束")