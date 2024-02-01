import re


# a class object for each slot
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
    # checks if the cell is a class slot
    return str(classDataString).lstrip().rstrip().find("\n") != -1


def isLabClassData(classDataString):
    # checks if the word "LAB" exists in the cell
    return "lab" in re.split("\s|-", str(classDataString.lower()))


def displayClassObjectList(classObjectList, pattern):
    hasAtleastOneSlot = False

    # list of classes that match the pattern
    currentClasses = {}

    for classSlot in classObjectList:
        if pattern == None:
            pattern = ""

        if classSlot.has_in_course(pattern):
            hasAtleastOneSlot = True

            # putting matching slots in dictionary with the slot index as key
            currentClasses[int(classSlot.index)] = classSlot

    if not hasAtleastOneSlot:
        print("\n\n🥳 FREE DAY! 🥳\n\n")
    else:
        # sorting the dictionary by keys
        currentClasses = dict(sorted(currentClasses.items()))

        # printing the dictionary values in order of keys
        for index in currentClasses:
            classObject = currentClasses[index]
            print(f"Class: {classObject.course}")
            print(f"Duration: {classObject.time_slot}")
            print(f"Teacher: {classObject.instructor}")
            print(f"Room: {classObject.room}")
            print("")

        print("\n")
