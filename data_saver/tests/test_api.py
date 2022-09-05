"""
Tests for api.py
"""

from unittest import TestCase, mock
from data_saver import api


class ApiTestCase(TestCase):

    @mock.patch('data_saver.api.get_batch_sales_data')
    def test_api(self, get_batch_sales_data: mock.MagicMock):
        """
        Test with mocked service call
        """
        get_batch_sales_data.return_value = [{"client": "Bob Marley", "Profit": 12}]
        respond = api.get_sales("http://test_url", "test_token", "2022-01-01")

        self.assertEqual(type(respond), type([]))

        print('✅ API test Ok')
