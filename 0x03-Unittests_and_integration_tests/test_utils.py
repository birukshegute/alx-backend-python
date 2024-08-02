#!/usr/bin/env python3
"""
Unit test for utils.py
"""

import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock, MagicMock
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """ Test class for TestAccessNestedMap """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ tests with valid inputs """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Tests for exceptions """
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception), repr(path[-1]))


class TestGetJson(unittest.TestCase):
    """Test class for GetJson Function"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """ function for the test"""
        with patch('utils.requests.get') as mocked_get:
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mocked_get.return_value = mock_response

            result = get_json(test_url)
            self.assertEqual(result, test_payload)

            mocked_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """ Test class for Memoize function"""

    def test_memoize(self):
        """ function for the test"""
        class TestClass:
            """ Test case class"""
            def a_method(self):
                """function call"""
                return 42

            @memoize
            def a_property(self):
                """Testing the cache"""
                return self.a_method()

        with patch.object(TestClass, 'a_method',
                          return_value=42) as mock_method:
            instance = TestClass()
            self.assertEqual(instance.a_property, 42)
            self.assertEqual(instance.a_property, 42)
            mock_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
