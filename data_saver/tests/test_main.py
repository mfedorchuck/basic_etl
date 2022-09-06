"""
Tests for data_saver/main.py
"""

from unittest import TestCase, mock
import data_saver.main as main


class MainTestCase(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        main.app.testing = True
        cls.client = main.app.test_client()

    def test_return_400_date_param_missed_path_param_missed(self):
        """
        Raise 400 HTTP code when no 'date' param
        """
        json_params = {
            'raw_dir': '/foo/bar/',
            # no 'date' set
        }
        resp = self.client.post('/', json=json_params)

        self.assertEqual(400, resp.status_code)
        print(f"✅ Raise 400 HTTP code when no 'date' param: Respond: {resp.text}\n")

    @mock.patch('data_saver.main.store.save_local')
    @mock.patch('data_saver.main.api.get_sales')
    def test_return_respond_with_mocked_functions(self, get_sales_mock: mock.MagicMock, save_to_disk: mock.MagicMock):
        """
        Return 201 HTTP code with isolated functions
        """

        get_sales_mock.return_value = [{"client_name": "Ghost", "gross_usd": 100500}]
        save_to_disk.return_value = "I'm fine, Thank You!"

        json_params = {
            'raw_dir': 'foo/bar/',
            'date': "2022-08-09",
        }
        resp = self.client.post('/', json=json_params)

        print("resp.status_code: ", resp.status_code)

        self.assertEqual(201, resp.status_code)
        print("✅ Returned 201 HTTP code with mocked save_local AND get_sales functions")
