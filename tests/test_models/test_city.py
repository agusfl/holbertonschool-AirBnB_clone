#!/usr/bin/python
"""
test Class City
"""


import unittest
from models.base_model import BaseModel
import models
from models.city import City


class TestCity(unittest.TestCase):
    """
    Test City
    """

    def test_documentation(self):
        """
        check if class has documentation
        """
        self.assertIsNotNone(City.__doc__)

    def test_class(self):
        """
        test class & test subclass
        """
        self.assertEqual(City.name, "")
        self.assertEqual(City.state_id, "")
        self.assertTrue(issubclass(City, BaseModel))

    def test_instance(self):
        """
        test instance of City
        """
        test = City()
        self.assertEqual(test.state_id, "")
        self.assertEqual(test.name, "")
        self.assertTrue(issubclass(City, BaseModel))

    def test_attributetype(self):
        """
        test attribute test
        """
        test = City()
        self.assertEqual(type(test.name), str)
        self.assertEqual(type(test.state_id), str)


if __name__ == "__main__":
    unittest.main()
