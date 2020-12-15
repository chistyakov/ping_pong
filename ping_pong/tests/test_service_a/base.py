import unittest
from unittest.mock import patch

from service_a import app


class BaseServiceA(unittest.TestCase):
    def setUp(self) -> None:
        self.app = app
        self.patcher = patch("service_a.BackgroundTasks.add_task")
        self.mock_object = self.patcher.start()

    def tearDown(self) -> None:
        self.patcher.stop()
