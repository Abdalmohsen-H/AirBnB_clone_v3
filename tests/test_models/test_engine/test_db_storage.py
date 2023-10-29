#!/usr/bin/python3
"""
Contains the TestDBStorageDocs and TestDBStorage classes
"""

from datetime import datetime
import inspect
import models
from models.engine import db_storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json
import os
import pep8
import unittest
DBStorage = db_storage.DBStorage
classes = {"Amenity": Amenity, "City": City, "Place": Place,
           "Review": Review, "State": State, "User": User}


class TestDBStorageDocs(unittest.TestCase):
    """Tests to check the documentation and style of DBStorage class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.dbs_f = inspect.getmembers(DBStorage, inspect.isfunction)

    def test_pep8_conformance_db_storage(self):
        """Test that models/engine/db_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_db_storage(self):
        """Test tests/test_models/test_db_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_engine/\
test_db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_db_storage_module_docstring(self):
        """Test for the db_storage.py module docstring"""
        self.assertIsNot(db_storage.__doc__, None,
                         "db_storage.py needs a docstring")
        self.assertTrue(len(db_storage.__doc__) >= 1,
                        "db_storage.py needs a docstring")

    def test_db_storage_class_docstring(self):
        """Test for the DBStorage class docstring"""
        self.assertIsNot(DBStorage.__doc__, None,
                         "DBStorage class needs a docstring")
        self.assertTrue(len(DBStorage.__doc__) >= 1,
                        "DBStorage class needs a docstring")

    def test_dbs_func_docstrings(self):
        """Test for the presence of docstrings in DBStorage methods"""
        for func in self.dbs_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""
    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_all_returns_dict(self):
        """Test that all returns a dictionaty"""
        self.assertIs(type(models.storage.all()), dict)

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_all_no_class(self):
        """Test that all returns all rows when no class is passed"""

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_new(self):
        """test that new adds an object to the database"""

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_save(self):
        """Test that save properly saves objects to file.json"""

    @unittest.skipIf(models.storage_t != 'file', "don't test file storage")
    def test_get(self):
        """Test get method that added on task 2 in storage engine classes"""
        get_res = storage.get(None, None)
        self.assertIsNone(get_res)

    @unittest.skipIf(models.storage_t != 'file', "don't test file storage")
    def test_count(self):
        """Test count method that added on task 2 in storage engine classes"""
        count_res = storage.count()
        self.assertIsNotNone(count_res)
class TestDBStorage(unittest.TestCase):

    # DBStorage object can be instantiated successfully
    def test_instantiation_success(self):
        db_storage = DBStorage()
        self.assertIsInstance(db_storage, DBStorage)

    # all() method returns a dictionary of all objects in the database
    def test_all_method_returns_dictionary(self, mocker):
        db_storage = DBStorage()
        with mocker.patch('models.engine.db_storage.DBStorage.__session') as mock_session:
            mock_session.query.return_value.all.return_value = [Amenity(), City(), Place()]
            result = db_storage.all()
            self.assertIsInstance(result, dict)
            self.assertEqual(len(result), 3)

    # new() method adds an object to the current database session
    def test_new_method_adds_object(self, mocker):
        db_storage = DBStorage()
        obj = Amenity()
        with mocker.patch('models.engine.db_storage.DBStorage.__session') as mock_session:
            db_storage.new(obj)
            mock_session.add.assert_called_once_with(obj)

    # all() method returns an empty dictionary when there are no objects in the database
    def test_all_method_returns_empty_dictionary(self, mocker):
        db_storage = DBStorage()
        with mocker.patch('models.engine.db_storage.DBStorage.__session') as mock_session:
            mock_session.query.return_value.all.return_value = []
            result = db_storage.all()
            self.assertIsInstance(result, dict)
            self.assertEqual(len(result), 0)

    # new() method raises an exception when the object is None
    def test_new_method_raises_exception_when_object_is_none(self, mocker):
        db_storage = DBStorage()
        with self.assertRaises(Exception):
            db_storage.new(None)

    # delete() method does not raise an exception when the object is None
    def test_delete_method_does_not_raise_exception_when_object_is_none(self, mocker):
        db_storage = DBStorage()
        with self.assertRaises(Exception):
            db_storage.delete(None)