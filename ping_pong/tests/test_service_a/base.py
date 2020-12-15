import unittest
from unittest.mock import patch

from service_a.main import create_app


class BaseServiceA(unittest.TestCase):
    def setUp(self) -> None:
        self.app = create_app()
        self.patcher = patch("service_a.handler.BackgroundTasks.add_task")
        self.mock_object = self.patcher.start()

    def tearDown(self) -> None:
        self.patcher.stop()
