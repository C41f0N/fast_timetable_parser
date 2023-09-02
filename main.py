import pandas as pd

timeTable = pd.ExcelFile("timetable.xlsx")

# Getting sheet names
sheetNames = timeTable.sheet_names


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


print(is_weekday("january"))
