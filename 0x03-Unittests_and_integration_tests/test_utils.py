#!/usr/bin/env python3
""" Module with unit tests
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)


class TestAccessNestedMap(unittest.TestCase):
    ''' Test the utils.access_nested_map method
    '''
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence, result: Any):
        ''' Test method '''
        self.assertEqual(access_nested_map(nested_map, path), result)


if __name__ == "__main__":
    unittest.main()
