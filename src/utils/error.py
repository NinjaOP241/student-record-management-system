class StudentRecordError(Exception):
    """Base exception for student record management errors."""
    pass

class ConflictError(StudentRecordError):
    """Raised when an operation conflicts with existing data."""
    pass

class NotFoundError(StudentRecordError):
    """Raised when a requested student does not exist."""
    pass

class InvalidInputError(StudentRecordError):
    """Raised when user-provided input is invalid."""
    pass