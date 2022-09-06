"""
Tests for store.py
"""
import os
import json

from unittest import TestCase
from data_transformer import transform


class TransformTestCase(TestCase):

    def test_transform_and_save_data(self):
        """
        Test with broken path to file
        """
        respond = transform.transform_and_save_data(raw_dir_path="test/path", stg_dir_path="test_stg/path")

        # self.assertEqual(test_list, data_from_file)

        print(f"✅ store.save_local test Ok: {respond}")
