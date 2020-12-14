import unittest

from starlette.testclient import TestClient

from service_a import app


class BaseServiceA(unittest.TestCase):
    def setUp(self) -> None:
        self.app = app
        self.client = TestClient(self.app)
