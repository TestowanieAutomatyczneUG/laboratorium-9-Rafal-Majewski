from modules.Car import Car
from modules.CarImpl import CarImpl
from unittest.mock import Mock, patch
import unittest



class Test_Car(unittest.TestCase):
	# def __init__(self):

	# def setUp(self):
	# 	print(CarImpl.needsFuel)
	# 	self.carImpl = CarImpl()
	@patch("modules.Car.getEngineTemperature")
	@patch("modules.Car.needsFuel")
	def test_needs_fuel(self, needsFuel, getEngineTemperature):
		needsFuel.return_value = True
		getEngineTemperature.return_value = 500
		carImpl = CarImpl()
		self.assertTrue(carImpl.warnings["fuel"])
	@patch("modules.Car.getEngineTemperature")
	@patch("modules.Car.needsFuel")
	def test_doesnt_needs_fuel(self, needsFuel, getEngineTemperature):
		needsFuel.return_value = False
		getEngineTemperature.return_value = 500
		carImpl = CarImpl()
		self.assertFalse(carImpl.warnings["fuel"])
	@patch("modules.Car.getEngineTemperature")
	@patch("modules.Car.needsFuel")
	def test_high_temperature(self, needsFuel, getEngineTemperature):
		needsFuel.return_value = True
		getEngineTemperature.return_value = 600
		carImpl = CarImpl()
		self.assertTrue(carImpl.warnings["temperature"])
	@patch("modules.Car.getEngineTemperature")	
	@patch("modules.Car.needsFuel")
	def test_low_temperature(self, needsFuel, getEngineTemperature):
		needsFuel.return_value = True
		getEngineTemperature.return_value = 20
		carImpl = CarImpl()
		self.assertFalse(carImpl.warnings["temperature"])
	@patch("modules.Car.getEngineTemperature")
	@patch("modules.Car.needsFuel")
	def test_idle(self, needsFuel, getEngineTemperature):
		needsFuel.return_value = True
		getEngineTemperature.return_value = 500
		carImpl = CarImpl()
		self.assertFalse(carImpl.isMoving)
	@patch("modules.Car.getEngineTemperature")
	@patch("modules.Car.needsFuel")
	def test_moving(self, needsFuel, getEngineTemperature):
		needsFuel.return_value = True
		getEngineTemperature.return_value = 500
		carImpl = CarImpl()
		carImpl.driveTo("Brazil")
		self.assertTrue(carImpl.isMoving)
