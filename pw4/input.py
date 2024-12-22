# input.py

import math
import numpy as np
import curses

class Student:
    def __init__(self, name, student_id, dob):
        self.name = name
        self.student_id = student_id
        self.dob = dob

class Course:
    def __init__(self, name, course_id):
        self.name = name
        self.course_id = course_id

class StudentManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}

    def input_num_of_students(self):
        num_students = int(input("Enter number of students: "))
        return num_students

    def input_student_details(self, num_students):
        for _ in range(num_students):
            name = input("Enter student name: ")
            student_id = input("Enter student ID: ")
            dob = input("Enter student DOB: ")
            self.students.append(Student(name, student_id, dob))

    def input_num_of_courses(self):
        num_courses = int(input("Enter number of courses: "))
        return num_courses

    def input_course_details(self, num_courses):
        for _ in range(num_courses):
            name = input("Enter course name: ")
            course_id = input("Enter course ID: ")
            self.courses.append(Course(name, course_id))

    def input_student_marks(self, stdscr):
        stdscr.addstr("Enter course's ID to input marks: ")
        stdscr.refresh()
        curses.echo()
        course_id = stdscr.getstr().decode("utf-8")
        curses.noecho()

        course = next((course for course in self.courses if course.course_id == course_id), None)
        if not course:
            stdscr.addstr("Course not found.\n")
            stdscr.addstr("Press any key to return to the menu.")
            stdscr.refresh()
            stdscr.getch()
            return

        for student in self.students:
            while True:
                try:
                    stdscr.addstr(f"\nEnter marks for {student.name} ({student.student_id}): ")
                    stdscr.refresh()
                    curses.echo()
                    mark = float(stdscr.getstr().decode("utf-8"))
                    curses.noecho()

                    if 0.0 <= mark <= 100.0:
                        mark = math.floor(mark * 10) / 10
                        if course_id not in self.marks:
                            self.marks[course_id] = {}
                        self.marks[course_id][student.student_id] = mark
                        break
                    else:
                        stdscr.addstr("Invalid mark! Marks must be between 0 and 100.\n")
                except ValueError:
                    stdscr.addstr("Invalid input! Please enter a numeric value.\n")

    def calculate_gpa(self):
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
        gpa_dict = self.calculate_gpa()
        stdscr.addstr("Student GPA:\n")
        for student_id, gpa in gpa_dict.items():
            student_name = next((s.name for s in self.students if s.student_id == student_id), "Unknown Student")
            stdscr.addstr(f"- {student_name} ({student_id}): {gpa}\n")
        stdscr.refresh()

    def show_student_details(self, stdscr):
        stdscr.addstr("Enter student's ID to view details: ")
        stdscr.refresh()
        curses.echo()
        student_id = stdscr.getstr().decode("utf-8")
        curses.noecho()

        student = next((student for student in self.students if student.student_id == student_id), None)
        if not student:
            stdscr.addstr("Student not found.\n")
            stdscr.addstr("Press any key to return to the menu.")
            stdscr.refresh()
            stdscr.getch()
            return

        stdscr.addstr(f"\nName: {student.name}\n")
        stdscr.addstr(f"ID: {student.student_id}\n")
        stdscr.addstr(f"DOB: {student.dob}\n")

        stdscr.addstr("Courses and Marks:\n")
        for course_id, marks in self.marks.items():
            if student_id in marks:
                course_name = next((c.name for c in self.courses if c.course_id == course_id), "Unknown Course")
                stdscr.addstr(f"- {course_name} (ID: {course_id}): {marks[student_id]}\n")

        stdscr.refresh()
        stdscr.addstr("\nPress any key to return to the menu.")
        stdscr.refresh()
        stdscr.getch()

    def display_menu(self, stdscr):
        stdscr.clear()
        stdscr.addstr("Student Management System\n")
        stdscr.addstr("1. List Courses\n")
        stdscr.addstr("2. List Students\n")
        stdscr.addstr("3. Input Marks\n")
        stdscr.addstr("4. Show Marks\n")
        stdscr.addstr("5. Show GPA\n")
        stdscr.addstr("6. Show Student Details\n")
        stdscr.addstr("7. Sort Students by GPA\n")
        stdscr.addstr("8. Exit\n")
        stdscr.addstr("Enter your choice: ")
        stdscr.refresh()

        choice = stdscr.getkey()
        return choice

    def menu(self, stdscr):
        while True:
            stdscr.clear()
            choice = self.display_menu(stdscr)

            if choice == "1":
                stdscr.clear()
                self.list_all_courses(stdscr)
                stdscr.addstr("\nPress any key to return to the menu.")
                stdscr.refresh()
                stdscr.getch()

            elif choice == "2":
                stdscr.clear()
                self.list_all_students(stdscr)
                stdscr.addstr("\nPress any key to return to the menu.")
                stdscr.refresh()
                stdscr.getch()

            elif choice == "3":
                stdscr.clear()
                self.input_student_marks(stdscr)
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
                self.show_student_gpa(stdscr)
                stdscr.addstr("\nPress any key to return to the menu.")
                stdscr.refresh()
                stdscr.getch()

            elif choice == "6":
                stdscr.clear()
                self.show_student_details(stdscr)
                stdscr.addstr("\nPress any key to return to the menu.")
                stdscr.refresh()
                stdscr.getch()

            elif choice == "7":
                stdscr.clear()
                self.sort_students_by_gpa(stdscr)
                stdscr.addstr("\nPress any key to return to the menu.")
                stdscr.refresh()
                stdscr.getch()

            elif choice == "8":
                break

            else:
                stdscr.clear()
                stdscr.addstr("Invalid choice. Please try again.\n")
                stdscr.addstr("\nPress any key to return to the menu.")
                stdscr.refresh()
                stdscr.getch()

