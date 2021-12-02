from modules.Os import Os

class Checker:
	def __init__(self):
		self.os = Os()
	def remainder(self):
		if self.os.getTime().hour >= 17:
			self.os.playWavFile("./data/vstavej.wav")
			return True
		return False