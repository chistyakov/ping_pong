from test_service_a.base import BaseServiceA


class TestPing(BaseServiceA):
    def test_ping(self):

        response = self.client.post("/ping", json={"digits": []})
        self.assertEqual(response.json(), {"digits": []})
