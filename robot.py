 #!/usr/bin/env python3
__author__ = "nikolojedison"

#May need more libraries in the future, esp. once everything else is properly implemented.
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
    
    #Probably will be changed once macros are added, currently just
    #placeholder text to make sure nothing explodes.
    def autonomous(self):
        while self.isAutonomous() and self.isEnabled():
            Scheduler.getInstance().run()
            self.log()
            wpilib.Timer.delay(.005)

    def operatorControl(self):
        joystick = self.oi.getStick()
        #Should look into whether buttons need to be imported here as well.

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
        #No tests. Probably something to figure out sometime.
        pass

    def log(self):
        """It's big, it's heavy, it's wood."""
        #SOMEDAY WE WILL FIGURE OUT LOGGING. I PROMISE.
        self.drivetrain.log()

if __name__ == "__main__":
    wpilib.run(OctoBot)
