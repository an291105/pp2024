import curses
import platform
import math
import numpy as np

class Student:
    def __init__(self, name, student_id, dob):
        # Initialize the Student class with name, student ID, and date of birth
        self.name = name
        self.student_id = student_id
        self.dob = dob

class Course:
    def __init__(self, name, course_id):
        # Initialize the Course class with name and course ID
        self.name = name
        self.course_id = course_id

class StudentManagementSystem:
    def __init__(self):
        # Initialize the StudentManagementSystem with empty lists for students and courses, and an empty dictionary for marks
        self.students = []
        self.courses = []
        self.marks = {}

    def input_num_of_students(self):
        # Prompt the user to enter the number of students
        num_students = int(input("Enter number of students: "))
        return num_students

    def input_student_details(self, num_students):
        # Prompt the user to enter details for each student
        for _ in range(num_students):
            name = input("Enter student name: ")
            student_id = input("Enter student ID: ")
            dob = input("Enter student DOB: ")
            self.students.append(Student(name, student_id, dob))

    def input_num_of_courses(self):
        # Prompt the user to enter the number of courses
        num_courses = int(input("Enter number of courses: "))
        return num_courses

    def input_course_details(self, num_courses):
        # Prompt the user to enter details for each course
        for _ in range(num_courses):
            name = input("Enter course name: ")
            course_id = input("Enter course ID: ")
            self.courses.append(Course(name, course_id))

    def input_student_marks(self, stdscr):
        # Prompt the user to enter the course ID to input marks
        stdscr.addstr("Enter course's ID to input marks: ")
        stdscr.refresh()
        curses.echo()
        course_id = stdscr.getstr().decode("utf-8")  # Get string from curses
        curses.noecho()

        # Check if the course exists
        course = next((course for course in self.courses if course.course_id == course_id), None)
        if not course:
            stdscr.addstr("Course not found.\n")
            stdscr.addstr("Press any key to return to the menu.")
            stdscr.refresh()
            stdscr.getch()
            return

        # Input marks for each student
        for student in self.students:
            while True:
                try:
                    stdscr.addstr(f"\nEnter marks for {student.name} ({student.student_id}): ")
                    stdscr.refresh()
                    curses.echo()
                    mark = float(stdscr.getstr().decode("utf-8"))  # Get mark
                    curses.noecho()

                    # Check if the mark is within the valid range (0 to 100)
                    if 0.0 <= mark <= 100.0:
                        mark = math.floor(mark * 10) / 10  # Round down to 1 decimal place
                        if course_id not in self.marks:
                            self.marks[course_id] = {}
                        self.marks[course_id][student.student_id] = mark
                        break  # Exit loop if input is valid
                    else:
                        stdscr.addstr("Invalid mark! Marks must be between 0 and 100.\n")
                except ValueError:
                    stdscr.addstr("Invalid input! Please enter a numeric value.\n")

    def calculate_gpa(self):
        # Calculate GPA for each student
        gpa_dict = {}
        for student in self.students:
            student_marks = []
            for course_id in self.marks:
                if student.student_id in self.marks[course_id]:
                    student_marks.append(self.marks[course_id][student.student_id])
            if student_marks:
                gpa = np.mean(student_marks)
                gpa_dict[student.student_id] = round(gpa, 2)
        return gpa_dict

    def show_student_gpa(self, stdscr):
        # Display the GPA of students
        gpa_dict = self.calculate_gpa()
        stdscr.addstr("Student GPA:\n")
        for student_id, gpa in gpa_dict.items():
            student_name = next((s.name for s in self.students if s.student_id == student_id), "Unknown Student")
            stdscr.addstr(f"- {student_name} ({student_id}): {gpa}\n")
        stdscr.refresh()

    def list_all_courses(self, stdscr):
        # Display the list of courses
        stdscr.addstr("List of courses:\n")
        for course in self.courses:
            stdscr.addstr(f"- {course.name} (ID: {course.course_id})\n")
        stdscr.refresh()

    def list_all_students(self, stdscr):
        # Display the list of students
        stdscr.addstr("List of students:\n")
        for student in self.students:
            stdscr.addstr(f"- {student.name} (ID: {student.student_id})\n")
        stdscr.refresh()

    def show_student_marks(self, stdscr):
        # Display the marks of students
        stdscr.addstr("Student Marks:\n")
        for course_id, student_marks in self.marks.items():
            course_name = next((c.name for c in self.courses if c.course_id == course_id), "Unknown Course")
            stdscr.addstr(f"\nCourse: {course_name} (ID: {course_id})\n")
            for student_id, mark in student_marks.items():
                student_name = next((s.name for s in self.students if s.student_id == student_id), "Unknown Student")
                stdscr.addstr(f"- {student_name} ({student_id}): {mark}\n")
        stdscr.refresh()

    def display_menu(self, stdscr):
        # Display the menu
        stdscr.clear()
        stdscr.addstr("Student Management System\n")
        stdscr.addstr("1. List Courses\n")
        stdscr.addstr("2. List Students\n")
        stdscr.addstr("3. Input Marks\n")
        stdscr.addstr("4. Show Marks\n")
        stdscr.addstr("5. Show GPA\n")
        stdscr.addstr("6. Exit\n")
        stdscr.addstr("Enter your choice: ")
        stdscr.refresh()

        # Get the user's choice
        choice = stdscr.getkey()
        return choice

    def menu(self, stdscr):
        while True:
            stdscr.clear()  # Clear the screen
            choice = self.display_menu(stdscr)  # Display the menu and get the user's choice

            if choice == "1":
                stdscr.clear()
                self.list_all_courses(stdscr)
                stdscr.addstr("\nPress any key to return to the menu.")
                stdscr.refresh()
                stdscr.getch()  # Wait for a key press

            elif choice == "2":
                stdscr.clear()
                self.list_all_students(stdscr)
                stdscr.addstr("\nPress any key to return to the menu.")
                stdscr.refresh()
                stdscr.getch()

            elif choice == "3":
                stdscr.clear()
                self.input_student_marks(stdscr)  # Input marks
                stdscr.addstr("\nMarks have been entered. Press any key to return.")
                stdscr.refresh()
                stdscr.getch()

            elif choice == "4":
                stdscr.clear()
                self.show_student_marks(stdscr)
                stdscr.addstr("\nPress any key to return to the menu.")
                stdscr.refresh()
                stdscr.getch()

            elif choice == "5":
                stdscr.clear()
                self.show_student_gpa(stdscr)  # Show GPA
                stdscr.addstr("\nPress any key to return to the menu.")
                stdscr.refresh()
                stdscr.getch()

            elif choice == "6":
                break  # Exit the program

            else:
                stdscr.clear()
                stdscr.addstr("Invalid choice. Please try again.\n")
                stdscr.addstr("\nPress any key to return to the menu.")
                stdscr.refresh()
                stdscr.getch()

if __name__ == "__main__":
    smms = StudentManagementSystem()
    num_students = int(input("Enter number of students: "))  # Enter the number of students
    smms.input_student_details(num_students)
    num_courses = int(input("Enter number of courses: "))  # Enter the number of courses
    smms.input_course_details(num_courses)
    curses.wrapper(smms.menu)  # Run the curses menu
