import time
import pandas as pd
import class_object as co
from class_object import Class
from fetch import download_timetable

fileName = "timetable.xlsx"

print(
    """
 _______ _______  ______ _______    _______ _                         _     _        
(_______|_______)/ _____|_______)  (_______|_)              _        | |   | |       
 _____   _______( (____     _          _    _ ____  _____ _| |_ _____| |__ | | _____ 
|  ___) |  ___  |\____ \   | |        | |  | |    \| ___ (_   _|____ |  _ \| || ___ |
| |     | |   | |_____) )  | |        | |  | | | | | ____| | |_/ ___ | |_) ) || ____|
|_|     |_|   |_(______/   |_|        |_|  |_|_|_|_|_____)  \__)_____|____/ \_)_____)
                                                                                     
 ______                                                                              
(_____ \                                                                             
 _____) )____  ____ ___ _____  ____                                                  
|  ____(____ |/ ___)___) ___ |/ ___)                                                 
| |    / ___ | |  |___ | ____| |                                                     
|_|    \_____|_|  (___/|_____)_|                                                     
                                                                                     
"""
)

# Created by Sarim Ahmed (github.com/thenoisyninga)

print("\n[+] Welcome!\n[+] Hold up, let me read the timetable 🧐...\n")

# Automatically add the timetable or add it manually in the same directory as this file with the name timetable.xlsx
# choice = input(
#     "[+] Do you want to download the timetable automatically from Google Sheet? (y/n): "
# )

# if choice.lower() == "y":
#     print("[+] Attempting to download the new sheet...")
#     downloaded = download_timetable()

#     if not downloaded:
#         exit()

# else:
#     print("[+] Okay, I will use the timetable.xlsx file in this directory.\n")

# Read the timetable.xlsx file
try:
    timeTable = pd.ExcelFile(fileName)
except FileNotFoundError:
    print(
        f"[-] I couldn't find the timetable.xlsx file in this directory, please make sure it is in the same directory as this file and try again.\n"
    )
    exit()


# Funciton to check if given string is a day name
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

    if weekdays.__contains__(str(sheetName).strip().upper()):
        return True
    else:
        return False


# Ask the user for their section number
patternList = str(
    input("Write your section (pattern I will use to search for your classes), you can add multiple patterns too if you have electives, making them comma seperated: ")
).split(",")
print("")

# check every sheet
for sheet in timeTable.sheet_names:
    # for sheets who's name are weekdays
    if is_weekday(sheet):
        time.sleep(0.25)
        print("=========================================================")
        print(f"            📚 SCHEDULE FOR {sheet.upper()} 🖊️ ")
        print("=========================================================\n")

        dayClasses = []

        # Read complete excel sheet including the title columns/rows in this variable
        completeExcelSheet = timeTable.parse(sheet)
        completeExcelSheetArray = completeExcelSheet.to_numpy()

        # Read excel sheet excluding the title columns/rows in this variable
        dayTimeTable = timeTable.parse(sheet, header=3, index_col=0)
        classesArray = dayTimeTable.to_numpy()

        # loop over every cell
        for i in range(len(classesArray)):
            row = classesArray[i]
            for j in range(len(row)):
                classData = row[j]

                # if the current slot is a valid class
                if co.isValidClassData(classData):
                    # reading slot time and classroom and slot number(index)
                    classroom = completeExcelSheetArray[i + 3][0]
                    timeSlot = completeExcelSheetArray[1][j + 1]
                    index = completeExcelSheetArray[0][j + 1]

                    # extracting more info from the class cell
                    instructor = str(classData).split("\n")[1].rstrip().lstrip()
                    course = str(classData).split("\n")[0].rstrip().lstrip()

                    # (this next part accounts for the merged cells used for lab classes)

                    # checking if current cell is a lab class
                    if co.isLabClassData(classData):
                        # Update the timeslot duration to extend to 3 slots

                        # get the timeslot for the last lab slot
                        labLastTimeSlot = completeExcelSheetArray[1][(j + 1) + 2]

                        # new timeslot = the starting time of the first slot and the
                        # ending time of the last slot
                        timeSlot = f"{timeSlot.split('-')[0].strip()}-{labLastTimeSlot.split('-')[1].strip()}"

                        pass

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

        # there is a second argument which takes your section
        # name as a pattern to search for when printing class' data, if
        # it is set to None, the progarm will print all slots.

        co.displayClassObjectList(  
            classObjectList=dayClasses,
            patternList=patternList,
        )

print("\n[-] Thank you for choosing my services! 😊🫡, now i will die.\n\n")
