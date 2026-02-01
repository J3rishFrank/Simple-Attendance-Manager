class Classroom:
    def __init__(self,class_name):
        self.class_name = class_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)
    
    def get_students(self):
        return self.students