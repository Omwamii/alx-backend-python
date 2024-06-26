#!/usr/bin/env python3
""" Module with unit tests
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)


class TestAccessNestedMap(unittest.TestCase):
    """ Test the utils.access_nested_map method
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence,
                               result: Any):
        """ Test method """
        self.assertEqual(access_nested_map(nested_map, path), result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")
         )])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence):
        """ Test exception in access_nested_map """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ Test the get_json function """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_requests):
        """ Test for get_json """
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_requests.return_value = mock_response
        self.assertEqual(get_json(test_url), test_payload)


class TestMemoize(unittest.TestCase):
    """ Test memoization fn """
    def test_memoize(self):
        """ Test for memoize, ensure that when a_property is called twice
            a_method is only called once
        """
        class TestClass:
            """ Test class to wrap memoize """
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock:
            test_class = TestClass()
            test_class.a_property()
            test_class.a_property()
            mock.assert_called_once()


if __name__ == "__main__":
    unittest.main()
