__author__ = ' ' 

import wpilib
from networktables import NetworkTable
from wpilib.buttons import JoystickButton, InternalButton

class OI:
	"""Button mapping goes here."""

	self.stick = wpilib.Joystick(0)
	self.smart_dashboard = NetworkTable.getTable("SmartDashboard")

	#Buttons
	#-------

	def getJoystick(self):
		"""Drive joystick."""
		return self.stick
