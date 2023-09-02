class Class:
    def __init__(self, time_slot, instructor, course, room, weekday):
        self.time_slot = time_slot
        self.instrucor = instructor
        self.course = course
        self.room = room
        self.weekday = weekday


def isValidClass(classDataString):
    return str(classDataString).lstrip().rstrip().find("\n") != -1
