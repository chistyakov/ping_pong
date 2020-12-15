from starlette.testclient import TestClient

from test_service_b.base import BaseServiceB


class TestPong(BaseServiceB):
    def test_empty_list(self):
        with TestClient(self.app) as client:
            response = client.post("/pong", json={"digits": []})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(), {"digits": [], "avg": None, "min": None, "max": None}
        )

    def test_single_item(self):
        with TestClient(self.app) as client:
            response = client.post("/pong", json={"digits": [42]})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(), {"digits": [42], "avg": 42, "min": 42, "max": 42}
        )

    def test_two_items(self):
        with TestClient(self.app) as client:
            response = client.post("/pong", json={"digits": [2, 1]})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(), {"digits": [2, 1], "avg": 1.5, "min": 1, "max": 2}
        )

    def test_three_items(self):
        with TestClient(self.app) as client:
            response = client.post("/pong", json={"digits": [2, 1, 2]})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {"digits": [2, 1, 2], "avg": 1.6666666666666667, "min": 1, "max": 2},
        )

    def test_missing_list(self):
        with TestClient(self.app) as client:
            response = client.post("/pong", json={})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(), {"digits": [], "avg": None, "min": None, "max": None}
        )

    def test_invalid_not_list(self):
        with TestClient(self.app) as client:
            response = client.post("/pong", json={"digits": "foo"})
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
            response = client.post("/pong", json={"digits": [1, "a"]})
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
            response = client.post("/pong", json={"digits": [101]})
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
