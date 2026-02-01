from attendance_manager import AttendanceManager

class MenuSystem:
    def __init__(self):
        self.manager = AttendanceManager()
    
    # Teacher login method
    def login(self):
        print("\n<<--- Teacher Login --->>")
        while True:
            username = input("Username: ")
            password = input("Password: ")

            teacher = self.manager.authenticate(username, password)
            # teacher is a Teacher instance (inherits from Individual)
            if teacher:
                print(f"Welcome, {teacher._name}!")
                return True
            
            print("Invalid credentials. Please try again.\n")

    def start(self):
        # Startup menu: option 1 goes to Teacher Login; option 2 quits program
        while True:
            print("\n|=======================================================================================================|")
            print("|-------------------------------  WELCOME TO SIMPLE ATTENDANCE MANAGER  --------------------------------|")
            print("|=======================================================================================================|")
            print("|                                                                                                       |")
            print("|  1. Teacher Login                                                                                     |")
            print("|                                                                                                       |")
            print("|  2. Exit the Program                                                                                  |")
            print("|                                                                                                       |")
            print("|=======================================================================================================|\n")


            choice = input("Enter choice: ")
            if choice == "1":
                # Run teacher login; if successful, show the main program menu
                if self.login():
                    self.main_menu()
                # After returning from main_menu, continue to startup menu
            elif choice == "2":
                print("Exiting program...")
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")

    def main_menu(self):
        # Main application menu (requires a logged-in teacher)
        while True:
            print("\n|=======================================================================================================|")
            print("|---------------------------------------------  MAIN MENU  ---------------------------------------------|")
            print("|=======================================================================================================|")
            print("|                                                                                                       |")
            print("|  1. Student Management                                                                                |")
            print("|                                                                                                       |")
            print("|  2. Attendance Management                                                                             |")
            print("|                                                                                                       |")
            print("|  3. Logout                                                                                            |")
            print("|                                                                                                       |")
            print("|=======================================================================================================|\n")

            choice = input("Enter choice: ")
            if choice == "1":
                self.student_menu()
            elif choice == "2":
                self.attendance_menu()
            elif choice == "3":
                print("Logging out...")
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")

    def student_menu(self):
        while True:
            print("\n|=========================================================================================================|")
            print("|--------------------------------------------  STUDENT MENU  ---------------------------------------------|")
            print("|=========================================================================================================|")
            print("|                                                                                                         |")
            print("|  1. Add Student                                                                                         |")
            print("|                                                                                                         |")
            print("|  2. View Students                                                                                       |")
            print("|                                                                                                         |")
            print("|  3. Delete Student                                                                                      |")
            print("|                                                                                                         |")
            print("|  4. Back to Main Menu                                                                                   |")
            print("|                                                                                                         |")
            print("|=========================================================================================================|\n")

            choice = input("Enter choice: ")

            if choice == "1":
                student_id = input("Enter ID: ")
                name = input("Enter Name: ")
                class_name = input("Enter Class: ")
                self.manager.add_student(student_id, name, class_name)

            elif choice == "2":
                students = self.manager.view_students()
                for s in students:
                    print(s)

            elif choice == "3":
                student_id = input("Enter Student ID to delete: ")
                self.manager.delete_student(student_id)

            elif choice == "4":
                break
            else:
                print("Invalid choice. Please enter 1, 2, 3, or 4.")

    def attendance_menu(self):
        while True:
            print("\n|=========================================================================================================|")
            print("|-------------------------------------------  ATTENDANCE MENU  -------------------------------------------|")
            print("|=========================================================================================================|")
            print("|                                                                                                         |")
            print("|  1. Mark Attendance                                                                                     |")
            print("|                                                                                                         |")
            print("|  2. View Attendance                                                                                     |")
            print("|                                                                                                         |")
            print("|  3. Back to Main Menu                                                                                   |")
            print("|                                                                                                         |")
            print("|=========================================================================================================|\n")

            choice = input("Enter choice: ")

            if choice == "1":
                student_id = input("Enter Student ID: ")
                status = input("Enter Status (Present/Absent): ")
                self.manager.mark_attendance(student_id, status)

            elif choice == "2":
                records = self.manager.view_attendance()
                for r in records:
                    print(r)

            elif choice == "3":
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")