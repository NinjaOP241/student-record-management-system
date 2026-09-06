# Student Record Management & Search System

## A. Title

Student Record Management & Search System

## B. Objective

The objective of this assignment is to develop a Student Record Management and Search System using Python. This system demonstrates the practical application of Object-Oriented Programming (OOP) concepts, file handling (TXT, CSV, JSON), and basic searching and filtering techniques without the use of external data science libraries like Pandas or NumPy.

## C. Features

- **Add a new student:** Input student details and add them to the system.
- **Display student information:** View details of all students, including total marks, average marks, and pass/fail result.
- **Mark calculations:** Calculate total marks with `calculate_total()`, average marks with `calculate_average()`, and pass/fail status with `get_result()`.
- **Search by Student ID:** Find a specific student using their unique ID.
- **Search by Name:** Find students by their name.
- **Search by Department:** Find all students enrolled in a specific department.
- **Search by Average Marks (Condition-based):** Find students whose average marks exceed a given threshold.
- **Update Marks:** Modify the subject marks of an existing student.
- **Remove Student:** Delete a student record from the system using their Student ID.
- **Save and Load Data:** Persistent storage using text (`.txt`), CSV (`.csv`), or JSON (`.json`) file formats.
- **Configurable passing mark:** Set the common passing mark from the command line with `--passing-marks`.
- **Input handling:** Invalid whole-number input is rejected and the user is asked to enter it again.

## D. Project Structure

- `src/main.py` → Command-line interface and program execution (single access point). Parses command line arguments and provides the interactive menu.
- `src/student.py` → `Student` class and student-related methods (calculating totals, averages, determining results).
- `src/manager.py` → `StudentManager` class for the management of multiple student objects, including adding, removing, and searching records.
- `src/file_handler.py` → `FileHandler` class for reading and writing student records in TXT, CSV, and JSON formats.
- `src/utils/error.py` → Custom error classes for handling exceptions gracefully.
- `data/` → Directory containing sample data files (`students.txt`, `students.csv`, `students.json`).
- `screenshots/` → Location for screenshots showing tested program output.

## E. Requirements

- Python 3.x
- No external packages (like Pandas or NumPy) are required. The program relies solely on built-in Python modules (`csv`, `json`, `argparse`).

## F. How to Run

The program is executed from the command line, and it requires you to specify the input data file and its format using command-line arguments.

To run the program with a CSV file:

```bash
python -m src.main --file data/students.csv --format csv
```

To run the program with a JSON file:

```bash
python -m src.main --file data/students.json --format json
```

To run the program with a Text file:

```bash
python -m src.main --file data/students.txt --format txt
```

To use a custom passing mark:

```bash
python -m src.main --file data/students.csv --format csv --passing-marks 50
```

The default passing mark is 40. A student passes when all three subject marks meet or exceed the configured value.

After the records are loaded, the interactive menu provides these options:

```text
1. Add student
2. Display all students
3. Search by student ID
4. Search by name
5. Search by department
6. Search by average marks
7. Update marks
8. Remove student
9. Save records
0. Exit
```

## G. Input and Output

- **Inputs Accepted:** Command-line arguments for file paths and formats. Interactive terminal inputs for menu selections, adding students, updating marks, and providing search criteria.
- **Files Required:** An initial data file containing student records (e.g., `data/students.csv`).
- **Program Output:** The program outputs search results, student details, and confirmation messages directly to the terminal.
- **Output Files:** When choosing the "Save records" option, the program asks for both an output path and an output format. Example output paths are `data/updated_students.txt`, `data/updated_students.csv`, and `data/updated_students.json`.

### Sample Output

```
Records loaded successfully from data/students.csv

==================================================
			STUDENT RECORD MANAGEMENT
==================================================
1. Add student
2. Display all students
3. Search by student ID
4. Search by name
5. Search by department
6. Search by average marks
7. Update marks
8. Remove student
9. Save records
0. Exit
==================================================
...
Enter your choice: 2
Student ID: 101
Name: Rahul
Department: Computer Science
Semester: 5
Subject 1 Marks: 78
Subject 2 Marks: 82
Subject 3 Marks: 69
Total Marks: 229
Average Marks: 76.33
Result: Pass
...
```

## H. OOP Concepts Used

- **Classes:** Used to define the blueprint for `Student`, `StudentManager`, and `FileHandler`.
- **Objects:** Instances of classes are created, such as creating a `Student` object for each record loaded from a file.
- **Constructors:** The `__init__` method is used in `Student` and `StudentManager` to initialize attributes when an object is created.
- **Attributes:** Variables belonging to objects, such as `student_id`, `name`, and `passing_marks`.
- **Instance Methods:** Functions defined inside a class that operate on instances, like `calculate_average()` in `Student` and `search_student()` in `StudentManager`.
- **Additional methods:** `update_marks()` modifies a student's marks, `display_student()` displays one student's details, and `load_from_file()` and `save_to_file()` provide format-independent manager operations.

## I. File Handling Concepts Used

- **TXT Files:** Handled using built-in `open()`, `readlines()`, and `write()`. Records are parsed by splitting lines using a comma delimiter. The input file is opened in read mode and saved files are opened in write mode.
- **CSV Files:** Handled using Python's built-in `csv` module. `csv.reader` is used for reading rows (skipping the header), and `csv.writer` is used to write data with a header.
- **JSON Files:** Handled using Python's built-in `json` module. `json.load()` is used to convert JSON data into Python dictionaries, and `json.dump()` is used to serialize Python objects into a JSON file.
- JSON records use `student_id`, `name`, `department`, `semester`, and a nested `marks` dictionary containing `subject1`, `subject2`, and `subject3`.
- `with open(...) as ...:` Context managers are used to ensure files are properly closed after operations.

## J. Searching Concepts Used

Student records are stored in a Python list within the `StudentManager`. Searching is implemented using basic Python logic:

- `for` loops iterate over the list of student objects.
- `if` conditions evaluate whether a student matches the search criteria (e.g., `student.student_id == search_id`).
- For string matching (Name, Department), `.lower()` is used to ensure case-insensitive searches.
- For condition-based searches, values are compared using basic operators (e.g., `student.calculate_average() > threshold`).

## Testing Summary

The program was tested with five student records using all three input formats. The tests covered loading TXT, CSV, and JSON files; displaying records; searching by ID, name, department, and average; adding a student; updating marks; removing a student; rejecting duplicate IDs; handling invalid menu input; and saving and reloading updated TXT, CSV, and JSON files.

Screenshots of the tested menu and sample output are included in the `screenshots/` directory. The sample output above demonstrates the display operation, including total marks, average marks, and result status.

## K. Learning Outcome / Conclusion

Through this assignment, I reinforced my understanding of Object-Oriented Programming in Python by separating concerns across multiple classes and files. I gained practical experience handling different file formats (TXT, CSV, JSON) using built-in modules and learned how to build a simple interactive command-line application using `argparse`. The assignment also highlighted the effectiveness of basic loops and conditionals for data filtering and search operations without relying on heavier external libraries.
