# pw4/output.py
import curses
import math

def input_student_marks(stdscr, students, courses, marks):
    stdscr.addstr("Enter course's ID to input marks: ")
    stdscr.refresh()
    curses.echo()
    course_id = stdscr.getstr().decode("utf-8")  # Get string from curses
    curses.noecho()

    course = next((course for course in courses if course.course_id == course_id), None)
    if not course:
        stdscr.addstr("Course not found.\n")
        stdscr.addstr("Press any key to return to the menu.")
        stdscr.refresh()
        stdscr.getch()
        return

    for student in students:
        while True:
            try:
                stdscr.addstr(f"\nEnter marks for {student.name} ({student.student_id}): ")
                stdscr.refresh()
                curses.echo()
                mark = float(stdscr.getstr().decode("utf-8"))  # Get mark
                curses.noecho()

                if 0.0 <= mark <= 100.0:
                    mark = math.floor(mark * 10) / 10  # Round down to 1 decimal place
                    if course_id not in marks:
                        marks[course_id] = {}
                    marks[course_id][student.student_id] = mark
                    break  # Exit loop if input is valid
                else:
                    stdscr.addstr("Invalid mark! Marks must be between 0 and 100.\n")
            except ValueError:
                stdscr.addstr("Invalid input! Please enter a numeric value.\n")

def list_all_courses(stdscr, courses):
    stdscr.addstr("List of courses:\n")
    for course in courses:
        stdscr.addstr(f"- {course.name} (ID: {course.course_id})\n")
    stdscr.refresh()

def list_all_students(stdscr, students):
    stdscr.addstr("List of students:\n")
    for student in students:
        stdscr.addstr(f"- {student.name} (ID: {student.student_id})\n")
    stdscr.refresh()

def show_student_marks(stdscr, students, courses, marks):
    stdscr.addstr("Student Marks:\n")
    for course_id, student_marks in marks.items():
        course_name = next((c.name for c in courses if c.course_id == course_id), "Unknown Course")
        stdscr.addstr(f"\nCourse: {course_name} (ID: {course_id})\n")
        for student_id, mark in student_marks.items():
            student_name = next((s.name for s in students if s.student_id == student_id), "Unknown Student")
            stdscr.addstr(f"- {student_name} ({student_id}): {mark}\n")
    stdscr.refresh()
