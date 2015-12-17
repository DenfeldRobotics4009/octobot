__author__ = "nikolojedison"
import math

import wpilib
from wpilib.command import Subsystem

from utilities.drive_control import *
from commands.manual.octo_drive_with_joystick import OctoDriveWithJoystick
#from utilities.imu_simple import IMUSimple

class GyroDummy:
    """Makes the sim happy. Written by Aux, copied from 2015 code"""
    n = 0
    def getYaw(self):
        n = self.n
        n = n+1
        if n > 180:
            n = n-360
        elif n < -180:
            m = n+360
        self.n = n
        return n

class Drivetrain(Subsystem):
    '''Class drivetrain uses many things to do many other things.'''

    def __init__(self, robot):
        super().__init__()
        self.robot = robot

        self.gyro = GyroDummy()

        #Gyro definitions, I think...
        self.x = 0
        self.y = 0
        self.rotation = 0
        
        #Motor definitions
        self.one = wpilib.CANTalon(1)
        self.front_right_motor = wpilib.CANTalon(6)
        self.rear_right_motor = wpilib.CANTalon(0)
        self.two = wpilib.CANTalon(2)
        self.top_motor = wpilib.CANTalon(7)
        self.bottom_motor = wpilib.CANTalon(4)
        self.five = wpilib.CANTalon(5)
        self.three = wpilib.CANTalon(3)
	    
        #This... might work? Maybe? Needs testing, or at the very least a sim run.
        self.drive_diagonal = wpilib.RobotDrive(self.one, self.front_right_motor, self.rear_right_motor, self.two)
        self.drive_x = wpilib.RobotDrive(self.top_motor, self.bottom_motor)
        self.drive_y = wpilib.RobotDrive(self.five, self.three)
        #switch 2
        self.drive_diagonal.setInvertedMotor(self.drive_diagonal.MotorType.kFrontRight, True)
        self.drive_diagonal.setInvertedMotor(self.drive_diagonal.MotorType.kRearLeft, True)
        self.drive_x.setInvertedMotor(self.drive_x.MotorType.kFrontLeft, True)
        self.drive_y.setInvertedMotor(self.drive_y.MotorType.kFrontRight, True)

	

    def initDefaultCommand(self):
        '''When no other command is running, let the operator drive around using the joystick.'''
        self.setDefaultCommand(OctoDriveWithJoystick(self.robot))

    def log(self):
        pass
        #Still no logging implementation.

    def driveJoystick(self, joystick):
        #Start precision mode
	    precision = True
        #set the axes & pass them to the drive_control utility library
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
	    #Set the corner wheels to be mecanums.
	    self.drive_diagonal.mecanumDrive_Cartesian(x, y, rotation, 0)
	    #Set the x & y axis wheels to be arcade. These'll run at the same time as the corner wheels if they're 
	    #working properly.
	    self.drive_x.arcadeDrive(x, rotation)
	    self.drive_y.arcadeDrive(y, rotation)
