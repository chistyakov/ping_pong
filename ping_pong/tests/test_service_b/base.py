import unittest

from starlette.testclient import TestClient

from service_b import app


class BaseServiceB(unittest.TestCase):
    def setUp(self) -> None:
        self.app = app
        self.client = TestClient(self.app)
