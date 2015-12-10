__author__ = "nikolojedison"
import math

import wpilib
from wpilib.command import Subsystem

from utilities.drive_control import *
from commands.manual.octo_drive_with_joystick import OctoDriveWithJoystick
from utilities.imu_simple import IMUSimple

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
        
        #If the robot is real, use the IMUSimple library...
        if robot.isReal():
            self.gyro = IMUSimple()
        #...but if the robot isn't real, use the dummy library (defined on lines 11-23)
        else:
            self.gyro = GyroDummy()

        #Gyro definitions, I think...
        self.x = 0
        self.y = 0
        self.rotation = 0
	    
        #This... might work? Maybe? Needs testing, or at the very least a sim run.
        self.drive_diagonal = wpilib.RobotDrive(DriveMotor(0), DriveMotor(2), DriveMotor(4), DriveMotor(6))
        self.drive_x = wpilib.RobotDrive(DriveMotor(1), DriveMotor(5))
        self.drive_y = wpilib.RobotDrive(DriveMotor(3), DriveMotor(7))
        self.drive_diagonal.setInvertedMotor(self.drive_diagonal.MotorType.kFrontRight, True)
        self.drive_x.setInvertedMotor(self.drive_x.MotorType.kFrontRight, True)
        self.drive_y.setInvertedMotor(self.drive_y.MotorType.kFrontRight, True)
        self.drive_diagonal.controllerClass(CANTalon())
        self.drive_x.controllerClass(CANTalon())
        self.drive_y.controllerClass(CANTalon())
	

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
