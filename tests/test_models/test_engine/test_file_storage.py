#!/usr/bin/python3
"""unnittests suites for file_storage.py"""

import os
import json
import pep8
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    """File Storage tests"""

    pass
