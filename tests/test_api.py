import unittest
from src.api.client import ClientConfig


class TestApiClient(unittest.TestCase):
    def test_client_config(self):
        base_url = "https://api.up.com.au"
        auth = {"type": "Bearer", "token": "Bearer token"}
        paginator = {"next": "next", "previous": "previous"}

        client_config = ClientConfig(base_url, auth, paginator)
        expected_dict = {
            "client": {"base_url": base_url, "auth": auth, "paginator": paginator}
        }
        self.assertEqual(client_config.to_dict(), expected_dict)


if __name__ == "__main__":
    unittest.main()
