"""
Tests for store.py
"""
import os
import json

from unittest import TestCase
from data_saver import store


class ApiTestCase(TestCase):

    def test_data_saving(self):
        """
        Test with test json data and test path
        """
        test_list = [{"key1": "value1"}, {"key2": "value2"}]
        test_path = "test_dir"

        respond = store.save_local(path=test_path, data=test_list)

        with open(f"{test_path}/data.json", "r") as file:
            data_from_file = json.load(file)

        os.remove(f"{test_path}/data.json")
        os.rmdir(test_path)

        self.assertEqual(test_list, data_from_file)

        print(f"✅ store.save_local test Ok: {respond}")
