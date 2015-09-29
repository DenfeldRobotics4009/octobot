__author__ = "nikolojedison"
import math

import wpilib
from wpilib.command import Subsystem

class Drivetrain(Subsystem):
	'''Class drivetrain uses many things to do many other things.'''

	def __init__(self, robot):
		super().__init__()
		self.robot = robot
		
		self.drive = wpilib.RobotDrive(DriveMotor(0), DriveMotor(1), DriveMotor(2), DriveMotor(3))
		self.drive_aux = wpilibRobotDrive(DriveMotor(4), DriveMotor(5), DriveMotor(6), DriveMotor(7))
		self.drive.setExpiration(0.1)

		self.drive.setInvertedMotor(self.drive.MotorType.kFrontRight, True)
		self.drive.setInvertedMotor(self.drive.MotorType.kRearRight, True)
		self.drive_aux.setInvertedMotor(self.drive_aux.setInvertedMotor.MotorType.kFrontRight, True)
		self.drive_aux.setInvertedMotor(self.drive_aux.setInvertedMotor.MotorType.kRearRight, True)
		
		self.x = 0
		self.y = 0
		self.rotation = 0

	def initDefaultCommand(self):
		'''When no other command is running, let the operator drive around using the joystick.'''
		self.setDefaultCommand(OctoDriveWithJoystick(self.robot))

	def log(self):
		pass

	def driveJoystick(self, joystick):
		x = drive_control(joystick.getX(), precision)
		y = drive_control(joystick.getY(), precision)
		z = precision_mode(dead_zone(joystick.getRawAxis(3)*.75, .1), precision)
		if x>1:
			x=1
		elif x<-1:
			x=-1
		self.driveManual(x,y,z)

	def driveManual(self, x, y, rotation):
		self.x, self.y, self.rotation = x, y, rotation
		self.drive.mecanumDrive_Cartesian(x, y, rotation, 0)
		self.drive_aux.mecanumDrive_Cartesian(x, y, rotation, 0)

