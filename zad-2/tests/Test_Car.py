from modules.Car import Car
from unittest.mock import Mock
import unittest

class Test_Car(unittest.TestCase):
	def test_needsFuel(self):
		car = Car()
		car.needsFuel = Mock(name = "needsFuel")
		car.needsFuel.return_value = True
		self.assertTrue(car.needsFuel())
	def test_getEngineTemperature(self):
		engineTemperature = 100
		car = Car()
		car.getEngineTemperature = Mock(name = "getEngineTemperature")
		car.getEngineTemperature.return_value = engineTemperature
		self.assertEqual(car.getEngineTemperature(), engineTemperature)
	def test_driveTo(self):
		destination = "Brazil"
		car = Car()
		car.driveTo = Mock(name = "driveTo")
		car.driveTo.return_value = destination
		self.assertEqual(car.driveTo(destination), destination)
