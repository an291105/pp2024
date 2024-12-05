class Student:
    def __init__(self , student_id , name , dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob

class Course:
    def __init__(self , course_id , name):
        self.course_id = course_id
        self.name = name

class StudentManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}
#Function to input number of student
    def input_num_of_students(self):
        num_students = int(input("Enter number of students :"))
        return num_students
#Function to input student's details
    def input_student_details(self , num_students):
        for _ in range(num_students):
            student_id = input("Student's Id: ")
            name = input("Student's Name: ")
            dob = input(f"Enter date of birth for {name} (DD/MM/YYYY) :")
            self.students.append(Student(student_id, name , dob))
#Function to input number of courses
    def input_num_of_courses(self):
        num_courses = int(input("Enter number of courses: "))
        return num_courses
#Function to input course details
    def input_course_details(self , num_courses):
        for _ in range(num_courses):
            course_id = input("Course's Id: ")
            name = input("Course's name:")
            self.courses.append(Course(course_id, name))
#Function to input mark for student
    def input_student_marks(self):
        course_id = input("Enter course's id to input student's mark: ")
        course = next((course for course in self.courses if course.course_id == course_id), None)
        if not course:
            print("Course not found.")
            return 
        
        for student in self.students:
            marks = float(input(f"Enter a mark for {student.student_id} ({student.name})"))
            if course_id not in self.marks:
                self.marks[course_id] = {}
                self.marks[course_id][student.student_id] = marks
#Function to list all courses
    def list_all_courses(self):
        print("List of courses:")
        for course in self.courses:
            print(f"Course's Id : {course.course_id} , Course's name : {course.name}")
#Function to list all students
    def list_all_students(self):
        print("List of students: ")
        for student in self.students:
            print(f"Student's Id : {student.student_id} , Student's name : {student.name} ")
#Function to show student marks
    def show_student_marks(self):
        course_id = input("Enter Course's ID to view student's marks :")
        course = next((course for course in self.courses if course.course_id == course_id), None)
        if not course:
            print("Course not found!")
            return
        if course_id in self.marks:
            print(f"Marks for {course.name} ({course.course_id})")
            for student_id , marks in self.marks[course_id].items():
                student = next((student for student in self.students if student.student_id == student_id), None)
                print(f"Student's ID : {student_id} , Student's Name : {student.name} , Marks : {marks}")
        else:
            print("No marks entered")

    def menu(self):
        while True:
            print("Student's Mark Management System")
            print("1. View List Courses")
            print("2. View List Students")
            print("3. Input marks for a course")
            print("4. Show student's marks for a course")
            print("5. Exit")

            choice = input("Enter your choice (1-5) :")

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
                print("Invalid Choice , Please enter (1-5)")

if __name__ == "__main__": #This line is used to check if the script is being run directly or being imported as a module in another script.
    smms = StudentManagementSystem()
    num_students = smms.input_num_of_students()
    smms.input_student_details(num_students)
    num_courses = smms.input_num_of_courses()
    smms.input_course_details(num_courses)
    smms.menu()
            



