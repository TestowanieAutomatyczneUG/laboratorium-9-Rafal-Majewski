from modules.Car import Car
from unittest.mock import Mock
import unittest

class Test_Car(unittest.TestCase):
	def setUp(self):
		self.car = Car()
	def test_needsFuel(self):
		self.car.needsFuel = Mock(name = "needsFuel")
		self.car.needsFuel.return_value = True
		self.assertTrue(self.car.needsFuel())
	def test_getEngineTemperature(self):
		engineTemperature = 100
		self.car.getEngineTemperature = Mock(name = "getEngineTemperature")
		self.car.getEngineTemperature.return_value = engineTemperature
		self.assertEqual(self.car.getEngineTemperature(), engineTemperature)
	def test_driveTo(self):
		destination = "Brazil"
		self.car.driveTo = Mock(name = "driveTo")
		self.car.driveTo.return_value = destination
		self.assertEqual(self.car.driveTo(destination), destination)
