#!/usr/bin/python3
"""Defines unittests for console.py."""
import os
import pep8
import unittest
import models
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.engine.file_storage import FileStorage


class TestHBNBCommand(unittest.TestCase):
    """suite of test for the console"""

    def setUp(self):
        """set the up the test"""
        pass

    def tearDown(self):
        """end the test"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_pep8(self):
        """Test Pep8 styling."""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["console.py"])
        self.assertEqual(p.total_errors, 0, "fix Pep8")

    def test_docstrings(self):
        """Check for docstrings."""
        self.assertIsNotNone(HBNBCommand.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.default.__doc__)

    def test_create_kwargs(self):
        """Test create command with kwargs."""

        self.HBNB = HBNBCommand()
        with patch("sys.stdout", new=StringIO()) as f:
            call = ('create Place city_id="0001" name="My_house" '
                    'number_rooms=4 latitude=37.77 longitude=a')
            self.HBNB.onecmd(call)
            pl = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all Place")
            output = f.getvalue()
            self.assertIn(pl, output)
            self.assertIn("'city_id': '0001'", output)
            self.assertIn("'name': 'My house'", output)
            self.assertIn("'number_rooms': 4", output)
            self.assertIn("'latitude': 37.77", output)
            self.assertNotIn("'longitude'", output)

    def test_input_double_quote_escaping(self):
        """test input format"""

        self.HBNB = HBNBCommand()
        with patch("sys.stdout", new=StringIO()) as f:
            input = ('create City name="here_dd" number="3"')
            self.HBNB.onecmd(input)
            out = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all City")
            output = f.getvalue()
            self.assertIn(out, output)
            self.assertIn("'name': 'here dd'", output)
            self.assertIn("'number': 3", output)

    def test_decimal(self):
        """[test_decimal]
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create User number_bathrooms=4')
            HBNBCommand().onecmd('all User')
        msg = f.getvalue()[:-1]
        self.assertTrue("'number_bathrooms': 4" in msg)

    def test_float(self):
        """[test_float]
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create User price=0.069')
            HBNBCommand().onecmd('all User')
        msg = f.getvalue()[:-1]
        self.assertTrue("'price': 0.069" in msg)

if __name__ == "__main__":
    unittest.main()
