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
	
	self.drive_diagonal = wpilib.RobotDrive(DriveMotor(0), DriveMotor(2), DriveMotor(4), DriveMotor(6))
	self.drive_x = wpilib.RobotDrive(DriveMotor(1), DriveMotor(5))
	self.drive_y = wpilib.RobotDrive(DriveMotor(3), DriveMotor(7))
	self.drive_diagonal.setInvertedMotor(self.drive_diagonal.MotorType.kFrontRight, True)
	self.drive_diagonal.setInvertedMotor(self.drive_diagonal.MotorType.kRearRight, True)
	self.drive_x.setInvertedMotor(self.drive_x.MotorType.kRight, True)
	self.drive_y.setInvertedMotor(self.drive_y.MotorType.kRight, True)
	

    def initDefaultCommand(self):
        '''When no other command is running, let the operator drive around using the joystick.'''
        self.setDefaultCommand(OctoDriveWithJoystick(self.robot))

    def log(self):
        pass

    def driveJoystick(self, joystick):
	precision = True
	x = drive_control(joystick.getX(), precision)
	y = drive_control(joystick.getY(), precision)
	z = precision_mode(dead_zone(joystick.getRawAxis(3)*.75, .1), precisiou)
	
	if x>1:
		x=1
	elif x<-1:
		x=-1
	self.driveManual(x,y,z)
	
    def driveManual(self, x, y, rotation):
	self.x, self.y, self.rotation = x, y, rotation
	self.drive_diagonal.mecanumDrive_Cartesian(x, y, rotation, 0)
	self.drive_x.arcadeDrive(x, rotation)
	self.drive_y.arcadeDrive(y, rotation)
