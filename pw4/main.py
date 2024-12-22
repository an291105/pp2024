
import curses
from input import StudentManagementSystem

if __name__ == "__main__":
    smms = StudentManagementSystem()
    num_students = int(input("Enter number of students: "))  # Enter the number of students
    smms.input_student_details(num_students)
    num_courses = int(input("Enter number of courses: "))  # Enter the number of courses
    smms.input_course_details(num_courses)
    curses.wrapper(smms.menu)  # Run the curses menu