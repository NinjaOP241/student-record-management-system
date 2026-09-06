"""Command-line interface for the Student Record Management System."""

import argparse

from src.student import Student
from src.manager import StudentManager
from src.file_handler import FileHandler
from src.utils.error import StudentRecordError


def parse_arguments():
    """Parse command-line arguments."""

    # Command-line arguments keep file paths, formats, and rules configurable.
    parser = argparse.ArgumentParser(
        description="Student Record Management and Search System"
    )

    parser.add_argument(
        "--file",
        required=True,
        help="Path to the student record file"
    )

    parser.add_argument(
        "--format",
        choices=["txt", "csv", "json"],
        required=True,
        help="Format of the student record file"
    )

    parser.add_argument(
        "--passing-marks",
        type=int,
        default=40,
        help="Passing marks for each subject (default: 40)"
    )

    return parser.parse_args()


def print_heading(title):
    """Print a simple heading for a menu operation."""
    print("\n" + "-" * 50)
    print(title)
    print("-" * 50)


def read_integer(prompt):
    """Read an integer without closing the menu after bad input."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid whole number.")


def add_student(manager):
    """Read student details and add a new student."""

    print_heading("ADD STUDENT")
    student_id = read_integer("Enter Student ID: ")
    name = input("Enter Name: ")
    department = input("Enter Department: ")
    semester = read_integer("Enter Semester: ")
    subject1_marks = read_integer("Enter Subject 1 Marks: ")
    subject2_marks = read_integer("Enter Subject 2 Marks: ")
    subject3_marks = read_integer("Enter Subject 3 Marks: ")

    student = Student(
        student_id,
        name,
        department,
        semester,
        subject1_marks,
        subject2_marks,
        subject3_marks
    )

    try:
        manager.add_student(student)
        print("Student added successfully.")
    except StudentRecordError as error:
        print(f"Error: {error}")


def search_by_id(manager):
    """Search for and display a student by ID."""

    print_heading("SEARCH BY STUDENT ID")
    student_id = read_integer("Enter Student ID: ")

    student = manager.search_student(student_id)

    if student is None:
        print(f"No student found with ID {student_id}.")
        return

    student.display_student(manager.passing_marks)


def search_by_name(manager):
    """Search for and display students by name."""

    print_heading("SEARCH BY NAME")
    name = input("Enter Student Name: ")

    students = manager.search_by_name(name)

    if not students:
        print(f"No students found with name '{name}'.")
        return

    for student in students:
        student.display_student(manager.passing_marks)
        print()


def search_by_department(manager):
    """Search for and display students by department."""

    print_heading("SEARCH BY DEPARTMENT")
    department = input("Enter Department: ")

    students = manager.search_by_department(department)

    if not students:
        print(f"No students found in department '{department}'.")
        return

    for student in students:
        student.display_student(manager.passing_marks)
        print()


def search_by_average(manager):
    """Display students whose average exceeds the given threshold."""

    print_heading("SEARCH BY AVERAGE MARKS")
    threshold = read_integer("Enter average marks threshold: ")

    students = manager.search_by_average(threshold)

    if not students:
        print(f"No students found with average marks greater than {threshold}.")
        return

    for student in students:
        student.display_student(manager.passing_marks)
        print()


def update_marks(manager):
    """Update the marks of an existing student."""

    print_heading("UPDATE MARKS")
    student_id = read_integer("Enter Student ID: ")

    student = manager.search_student(student_id)

    if student is None:
        print(f"No student found with ID {student_id}.")
        return

    subject1_marks = read_integer("Enter new Subject 1 Marks: ")
    subject2_marks = read_integer("Enter new Subject 2 Marks: ")
    subject3_marks = read_integer("Enter new Subject 3 Marks: ")

    student.update_marks(
        subject1_marks,
        subject2_marks,
        subject3_marks
    )

    print("Marks updated successfully.")


def remove_student(manager):
    """Remove a student by ID."""

    print_heading("REMOVE STUDENT")
    student_id = read_integer("Enter Student ID: ")

    try:
        manager.remove_student(student_id)
        print("Student removed successfully.")
    except StudentRecordError as error:
        print(f"Error: {error}")


def save_records(manager, file_handler):
    """Save current records to a user-specified output file."""

    print_heading("SAVE RECORDS")
    filepath = input("Enter output file path (example: data/output.txt): ")

    file_format = input(
        "Enter output file format (txt/csv/json): "
    ).lower()

    try:
        manager.save_to_file(
            filepath,
            file_handler,
            file_format
        )
        print(f"Records saved successfully to {filepath}")
    except StudentRecordError as error:
        print(f"Error: {error}")

    
def display_menu():
    """Display the main program menu."""

    print("\n" + "=" * 50)
    print("STUDENT RECORD MANAGEMENT".center(50))
    print("=" * 50)
    print("1. Add student")
    print("2. Display all students")
    print("3. Search by student ID")
    print("4. Search by name")
    print("5. Search by department")
    print("6. Search by average marks")
    print("7. Update marks")
    print("8. Remove student")
    print("9. Save records")
    print("0. Exit")
    print("=" * 50)


def main():
    """Run the student record management program."""
    
    try:
        args = parse_arguments()

        manager = StudentManager(args.passing_marks)
        file_handler = FileHandler()

        manager.load_from_file(
            args.file,
            file_handler,
            args.format
        )

        print(
            f"\nRecords loaded successfully from {args.file}"
        )

        while True:
            display_menu()

            choice = input("Enter your choice: ")

            if choice == "1":
                add_student(manager)

            elif choice == "2":
                manager.display_all_students()

            elif choice == "3":
                search_by_id(manager)

            elif choice == "4":
                search_by_name(manager)

            elif choice == "5":
                search_by_department(manager)

            elif choice == "6":
                search_by_average(manager)

            elif choice == "7":
                update_marks(manager)

            elif choice == "8":
                remove_student(manager)

            elif choice == "9":
                save_records(
                    manager,
                    file_handler
                )

            elif choice == "0":
                print("Exiting...")
                break

            else:
                print("Invalid choice. Please try again.")

    # Convert expected failures into readable messages for the user.
    except StudentRecordError as error:
        print(f"Error: {error}")

    except ValueError:
        print("Error: Please enter a valid numeric value.")

    except FileNotFoundError:
        print("Error: The specified file was not found.")

    except OSError as error:
        print(f"File error: {error}")


if __name__ == "__main__":
    main()