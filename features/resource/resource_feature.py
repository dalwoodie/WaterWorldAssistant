"""
资源模块

负责：

资源读取

资源统计

资源优先级判断
"""

from features.base import BaseFeature

from .resource_type import ResourceType


class ResourceFeature(BaseFeature):

    @property
    def name(self):

        return "Resource"

    def run(self):

        self.log("Resource Feature Running...")

    def get_priority(
        self,
        resource: ResourceType
    ) -> int:
        """
        返回资源优先级。

        数值越大，优先级越高。
        """

        priorities = {

            ResourceType.GOLD: 100,

            ResourceType.IRON: 90,

            ResourceType.WATER: 80,

            ResourceType.WOOD: 70,

            ResourceType.FOOD: 60

        }

        return priorities.get(
            resource,
            0
        )