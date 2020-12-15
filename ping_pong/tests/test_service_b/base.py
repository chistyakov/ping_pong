import unittest
from unittest.mock import patch

from service_b.main import create_app


class BaseServiceB(unittest.TestCase):
    def setUp(self) -> None:
        self.app = create_app()
        self.patcher = patch("service_b.handler.BackgroundTasks.add_task")
        self.mock_object = self.patcher.start()

    def tearDown(self) -> None:
        self.patcher.stop()
