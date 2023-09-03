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


def displayClassObjectList(classObjectList, pattern):
    hasAtleastOneSlot = False

    for classSlot in classObjectList:
        if pattern == None:
            pattern = ""

        if classSlot.has_in_course(pattern):
            hasAtleastOneSlot = True

            print(f"Class: {classSlot.course}")
            print(f"Duration: {classSlot.time_slot}")
            print(f"Teacher: {classSlot.instructor}")
            print(f"Room: {classSlot.room}")
            print("")
    if not hasAtleastOneSlot:
        print("\n\n🥳 FREE DAY! 🥳\n\n")
    else:
        print("\n")
