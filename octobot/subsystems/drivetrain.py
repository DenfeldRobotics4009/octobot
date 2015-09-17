__author__ = "nikolojedison"
import math

import wpilib
from wpilib.command import Subsystem

class Drivetrain(Subsystem):
	'''Class drivetrain uses many things to do many other things.'''

	def __init__(self, robot):
		super().__init__()
		self.robot = robot
