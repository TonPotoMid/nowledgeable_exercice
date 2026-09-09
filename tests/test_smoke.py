import unittest

from app import app


class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_health_endpoint(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"status": "ok"})

    def test_items_endpoint(self):
        response = self.client.get("/api/items")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("items", data)
        self.assertIsInstance(data["items"], list)


if __name__ == "__main__":
    unittest.main()
