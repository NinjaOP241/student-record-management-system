class Student:
    """Represent one student's personal details and subject marks."""

    def __init__(self, student_id, name, department, semester,
                 subject1_marks, subject2_marks, subject3_marks):
        self.student_id = student_id
        self.name = name
        self.department = department
        self.semester = semester
        self.subject1_marks = subject1_marks
        self.subject2_marks = subject2_marks
        self.subject3_marks = subject3_marks
        
    def calculate_total(self):
        """Return the total marks of the three subjects."""
        return self.subject1_marks + self.subject2_marks + self.subject3_marks

    def calculate_average(self):    
        """Return the average marks of the three subjects."""
        return self.calculate_total() / 3

    def get_result(self, passing_marks):
        """Return Pass if all subjects meet the passing mark."""
        # A student must meet the common passing mark in every subject.
        if (
            self.subject1_marks >= passing_marks
            and self.subject2_marks >= passing_marks
            and self.subject3_marks >= passing_marks
        ):
            return "Pass"

        return "Fail"

    def update_marks(self, subject1_marks=None, subject2_marks=None, subject3_marks=None):
        """Update the marks provided by the caller."""
        # None means that the existing mark for that subject should remain unchanged.
        if subject1_marks is not None:
            self.subject1_marks = subject1_marks

        if subject2_marks is not None:
            self.subject2_marks = subject2_marks

        if subject3_marks is not None:
            self.subject3_marks = subject3_marks

    def display_student(self, passing_marks):
        """Display the student's details, marks, average, and result."""
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Department:", self.department)
        print("Semester:", self.semester)
        print("Subject 1 Marks:", self.subject1_marks)
        print("Subject 2 Marks:", self.subject2_marks)
        print("Subject 3 Marks:", self.subject3_marks)
        print("Total Marks:", self.calculate_total())
        print(f"Average Marks: {self.calculate_average():.2f}")
        print("Result:", self.get_result(passing_marks))