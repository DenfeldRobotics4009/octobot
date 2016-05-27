 #!/usr/bin/env python3
__author__ = "nikolojedison"

import wpilib
import networktables
from wpilib.command import Scheduler
from oi import OI

from subsystems.drivetrain import Drivetrain

from utilities.drive_control import *
from commands.play_macro import PlayMacro

class OctoBot(wpilib.SampleRobot):

    #Initialise the robot.
    def robotInit(self):
        self.drivetrain = Drivetrain(self)
        self.oi = OI(self)
    
    def autonomous(self):
        while self.isAutonomous() and self.isEnabled():
            Scheduler.getInstance().run()
            self.log()
            wpilib.Timer.delay(.005)

    def operatorControl(self):
        joystick = self.oi.getStick()

        while self.isOperatorControl() and self.isEnabled():
            self.log()
            Scheduler.getInstance().run()
            wpilib.Timer.delay(.005)

    def disabled(self):
        """Stuff to do whilst disabled."""

        while self.isDisabled():
            self.log()
            wpilib.Timer.delay(.005)

    def test(self):
        """No tests"""
        pass

    def log(self):
        """It's big, it's heavy, it's wood."""
        #SOMEDAY WE WILL FIGURE OUT LOGGING. I PROMISE.
        self.drivetrain.log()

if __name__ == "__main__":
    wpilib.run(OctoBot)
