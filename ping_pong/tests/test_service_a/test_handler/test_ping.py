from starlette.testclient import TestClient

from base import anything
from test_service_a.base import BaseServiceA


class TestPing(BaseServiceA):
    def test_ping_empty_list(self):
        with TestClient(self.app) as client:
            response = client.post("/ping", json={"digits": []})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"digits": [anything]})


class TestPingValidation(BaseServiceA):
    def test_missing_list(self):
        with TestClient(self.app) as client:
            response = client.post("/ping", json={})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"digits": [anything]})

    def test_invalid_not_list(self):
        with TestClient(self.app) as client:
            response = client.post("/ping", json={"digits": 1})
        self.assertEqual(response.status_code, 422)
        self.assertEqual(
            response.json(),
            {
                "detail": [
                    {
                        "loc": ["body", "digits"],
                        "msg": "value is not a valid list",
                        "type": "type_error.list",
                    }
                ]
            },
        )

    def test_invalid_not_int(self):
        with TestClient(self.app) as client:
            response = client.post("/ping", json={"digits": [1, "a"]})
        self.assertEqual(response.status_code, 422)
        self.assertEqual(
            response.json(),
            {
                "detail": [
                    {
                        "loc": ["body", "digits", 1],
                        "msg": "value is not a valid integer",
                        "type": "type_error.integer",
                    }
                ]
            },
        )

    def test_invalid_not_in_range(self):
        with TestClient(self.app) as client:
            response = client.post("/ping", json={"digits": [101]})
        self.assertEqual(response.status_code, 422)
        self.assertEqual(
            response.json(),
            {
                "detail": [
                    {
                        "loc": ["body", "digits", 0],
                        "msg": "101 not in range (0, 100)",
                        "type": "assertion_error",
                    }
                ]
            },
        )
