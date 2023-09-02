import pandas as pd
from class_object import isValidClass

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

        dayTimeTable = timeTable.parse(sheet, header=3, index_col=0)
        classesArray = dayTimeTable.to_numpy()

        for row in classesArray:
            for classData in row:
                print("\n")
                print(classData)
                print(isValidClass(classData))

        break
