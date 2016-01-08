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

      #  if robot.isReal():
       #     self.gyro = IMUSimple()
       # else:
       #     self.gyro = GyroDummy()

        self.gyro = GyroDummy()

        #Gyro definitions, I think...
        self.x = 0
        self.y = 0
        self.rotation = 0

        #Motor definitions
        self.zed = wpilib.CANTalon(0)
        self.one = wpilib.CANTalon(1)
        self.two = wpilib.CANTalon(2)
        self.three = wpilib.CANTalon(3)
        self.four = wpilib.CANTalon(4)
        self.five = wpilib.CANTalon(5)
        self.six = wpilib.CANTalon(6)
        self.seven = wpilib.CANTalon(7)

        self.drive_diagonal = wpilib.RobotDrive(self.zed, self.two, self.six, self.one)
        self.drive_x = wpilib.RobotDrive(self.three, self.five)
        self.drive_y = wpilib.RobotDrive(self.four, self.seven)

        self.drive_diagonal.setInvertedMotor(self.drive_diagonal.MotorType.kRearLeft, True)
        self.drive_diagonal.setInvertedMotor(self.drive_diagonal.MotorType.kRearRight, True)

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
        #-----------------------------------------------------------------------
        #the getX() and getY() bits are both 0 indexed according to the joystick
        #documentation for WPIlib, so X = 0, Y = 1, Z = 2, twist (supposedly) =
        #3, etc. The thing is, the default throttle axis is set to 3, and the
        #default twist axis is set to 2.
        #So.
        #When we tested previous versions on the robot with getRawAxis(3), the
        #throttle would do the things (different joystick setup on Lopez Jr
        #iirc, so that's part of it).
        #Now (1/5/16), I've set getRawAxis(2). Works fine.

	    x = drive_control(joystick.getX()*2, precision)
	    y = drive_control(joystick.getY()*2, precision)
	    z = precision_mode(dead_zone(joystick.getRawAxis(2)*2, .1), precision)
	    #a = self.gyro.getYaw()
	    a = 0
	    self.driveManual(x, y, z, a)
	    if x>1:
		    x=1
	    elif x<-1:
		    x=-1

    #invert zed and one for rotation
    #def driveManual(self, x, y, z):
    def driveManual(self, x, y, rotation, a):
        self.x, self.y, self.rotation, self.a = x, y, rotation, a
        self.drive_diagonal.mecanumDrive_Cartesian(x, y, rotation, a)
        self.drive_x.arcadeDrive(y, -rotation)
        self.drive_y.arcadeDrive(x, rotation)
        if rotation < 0.0625 or > 0.0625:
            self.drive_diagonal.setInvertedMotor(self.drive_diagonal.MotorType.kFrontLeft, True)
            self.drive_diagonal.setInvertedMotor(self.drive_diagonal.MotorType.kFrontRight, True)
        else:
            self.drive_diagonal.setInvertedMotor(self.drive_diagonal.MotorType.kFrontLeft, False)
            self.drive_diagonal.setInvertedMotor(self.drive_diagonal.MotorType.kFrontRight, False)

            #self.x, self.y, self.z = x, y, z
            #self.four.set(x*.8)
            #self.seven.set(-x*.8)
            #self.five.set(-y*.8)
            #self.three.set(y*.8)

            #What happens here works fine. Don't question it.

            #if x > 0.0625 or x < -0.0625 :
            #    self.six.set(-x)
            #    self.one.set(-x)
            #    self.four.set(x*.8)
            #    self.seven.set(-x*.8)
            #    self.two.set(x)
            #    self.zed.set(x)

        #    elif y > 0.0625 or y < -0.0625:
            #    self.six.set(-y)
            #    self.one.set(y)
            #    self.five.set(-y*.8)
            #    self.three.set(y*.8)
            #    self.two.set(y)
            #    self.zed.set(-y)

        #    elif z > 0.0625 or z < -0.0625:
            #    self.zed.set(z)
            #    self.one.set(z)
            #    self.two.set(z)
            #    self.three.set(-z)
            #    self.four.set(z)
            #    self.six.set(z)
            #    self.five.set(-z)
            #    self.seven.set(z)

            #if all the joystick inputs aren't doing the things, set all the
            #motors to 0
        #    else:
            #    self.zed.set(0)
            #    self.one.set(0)
            #    self.two.set(0)
            #    self.three.set(0)
            #    self.four.set(0)
            #    self.five.set(0)
            #    self.six.set(0)
            #    self.seven.set(0)
