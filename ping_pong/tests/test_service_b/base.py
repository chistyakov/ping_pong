import unittest
from unittest.mock import patch

from service_b import app


class BaseServiceB(unittest.TestCase):
    def setUp(self) -> None:
        self.app = app
        self.patcher = patch("service_b.BackgroundTasks.add_task")
        self.mock_object = self.patcher.start()

    def tearDown(self) -> None:
        self.patcher.stop()
