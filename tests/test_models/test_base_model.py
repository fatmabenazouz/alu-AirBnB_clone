#!/usr/bin/python3
"""Test BaseModel"""

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """test BaseModel"""

    def test_save_BaseModel(self):
        """test save_Basemodel"""
        base = BaseModel()
        self.assertEqual(base.created_at, base.updated_at)

    def test_doc(self):
        """ Tests doc """
        self.assertIsNotNone(BaseModel.__doc__)

    def test_to_json(self):
    """Test the to_json method"""
    base = BaseModel()
    base_json = base.to_json()

    self.assertIsInstance(base_json, dict)

    self.assertIn("id", base_json)
    self.assertIn("created_at", base_json)
    self.assertIn("updated_at", base_json)
    self.assertIn("__class__", base_json)
    self.assertEqual(base.id, base_json["id"])
    self.assertEqual("BaseModel", base_json["__class__"])

    def test_kwarg(self):
        basemodel = BaseModel()
        self.assertEqual(basemodel.__class__.__name__, "BaseModel")
        self.assertTrue(hasattr(basemodel, "id"))
        self.assertTrue(hasattr(basemodel, "created_at"))
        self.assertTrue(hasattr(basemodel, "updated_at"))
        self.assertTrue(hasattr(basemodel, "__class__"))


if __name__ == "__main__":
    unittest.main()
