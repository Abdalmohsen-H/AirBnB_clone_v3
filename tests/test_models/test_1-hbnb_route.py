#!/usr/bin/python3
"""
TEST
"""
from flask import app
import unittest

class TestIndex(unittest.TestCase):
    """
    """
    # Returns 'Hello HBNB!' when accessing the root URL
    def test_returns_hello_hbnb(self):
        response = app.test_client().get('/')
        self.assertEqual(response.data.decode(), 'Hello HBNB!')


class TestHbnb(unittest.TestCase):
    """
    """

    # Returns 'HBNB' when accessing the '/hbnb' route
    def test_returns_hbnb(self):
        with app.test_client() as client:
            response = client.get('/hbnb')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data.decode(), 'HBNB')

    # No edge cases identified
    def test_no_edge_cases(self):
        pass

    # Function returns a 404 error when accessing a different route
    def test_returns_404_error(self):
        with app.test_client() as client:
            response = client.get('/random')
            self.assertEqual(response.status_code, 404)