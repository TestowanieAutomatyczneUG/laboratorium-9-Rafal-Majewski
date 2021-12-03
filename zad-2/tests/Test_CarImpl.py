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
		


	# def test_needsFuel(self):
	# 	Car.needsFuel = Mock()
	# 	Car.needsFuel.return_value = True
	# 	Car.getEngineTemperature = Mock()
	# 	Car.getEngineTemperature.return_value = 500
	# 	carImpl = CarImpl()
	# 	self.assertTrue(carImpl.warnings["fuel"])
		# self.car.needsFuel = Mock(name = "needsFuel")
		# self.car.needsFuel.return_value = True
		# self.assertTrue(self.car.needsFuel())
	# def test_getEngineTemperature(self):
	# 	engineTemperature = 100
	# 	self.car.getEngineTemperature = Mock(name = "getEngineTemperature")
	# 	self.car.getEngineTemperature.return_value = engineTemperature
	# 	self.assertEqual(self.car.getEngineTemperature(), engineTemperature)
	# def test_driveTo(self):
	# 	destination = "Brazil"
	# 	self.car.driveTo = Mock(name = "driveTo")
	# 	self.car.driveTo.return_value = destination
	# 	self.assertEqual(self.car.driveTo(destination), destination)
