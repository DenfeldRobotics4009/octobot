__author__ = ' '

#May need more libraries in the future, esp. once everything else is properly implemented.
import wpilib
from networktables import NetworkTable
from wpilib.buttons import JoystickButton, InternalButton

from commands.manual.octo_drive_with_joystick import OctoDriveWithJoystick
from pov_button import POVButton

class OI:
    """Button mapping goes here."""

    #Currently a single-joystick setup. May want to change that later if subsystems are added.
    self.stick = wpilib.Joystick(0)
    self.smart_dashboard = NetworkTable.getTable("SmartDashboard")

    #Buttons based off of Logitech Attack 3 joystick used on Delta.
    trigger = JoystickButton(self.stick, 1)
    thumb = JoystickButton(self.stick, 2)
    three = JoystickButton(self.stick, 3)
    four = JoystickButton(self.stick, 4)
    five = JoystickButton(self.stick, 5)
    six = JoystickButton(self.stick, 6)
    seven = JoystickButton(self.stick, 7)
    eight = JoystickButton(self.stick, 8)
    nine = JoystickButton(self.stick, 9)
    ten = JoystickButton(self.stick, 10)
    eleven = JoystickButton(self.stick, 11)
    twelve = JoystickButton(self.stick, 12)
  
    def getJoystick(self):
        """Drive joystick."""
        return self.stick
