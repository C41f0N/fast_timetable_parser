import re


class Class:
    def __init__(self, time_slot, instructor, course, room, weekday, index):
        self.time_slot = time_slot
        self.instructor = instructor
        self.course = course
        self.room = room
        self.weekday = weekday
        self.index = index

    def has_in_course(self, pattern):
        return pattern in self.course


def isValidClassData(classDataString):
    return str(classDataString).lstrip().rstrip().find("\n") != -1


def isLabClassData(classDataString):
    return "LAB" in re.split("\s|-", str(classDataString))


def displayClassObjectList(classObjectList):
    for classSlot in classObjectList:
        if classSlot.has_in_course("BCS-1D"):
            print("=================================================")
            print(classSlot.course)
            print(classSlot.time_slot)
            print(classSlot.instructor)
            print(classSlot.room)
            print(classSlot.weekday)
            print(classSlot.index)
            print("=================================================\n\n")
