from student import Student
from attendance_record import AttendanceRecord
from file_storage import FileStorage
from teacher import Teacher
from datetime import date

# Abstraction & Encapsulation: AttendanceManager encapsulates the program's
# core business logic (students, teachers, attendance_records) and provides
# high-level methods (add_student, mark_attendance, authenticate). It uses
# FileStorage to abstract away persistence details.
class AttendanceManager:

    def __init__(self):
        self.file_storage = FileStorage()
        self.students = []
        self.attendance_records = []
        self.teachers = []
        self.load_data()

    # Abstraction
    def load_data(self):
        students_data = self.file_storage.load_data('students.json')
        attendance_data = self.file_storage.load_data('attendance_records.json')
        teachers_data = self.file_storage.load_data('teachers.json')

        for s in students_data:
            # Instantiate Student (inherits from Individual)
            student = Student(s['id'], s['name'], s['class'])
            self.students.append(student)

        for a in attendance_data:
            record = AttendanceRecord(a['student_id'], a['date'], a['status'])
            self.attendance_records.append(record)

        for t in teachers_data:
            # Instantiate Teacher (inherits from Individual)
            teacher = Teacher(t.get('username'), t.get('password'), t.get('name'))
            self.teachers.append(teacher)

        # Ensure at least one teacher exists
        if not self.teachers:
            # Create default Teacher (inherits from Individual)
            default = Teacher('admin', 'admin123', 'Administrator')
            self.teachers.append(default)
            self.save_data()

    def save_data(self):
        student_data = [
            {"id": s.get_id(), "name": s.get_name(), "class": s.get_class_name()}
            for s in self.students
        ]

        attendance_data = [
            {"student_id": r.student_id, "date": r.date, "status": r.status}
            for r in self.attendance_records
        ]

        teachers_data = [
            {"username": t.get_username(), "password": t.password, "name": t.get_name()}
            for t in self.teachers
        ]

        self.file_storage.save_data('students.json', student_data)
        self.file_storage.save_data('attendance_records.json', attendance_data)
        self.file_storage.save_data('teachers.json', teachers_data)

    # Teacher/Auth Methods
    def authenticate(self, username, password):
        for t in self.teachers:
            if t.get_username() == username and t.verify_password(password):
                return t
        return None
    
        teacher = Teacher(username, password, name)
        self.teachers.append(teacher)
        self.save_data()
        print(f"Teacher {name} added successfully.")

    # Student Methods
    # Adding a Student
    def add_student(self, student_id, name, class_name):
        # Normalize inputs for robust comparison: IDs as strings, names/classes stripped and lowercase
        sid_str = str(student_id).strip()
        name_norm = str(name).strip().lower()
        class_norm = str(class_name).strip().lower()

        # prevent duplicate IDs (compare as strings)
        if any(str(s.get_id()).strip() == sid_str for s in self.students):
            print(f"A student with ID {student_id} already exists.")
            return

        # prevent duplicate name+class pair (case-insensitive, trimmed)
        if any(s.get_name().strip().lower() == name_norm and s.get_class_name().strip().lower() == class_norm for s in self.students):
            print(f"A student with name '{name}' in class '{class_name}' already exists.")
            return

        student = Student(student_id, name, class_name)
        self.students.append(student)
        self.save_data()
        print(f"Student {name} added successfully.")

    # View a Student
    def view_students(self):
        return [s.display() for s in self.students]
    
    # Delete a Student's Data
    def delete_student(self, student_id):
        sid_str = str(student_id).strip()
        self.students = [
            student for student in self.students
            if str(student.get_id()).strip() != sid_str]
        self.attendance_records = [
            record for record in self.attendance_records
            if str(record.student_id).strip() != sid_str]
        self.save_data()
        print(f"Student ID {student_id} and associated attendance records deleted successfully.")

    # Attendance Methods
    # Mark Attendance
    def mark_attendance(self, student_id, status):
        sid_str = str(student_id).strip()
        # Validate student exists
        if not any(str(s.get_id()).strip() == sid_str for s in self.students):
            print(f"No student with ID {student_id} found.")
            return

        today = date.today().isoformat()
        # Avoid duplicate marking for same date
        if any(str(r.student_id).strip() == sid_str and r.date == today for r in self.attendance_records):
            print(f"Attendance for Student ID {student_id} already marked for {today}.")
            return

        record = AttendanceRecord(student_id, today, status)
        self.attendance_records.append(record)
        self.save_data()
        print(f"Attendance for Student ID {student_id} marked as {status} on {today}.")

    # View Attendance
    def view_attendance(self):
        return [r.display() for r in self.attendance_records]        