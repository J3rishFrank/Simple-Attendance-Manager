from individual import Individual

# Inheritance & Encapsulation: Teacher extends Individual and encapsulates credentials.
# The password is stored internally and accessed via verify_password().
class Teacher(Individual):  # inherits from Individual (is-a Individual)
    def __init__(self, username, password, name):
        super().__init__(name)
        self.username = username
        self.password = password

    def verify_password(self, password):
        return self.password == password

    def get_username(self):
        return self.username

    def get_name(self):
        return self._name

    def display(self):
        return f"Teacher: {self._name} (username: {self.username})"
