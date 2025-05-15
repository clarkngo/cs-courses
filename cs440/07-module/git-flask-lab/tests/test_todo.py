import unittest
from app.todo import app

class TodoTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_add_and_list_task(self):
        self.client.post("/add", json={"id": "1", "description": "Test Task"})
        response = self.client.get("/list")
        self.assertIn("1", response.get_data(as_text=True))

if __name__ == "__main__":
    unittest.main()
