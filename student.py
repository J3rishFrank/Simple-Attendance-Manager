from individual import Individual

# Encapsulation: Student keeps its internal data (_student_id, _class_name) protected
# and provides methods (get_id, get_name, get_class_name) to read them.
# Inheritance: Student subclasses Individual to reuse the common interface.
class Student(Individual):  # inherits from Individual (is-a Individual)
    def __init__(self, student_id, name, class_name):
        super().__init__(name)
        self._student_id = student_id   # Protected attribute
        self._class_name = class_name   # Protected attribute

    def get_id(self):
        return self._student_id
    
    def get_name(self):
        return self._name
    
    def get_class_name(self):
        return self._class_name
    
    # Polymorphism: Student implements the Individual.display() interface allowing
    # different individual objects to be displayed using the same method name.
    def display(self):
        return f"ID: {self._student_id}, Name: {self._name}, Class: {self._class_name}"