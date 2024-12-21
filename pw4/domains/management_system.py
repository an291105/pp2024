# pw4/domains/management_system.py
import numpy as np
from domains.student import Student
from domains.course import Course

class StudentManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}

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
