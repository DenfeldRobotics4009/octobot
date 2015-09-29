__author__ = ' '

from wpilib.command import Command

class OctoDriveWithJoystick(Command):
	"""Have the robot drive with the octo setup using the joystick until interrupted."""

	def __init__(self, robot):
		super().__init__()
		self.robot = robot
		self.requires(self.robot.drivetrain)

	def execute(self):
		self.robot.drivetrain.driveJoystick(self.robot.oi.getJoystick())
	
	def isFinished(self):
		return False

	def end(self):
		pass

	def interrupted(self):
		self.end()
