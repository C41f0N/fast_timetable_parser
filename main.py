import pandas as pd
import class_object
from class_object import Class

fileName = "timetable.xlsx"

timeTable = pd.ExcelFile(fileName)


# Checks if given string qualifies as a day name
def is_weekday(sheetName):
    weekdays = [
        "MONDAY",
        "TUESDAY",
        "WEDNESDAY",
        "THURSDAY",
        "FRIDAY",
        "SATURDAY",
        "SUNDAY",
    ]

    if weekdays.__contains__(str(sheetName).upper()):
        return True
    else:
        return False


for sheet in timeTable.sheet_names:
    # for sheets that qualify as weekdays
    if is_weekday(sheet):
        print(f"*** DATA FOR {sheet.upper()} ***")

        dayClasses = []

        # Read complete excel sheet including the title columns/rows
        completeExcelSheet = timeTable.parse(sheet)
        completeExcelSheetArray = completeExcelSheet.to_numpy()

        # Read excel sheet excluding the title columns/rows
        dayTimeTable = timeTable.parse(sheet, header=3, index_col=0)
        classesArray = dayTimeTable.to_numpy()

        # loop over every cell
        for i in range(len(classesArray)):
            row = classesArray[i]
            for j in range(len(row)):
                classData = row[j]

                # if the current slot is a valid class
                if class_object.isValidClassData(classData):
                    # reading slot time and classroom and slot number(index)
                    classroom = completeExcelSheetArray[i + 3][0]
                    timeSlot = completeExcelSheetArray[1][j + 1]
                    index = completeExcelSheetArray[0][j + 1]

                    # extracting more info from the class
                    instructor = str(classData).split("\n")[1].rstrip().lstrip()
                    course = str(classData).split("\n")[0].rstrip().lstrip()

                    # this part accounts for the merged cells for lab classes

                    # checking if current cell is a lab class
                    if class_object.isLabClassData(classData):
                        # Create the next three class slots instead of one

                        # get the timeslot for next two slots
                        timeSlot2 = completeExcelSheetArray[1][(j + 1) + 1]
                        timeSlot3 = completeExcelSheetArray[1][(j + 1) + 2]

                        labClass1 = currentClass = Class(
                            time_slot=timeSlot,
                            instructor=instructor,
                            room=classroom,
                            weekday=sheet,  # sheetname is weekday
                            index=index,
                            course=course,
                        )

                        labClass2 = currentClass = Class(
                            time_slot=timeSlot2,
                            instructor=instructor,
                            room=classroom,
                            weekday=sheet,  # sheetname is weekday
                            index=index + 1,
                            course=course,
                        )

                        labClass3 = currentClass = Class(
                            time_slot=timeSlot3,
                            instructor=instructor,
                            room=classroom,
                            weekday=sheet,  # sheetname is weekday
                            index=index + 2,
                            course=course,
                        )

                        dayClasses.append(labClass1)
                        dayClasses.append(labClass2)
                        dayClasses.append(labClass3)

                        pass

                    else:
                        # Create a class object using the classData
                        currentClass = Class(
                            time_slot=timeSlot,
                            instructor=instructor,
                            room=classroom,
                            weekday=sheet,  # sheetname is weekday
                            index=index,
                            course=course,
                        )

                        dayClasses.append(currentClass)

        class_object.displayClassObjectList(dayClasses)
        break
