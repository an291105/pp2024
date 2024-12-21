# pw4/input.py
def input_num_of_students():
    num_students = int(input("Enter number of students: "))
    return num_students

def input_student_details(num_students, students):
    for _ in range(num_students):
        name = input("Enter student name: ")
        student_id = input("Enter student ID: ")
        dob = input("Enter student DOB: ")
        students.append(Student(name, student_id, dob))

def input_num_of_courses():
    num_courses = int(input("Enter number of courses: "))
    return num_courses

def input_course_details(num_courses, courses):
    for _ in range(num_courses):
        name = input("Enter course name: ")
        course_id = input("Enter course ID: ")
        courses.append(Course(name, course_id))
