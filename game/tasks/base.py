from abc import ABC, abstractmethod


class BaseTask(ABC):

    name = "BaseTask"

    def __init__(self, context):

        self.context = context

        self.logger = context.logger

    @abstractmethod
    def run(self):

        pass