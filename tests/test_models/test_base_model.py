#!/usr/bin/python3
"""unnittests suite for models/base_model.py."""

import pep8
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Unittests for testing the BaseModel class."""

    def test_pep8(self):
        """Test pep8 styling."""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["models/base_model.py"])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_docstrings(self):
        """Check for docstrings."""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)


if __name__ == "__main__":
    unittest.main()
