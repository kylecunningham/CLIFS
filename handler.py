#CLIFS/handler.py
#A part of the command line flight simulator.
#Copyright (c) 2014 ks-salutions.
#This uses Python 3. If you don't know Python 3's syntax, it should be relatively simple to catch up to it.
class handler:
	"""
Handles directions and such. The available functions are:
go (direction, speed)
go_ex (direction, distance, speed)
I'll see about adding more later.
	"""
	def init (self):
		distance = 0 # the distance variable controls the go_ex's second parameter.
		speed = 0 # this variable controls the go and go_ex's second and third parameters, respectively.
		direction = "" # this variable controls the direction. For now, the available directions are as follows: north, east, south, west, northeast, southeast, southwest, northwest, up, down, n, e, s, w, ne, se, sw, nw, u, and d.

	def go (self, direction, speed):
		"""
Causes the aircraft to go in one of the ten available directions (north, east, south, west, northeast, northwest, southeast, southwest, up, or down.)
Parameters:
direction: One of the ten available directions.
speed: Any speed (for now).
		"""
		if direction == "n" or direction == "e" or direction == "s" or direction == "w" or direction == "ne" or direction == "nw" or direction == "se" or direction == "sw" or direction == "u" or direction == "d" or direction=="north" or direction=="east" or direction=="south" or direction=="west" or direction=="northwest" or direction=="southwest" or direction=="northeast" or direction=="southeast" or direction=="up" or direction=="down":
			self.direction = direction
			self.speed = speed
			print ("You go ", direction, " at a speed of ", speed, ".")
		else:
			return -1

	def go_ex (self, direction, distance, speed):
		"""
Same as go (direction, speed), accept that the distance parameter is included now.
		"""
		if direction == "n" or direction == "e" or direction == "s" or direction == "w" or direction == "ne" or direction == "nw" or direction == "se" or direction == "sw" or direction == "u" or direction == "d" or direction=="north" or direction=="east" or direction=="south" or direction=="west" or direction=="northwest" or direction=="southwest" or direction=="northeast" or direction=="southeast" or direction=="up" or direction=="down":
			self.direction = direction
			self.speed = speed
			self.distance = distance
			print ("You go ", direction, " at a speed of ", speed, " within the distance of ", distance, "KM.")
		else:
			return -1
