import csv
import json
from src.student import Student

class FileHandler:
    """Read and write student records in TXT, CSV, and JSON formats."""

    def save_to_txt(self, students, filepath):
        """Save student records to a TXT file."""

        with open(filepath, "w") as output_file:
            for student in students:
                output_file.write(
                    f"{student.student_id}, {student.name}, "
                    f"{student.department}, {student.semester}, "
                    f"{student.subject1_marks}, {student.subject2_marks}, "
                    f"{student.subject3_marks}\n"
                )

    def load_from_txt(self, filepath):
        """Load student records from a TXT file."""

        students = []

        with open(filepath, "r") as input_file:
            lines = input_file.readlines()

            for line in lines:
                fields = line.strip().split(",")

                for field_index in range(len(fields)):
                    fields[field_index] = fields[field_index].strip()

                student_id = int(fields[0])
                name = fields[1]
                department = fields[2]
                semester = int(fields[3])
                subject1_marks = int(fields[4])
                subject2_marks = int(fields[5])
                subject3_marks = int(fields[6])

                student = Student(
                    student_id,
                    name,
                    department,
                    semester,
                    subject1_marks,
                    subject2_marks,
                    subject3_marks
                )

                students.append(student)

        return students

    def save_to_csv(self, students, filepath): 
        """Save student records to a CSV file with a header row."""

        with open(filepath, "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow([
                "Student_ID",
                "Name",
                "Department",
                "Semester",
                "Subject1",
                "Subject2",
                "Subject3"
            ])
            
            for student in students:
                writer.writerow([
                    student.student_id,
                    student.name,
                    student.department,
                    student.semester,
                    student.subject1_marks,
                    student.subject2_marks,
                    student.subject3_marks
                ])

    def load_from_csv(self, filepath):
        """Load student records from a CSV file and skip its header."""

        students = []

        with open(filepath, "r", newline="") as input_file:
            reader = csv.reader(input_file)

            # The first row is the required CSV column header.
            _header = next(reader, None)
            
            for data in reader:
                student_id = int(data[0])
                name = data[1]
                department = data[2]
                semester = int(data[3])
                subject1_marks = int(data[4])
                subject2_marks = int(data[5])
                subject3_marks = int(data[6])

                student = Student(
                    student_id,
                    name,
                    department,
                    semester,
                    subject1_marks,
                    subject2_marks,
                    subject3_marks
                )

                students.append(student)

        return students

    def save_to_json(self, students, filepath):
        """Save student records to a JSON file."""

        student_records = []

        for student in students:
            student_records.append({
                "student_id": student.student_id,
                "name": student.name,
                "department": student.department,
                "semester": student.semester,
                "subject1_marks": student.subject1_marks,
                "subject2_marks": student.subject2_marks,
                "subject3_marks": student.subject3_marks
            })

        with open(filepath, "w") as output_file:
            json.dump(student_records, output_file, indent=4)

    def load_from_json(self, filepath):
        """Load student records from a JSON file."""

        students = []

        with open(filepath, "r") as input_file:
            student_records = json.load(input_file)

        for record in student_records:
            student = Student(
                record["student_id"],
                record["name"],
                record["department"],
                record["semester"],
                record["subject1_marks"],
                record["subject2_marks"],
                record["subject3_marks"]
            )

            students.append(student)

        return students