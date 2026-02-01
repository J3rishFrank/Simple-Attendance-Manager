class AttendanceRecord:
    def __init__(self, student_id, date, status):
        self.student_id = student_id
        self.date = date
        self.status = status  # Present or Absent

    # Polymorphism: provides a display() method (same concept used by Student/Teacher)
    # so records and people can be displayed interchangeably by calling display().
    def display(self):
        return f"Student ID: {self.student_id}, Date: {self.date}, Status: {self.status}"