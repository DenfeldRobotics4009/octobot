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
        self.six = wpilib.CANTalon(6)
        self.zed = wpilib.CANTalon(0)
        self.two = wpilib.CANTalon(2)
        self.seven = wpilib.CANTalon(7)
        self.four = wpilib.CANTalon(4)
        self.five = wpilib.CANTalon(5)
        self.three = wpilib.CANTalon(3)

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

	    self.driveManual(x, y)

    def driveManual(self, x, y):
        #6 1, 5 3, 2 0
            self.x, self.y = x, y
        #    self.six.set(x)
        #    self.one.set(x)
        #    self.four.set(x)
        #    self.seven.set(x)
        #    self.two.set(x)
        #    self.zed.set(x)
            self.six.set(y)
            self.one.set(y)
            self.five.set(y)
            self.three.set(y)
            self.two.set(y)
            self.zed.set(y)
