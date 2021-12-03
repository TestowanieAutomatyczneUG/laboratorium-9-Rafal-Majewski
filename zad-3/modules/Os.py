from datetime import datetime
from pydub import AudioSegment
from pydub.playback import play
import os

class WrongFileTypeError(Exception):
	def __init__(self, message):
		self.message = message

class FileNotFoundError(Exception):
	def __init__(self, message):
		self.message = message

class PlayingError(Exception):
	def __init__(self, message):
		self.message = message

class Os:
	# def __init__(self):
	# 	self.isPlaying = False
	def getTime(self):
		return datetime.now()
	def playWavFile(self, filepath):
		if not os.path.isfile(filepath):
			raise FileNotFoundError("File not found")

		if not filepath.endswith(".wav"):
			raise WrongFileTypeError("File is not a wav file")
		try:
			# self.isPLaying = True
			play(AudioSegment.from_wav(filepath))
		except KeyboardInterrupt:
			pass
		except Exception as e:
			raise PlayingError("Playing error")
		# finally:
		# 	self.isPlaying = False