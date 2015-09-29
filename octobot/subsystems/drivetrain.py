__author__ = "nikolojedison"
import math

import wpilib
from wpilib.command import Subsystem
from commands.manual.octo_drive_with_joystick import OctoDriveWithJoystick
class Drivetrain(Subsystem):
	'''Class drivetrain uses many things to do many other things.'''

	def __init__(self, robot):
		super().__init__()
		self.robot = robot
		
		self.nw = wpilib.Talon(0) 
		self.n = wpilib.Talon(1)
		self.ne = wpilib.Talon(2)
		#self.Extraverted iNtuiton... no, wait...
		self.e = wpilib.Talon(3)
		self.se = wpilib.Talon(4)
		self.s = wpilib.Talon(5)
		self.sw = wpilib.Talon(6)
		self.w = wpilib.Talon(7)

		self.x = 0
		self.y = 0
		self.rotation = 0

	def initDefaultCommand(self):
		'''When no other command is running, let the operator drive around using the joystick.'''
		self.setDefaultCommand(OctoDriveWithJoystick(self.robot))

	def log(self):
		pass

	def manualSet(self, output):
		self.nw.set(output)
        self.n.set(output)
        self.ne.set(output)
        self.e.set(output)
        self.se.set(output)
        self.s.set(output)
        self.sw.set(output)
        self.w.set(output)
