# Timetable Parser for FAST NU

A python program to read the timetable excel file and perform operations on it. Basically what Timetable Notificare does, but you can look into it and see how it works, and also it has no UI. It is also compatible with the recent format changes.

Feel free to contribute to the project. As of now it is not ideal for those with electives.

![image](https://github.com/thenoisyninga/fast_timetable_parser/assets/88588593/44abd4b2-68db-465b-bcb4-42fe8c4b12c2)

![image](https://github.com/thenoisyninga/fast_timetable_parser/assets/88588593/fa24d16b-e24e-42d5-9517-c2dfd9cac268)

# Usage
- Install dependencies by running ``` pip install -r requirements.txt ``` in the project directory.
- Copy the timetable excel file into the project directory.
- Run main.py.
- The program asks for a section, which basically works as a search query for the courses.

# Conditions
The conditions required for the app to continue working on the timetable are as follows:
- The position of the title rows and columns (slots numbers, classrooms, slot duration) cannot change.
- The number of slots and their timings can vary as long as the format of writing time duration does not change.
- Each class cell should have the instructor and the course seperated by a linebreak ("\n"), the course should come first and instructor second.
- The labs have to cover exactly 3 slots (in succession), cells should be merged.
- No cells other than the lab ones should be merged.
