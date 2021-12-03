from modules.Checker import Checker
from unittest.mock import Mock
import unittest
from datetime import datetime

class Test_Checker(unittest.TestCase):
	def setUp(self):
		self.checker = Checker()

	def test_remainder_after_17(self):
		self.checker.os.getTime = Mock(name = "getTime")
		self.checker.os.getTime.return_value = datetime(2017, 11, 28, 23, 55, 59, 342380)
		# warning: this will seriously play the file!
		self.assertTrue(self.checker.remainder())
		
	def test_remainder_before_17(self):
		self.checker.os.getTime = Mock(name = "getTime")
		self.checker.os.getTime.return_value = datetime(2017, 11, 28, 15, 55, 59, 342380)
		self.assertFalse(self.checker.remainder())
