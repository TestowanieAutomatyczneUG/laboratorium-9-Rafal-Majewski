from modules.Car import Car
from unittest.mock import Mock
import unittest

# test the Car class

class Test_Car(unittest.TestCase):
	def test_needsFuel(self):
		car = Car()
		car.needsFuel = Mock(name = "needsFuel")
		car.needsFuel.return_value = True
		self.assertTrue(car.needsFuel())
	def test_getEngineTemperature(self):
		car = Car()
		car.getEngineTemperature = Mock(name = "getEngineTemperature")
		car.getEngineTemperature.return_value = 100
		self.assertEqual(car.getEngineTemperature(), 100)
	def test_driveTo(self):
		destination = "Brazil"
		car = Car()
		car.driveTo = Mock(name = "driveTo")
		car.driveTo.return_value = destination
		self.assertEqual(car.driveTo(destination), destination)
