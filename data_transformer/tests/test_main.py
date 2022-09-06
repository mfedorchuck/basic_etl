"""
Tests for data_transformer/main.py
"""

from unittest import TestCase, mock
import data_transformer.main as main


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

    @mock.patch('data_transformer.transform.transform_and_save_data')
    def test_return_respond_with_mocked_functions(self, transform_and_save_data: mock.MagicMock):
        """
        Return 201 HTTP code with isolated functions
        """

        transform_and_save_data.return_value = "Test data transformed successfully"
        json_params = {
            'raw_dir': 'foo/bar/',
            'stg_dir': 'foo/bar/',
        }
        resp = self.client.post('/', json=json_params)

        print()

        self.assertEqual(201, resp.status_code)
        print("✅ Returned 201 HTTP code. Respond status_code: ", resp.status_code)
