from modules.Car import Car

class CarImpl:
	def __init__(self):
		self.car = Car()
		self.warnings = {
			"fuel": self.car.needsFuel(),
			"temperature": True if self.car.getEngineTemperature() > 200 else False,
		}
		self.isMoving = False
	def driveTo(self, destination):
		self.car.driveTo(destination)
		self.isMoving = bool(destination)
	