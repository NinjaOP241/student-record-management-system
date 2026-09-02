from src.utils.error import ConflictError, InvalidInputError, NotFoundError

class StudentManager:
    """Manage a collection of Student objects using one passing-mark rule."""

    def __init__(self, passing_marks=40):
        self.students = []
        self.passing_marks = passing_marks

    def add_student(self, student):
        """Add a Student object to the collection, ensuring no duplicate IDs."""
        existing_student = self.search_student(student.student_id)

        # Student IDs identify records, so duplicates must be rejected.
        if existing_student:
            raise ConflictError(
                f"Student with ID {student.student_id} already exists"
            )

        self.students.append(student)

    def search_student(self, student_id):
        """Return the student with the given ID, or None if not found."""
        for student in self.students:
            if student.student_id == student_id:
                return student

        return None

    def search_by_name(self, student_name):
        """Return students matching the given name."""
        matching_students = []

        for student in self.students:
            if student.name.lower() == student_name.lower():
                matching_students.append(student)

        return matching_students
    
    def search_by_department(self, department):
        """Return students belonging to the given department."""
        matching_students = []

        for student in self.students:
            if student.department.lower() == department.lower():
                matching_students.append(student)

        return matching_students

    def search_by_average(self, threshold):
        """Return students whose average marks exceed the threshold."""
        matching_students = []

        for student in self.students:
            if student.calculate_average() > threshold:
                matching_students.append(student)

        return matching_students

    def remove_student(self, student_id):
        """Remove the student with the given ID."""
        student = self.search_student(student_id)

        if student is None:
            raise NotFoundError(
                f"Student with ID {student_id} not found"
            )

        self.students.remove(student)

    def display_all_students(self):
        """Display all students currently managed."""
        if not self.students:
            print("No student records found.")
            return
    
        for student in self.students:
            student.display_student(self.passing_marks)
            print()

    def load_from_file(self, filepath, file_handler, file_format):
        """Load students from the selected file format."""

        # Select the reader based on the format supplied by the user.
        if file_format == "txt":
            students = file_handler.load_from_txt(filepath)

        elif file_format == "csv":
            students = file_handler.load_from_csv(filepath)

        elif file_format == "json":
            students = file_handler.load_from_json(filepath)

        else:
            raise InvalidInputError("Unsupported file format")

        for student in students:
            self.add_student(student)

    def save_to_file(self, filepath, file_handler, file_format):
        """Save all managed students using the selected file format."""
        
        # Select the writer based on the format supplied by the user.
        if file_format == "txt":
            file_handler.save_to_txt(self.students, filepath)

        elif file_format == "csv":
            file_handler.save_to_csv(self.students, filepath)

        elif file_format == "json":
            file_handler.save_to_json(self.students, filepath)

        else:
            raise InvalidInputError("Unsupported file format")