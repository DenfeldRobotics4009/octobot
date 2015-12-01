__author__ = "auxiliary-character"
import wpilib
from wpilib.timer import Timer
from wpilib.command import Command
import csv

class PlayMacro(Command):
    """This plays macro movements from the .csv file."""
    def __init__(self, robot, name):
        """Initialize the command and get all the requirements."""
        super().__init__()
        self.robot = robot
        self.requires(robot.drivetrain)
        self.name = name
        self.done_yet = False

    def initialize(self):
        try:
            #attempt to access the files required
            if self.robot.isReal():
                self.f = open("/home/lvuser/py/"+self.name)
            else:
                self.f = open(self.name)
            self.reader_iterator = csv.DictReader(self.f)
        except FileNotFoundError:
            #This bit runs if the file isn't there
            self.reader_iterator = []
        self.setTimeout(15)
        start_time = Timer.getFPGATimestamp()
        for line in self.reader_iterator:
            t_delta = float(line["Time"]) - (Timer.getFPGATimestamp()-start_time)
            if t_delta > 0:
                Timer.delay(t_delta)
            self.robot.drivetrain.driveManual(float(line["Drive_X"]),
                                            float(line["Drive_Y"]),
                                            float(line["Drive_Rotation"]))
            if self.isTimedOut() or self.done_yet:
                break

    def execute(self):
        pass

    def isFinished(self):
        return True

    def end(self):
        self.robot.drivetrain.driveManual(0,0,0)
        if hasattr(self, "f"):
            self.f.close()

    def interrupted(self):
        self.end()

    def cancel(self):
        self.end()
        super().cancel()