__author__ = "nikolojedison"
from wpilib.command import Command
from utilities.imu_simple import IMUSimple

class GyroReset(Command):
    """Reset the gyro."""

    def __init__(self, robot):
        self.robot = robot
        self.gyro = IMUSimple()
        a = self.gyro.getYaw()

    def execute(self, a):
        b = a - self.gyro.getYaw()
        return b

    def isFinished(self):
        return False

    def end(self):
        pass

    def interrupted(self):
        pass
