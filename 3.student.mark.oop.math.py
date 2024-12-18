import math
import numpy as np
import curses

class Student:
    def __init__(self, student_id, name, dob):
        # Initialize the Student class with ID, name, date of birth, and GPA
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.gpa = 0.0  # Default GPA is set to 0.0

class Course:
    def __init__(self, course_id, name):
        # Initialize the Course class with ID and name
        self.course_id = course_id
        self.name = name

class StudentManagementSystem:
    def __init__(self):
        # Initialize the StudentManagementSystem with lists for students, courses, and a dictionary for marks
        self.students = []
        self.courses = []
        self.marks = {}

    def input_num_of_students(self):
        # Function to input the number of students
        num_students = int(input("Enter number of students: "))
        return num_students

    def input_student_details(self, num_students):
        # Function to input details of each student
        for _ in range(num_students):
            student_id = input("Student's Id: ")
            name = input("Student's Name: ")
            dob = input(f"Enter date of birth for {name} (DD/MM/YYYY): ")
            self.students.append(Student(student_id, name, dob))

    def input_num_of_courses(self):
        # Function to input the number of courses
        num_courses = int(input("Enter number of courses: "))
        return num_courses

    def input_course_details(self, num_courses):
        # Function to input details of each course
        for _ in range(num_courses):
            course_id = input("Course's Id: ")
            name = input("Course's name: ")
            self.courses.append(Course(course_id, name))

    def input_student_marks(self):
        # Function to input marks for each student in a specific course
        course_id = input("Enter course's id to input student's mark: ")
        course = next((course for course in self.courses if course.course_id == course_id), None)
        if not course:
            print("Course not found.")
            return 

        for student in self.students:
            marks = float(input(f"Enter a mark for {student.student_id} ({student.name}): "))
            marks = math.floor(marks * 10) / 10  # Round down to 1-digit decimal
            if course_id not in self.marks:
                self.marks[course_id] = {}
            self.marks[course_id][student.student_id] = marks
        
        # Recalculate GPA for each student after entering marks
        self.calculate_gpa()

    def calculate_gpa(self):
        # Function to calculate GPA for each student
        for student in self.students:
            marks_array = []
            credits_array = []
            for course_id, marks_dict in self.marks.items():
                if student.student_id in marks_dict:
                    marks_array.append(marks_dict[student.student_id])
                    credits_array.append(1)  # Assuming each course has 1 credit
            if marks_array and credits_array:
                gpa = np.sum(np.array(marks_array) * np.array(credits_array)) / np.sum(np.array(credits_array))
                student.gpa = gpa

    def list_all_courses(self):
        # Function to list all courses
        print("List of courses:")
        for course in self.courses:
            print(f"Course's Id: {course.course_id}, Course's name: {course.name}")

    def list_all_students(self):
        # Function to list all students
        print("List of students:")
        for student in self.students:
            print(f"Student's Id: {student.student_id}, Student's name: {student.name}")

    def show_student_marks(self):
        # Function to show marks for students in a specific course
        course_id = input("Enter Course's ID to view student's marks: ")
        course = next((course for course in self.courses if course.course_id == course_id), None)
        if not course:
            print("Course not found!")
            return
        if course_id in self.marks:
            print(f"Marks for {course.name} ({course.course_id}):")
            for student_id, marks in self.marks[course_id].items():
                student = next((student for student in self.students if student.student_id == student_id), None)
                if student:
                    print(f"Student's ID: {student_id}, Student's Name: {student.name}, Marks: {marks}")
        else:
            print("No marks entered")

    def decorate_menu(self, stdscr):
        # Function to set up the curses menu
        stdscr.clear()
        stdscr.addstr(0, 0, "Student Management System")
        stdscr.addstr(2, 0, "1. View List Courses")
        stdscr.addstr(3, 0, "2. View List Students")
        stdscr.addstr(4, 0, "3. Input marks for a course")
        stdscr.addstr(5, 0, "4. Show student's marks for a course")
        stdscr.addstr(6, 0, "5. Exit")
        stdscr.refresh()
        choice = stdscr.getkey()
        return choice

    def menu(self):
        # Function to wrap the curses menu
        try:
            curses.wrapper(self.curses_menu)
        except Exception as e:
            print(f"An error occurred: {e}")

    def curses_menu(self, stdscr):
        # Curses menu loop
        while True:
            choice = self.decorate_menu(stdscr)

            if choice == '1':
                self.list_all_courses()
            elif choice == '2':
                self.list_all_students()
            elif choice == '3':
                self.input_student_marks()
            elif choice == '4':
                self.show_student_marks()
            elif choice == '5':
                print("OK!")
                break
            else:
                print("Invalid Choice, Please enter (1-5)")

if __name__ == "__main__":
    smms = StudentManagementSystem()
    num_students = smms.input_num_of_students()
    smms.input_student_details(num_students)
    num_courses = smms.input_num_of_courses()
    smms.input_course_details(num_courses)
    smms.menu()
