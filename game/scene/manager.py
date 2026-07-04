from .home import HomeScene
from .world import WorldScene
from .unknown import UnknownScene


class SceneManager:

    def __init__(self, context):

        self.context = context

        self.current = None

        self.scenes = [

            HomeScene(context),

            WorldScene(context),

            UnknownScene(context)

        ]

    def detect(self):

        for scene in self.scenes:

            if scene.check():

                self.current = scene

                return scene

        return None

    def is_home(self):

        return self.detect().name == "Home"

    def is_world(self):

        return self.detect().name == "World"

    def current_name(self):

        scene = self.detect()

        return scene.name if scene else "Unknown"