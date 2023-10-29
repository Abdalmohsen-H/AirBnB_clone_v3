
from flask import app
import unittest
from web_flask import cisfun


class TestIndex(unittest.TestCase):

    # Returns 'Hello HBNB!' when accessing the root URL
    def test_returns_hello_hbnb(self):
        response = app.test_client().get('/')
        self.assertEqual(response.data.decode(), 'Hello HBNB!')

    # Returns a string with length between 1 and 1000 characters
    def test_returns_string_with_valid_length(self):
        response = app.test_client().get('/')
        self.assertGreater(len(response.data.decode()), 0)
        self.assertLess(len(response.data.decode()), 1001)

    # Returns an empty string when given invalid input
    def test_returns_empty_string_with_invalid_input(self):
        response = app.test_client().get('/')
        self.assertEqual(response.data.decode(), '')

    # Returns a 404 error when accessing a non-existent URL
    def test_returns_404_error_with_non_existent_URL(self):
        response = app.test_client().get('/nonexistent')
        self.assertEqual(response.status_code, 404)

    # Returns a string containing only ASCII characters
    def test_returns_string_with_only_ASCII_characters(self):
        response = app.test_client().get('/')
        self.assertTrue(all(ord(c) < 128 for c in response.data.decode()))

    # Returns a string containing only printable characters
    def test_returns_string_with_only_printable_characters(self):
        response = app.test_client().get('/')
        self.assertTrue(all(c.isprintable() for c in response.data.decode()))


class TestHbnb(unittest.TestCase):

    # The function returns 'HBNB' when the route '/hbnb' is accessed.
    def test_returns_hbnb(self):
        with app.test_client() as client:
            response = client.get('/hbnb')
            self.assertEqual(response.data.decode(), 'HBNB')

    # The function handles requests with trailing slashes.
    def test_handles_trailing_slashes(self):
        with app.test_client() as client:
            response = client.get('/hbnb/')
            self.assertEqual(response.data.decode(), 'HBNB')

    # The function handles requests with parameters.
    def test_handles_parameters(self):
        with app.test_client() as client:
            response = client.get('/hbnb?param=test')
            self.assertEqual(response.data.decode(), 'HBNB')


class TestCisfun(unittest.TestCase):

    # Returns a string starting with 'C '
    # followed by the value of the text variable
    # with underscores replaced by spaces.
    def test_returns_string_with_replaced_underscores(self):
        result = cisfun('hello_world')
        self.assertEqual(result, 'C hello world')

    # Handles text variable with no underscores.
    def test_handles_text_variable_with_no_underscores(self):
        result = cisfun('hello')
        self.assertEqual(result, 'C hello')
