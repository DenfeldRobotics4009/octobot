#!/usr/bin/env python3
__author__ = ' '

import wpilib
import networktables
from wpilib.command import Scheduler
from oi import OI

from subsystems.drivetrain import Drivetrain

class OctoBot(wpilib.SampleRobot):

    def robotInit(self):
        self.drivetrain = Drivetrain(self)

    def autonomous(self):
        while self.isAutonomous() and self.isEnabled():
            Scheduler.getInstance().run()
            self.log()
            wpilib.Timer.delay(.005)

    def operatorControl(self):
        self.drivetrain.drive.setSafetyEnabled(True)
        self.drivetrain.drive_aux.setSafetyEnabled(True)
        joystick = self.oi.getJoystick()

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
        self.drivetrain.log()

if __name__ == "__main__":
    wpilib.run(OctoBot)
