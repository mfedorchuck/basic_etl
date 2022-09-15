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

        with self.assertRaises(Exception) as context:
            transform.transform_and_save_data(raw_dir_path="test/path", stg_dir_path="test_stg/path")
