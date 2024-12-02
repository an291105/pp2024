# Function to input number of students
def inputNumOfStudents():
    numStudents = int(input("Enter a number of Students :"))
    return numStudents

# Function to input students details
def inputStudentDetails(numStudents):
    students = []  # Initialize the list here, outside the loop
    for _ in range(numStudents):
        studentsId = input("Student's Id:")
        name = input("Student's Name :")
        dob = input(f"Enter Date Of Birth for {name} (DD/MM/YYYY) :")
        students.append((studentsId , name , dob))  # Tuples Stored
    return students

# Function to input number of courses
def inputNumberOfCourses():
    numCourses = int(input("Enter a number of course :"))
    return numCourses

# Function to input course details
def inputCourseDetails(numCourses):
    courses = []  # Initialize the list here, outside the loop
    for _ in range(numCourses):
        coursesId = input("Course's Id: ")
        coursesName = input("Course's Name: ")
        courses.append((coursesId , coursesName))  # Tuples Stored
    return courses

# Function to select student's mark 
def InputStudentMarks(students , courses , markdict):
    courseId = input("Enter a Course Id to input marks : ")
    # Check if course exists
    course = next((course for course in courses if course[0] == courseId ), None)
    if not course:
        print("Can't Found The Course")
        return

    for student in students:  # Loop to input marks for all students
        studentId = student[0]
        marks =  float(input(f"Enter marks for {studentId} ({student[1]}) :"))

        # Store marks in the dictionary
        if courseId not in markdict:  # Check if course already exists
            markdict[courseId] = {}  # Create a new course entry if it doesn't exist

        markdict[courseId][studentId] = marks 

# Function to list all courses
def ListAllCourses(courses):
    print("List Of Courses:")
    for course in courses:
        print(f"Course's Id : {course[0]} , Course's Name : {course[1]}")

# Function to list all students
def ListAllStudents(students):
    print("List of Students: ")
    for student in students:
        print(f"Student's Id : {student[0]} , Student's Name : {student[1]} , Student's Date of Birth : {student[2]}")

# Function to show student's marks
def ShowStudentMarks(courses , markdict):
    courseId = input("Enter a course Id to view student's marks : ")

    # Check if course exists
    course = next((course for course in courses if course[0] == courseId), None)
    if not course:
        print("Cannot find the course")
        return

    if courseId in markdict:
        print(f"Marks for {course[1]} (Course's Id : {courseId}) : ")
        for studentId, marks in markdict[courseId].items():
            print(f"Student's Id : {studentId} , Mark : {marks}")
    else:
        print("No marks entered for this course")

# Main Function
def main():
    numStudents = inputNumOfStudents() 
    students = inputStudentDetails(numStudents)
    
    numCourses = inputNumberOfCourses()  
    courses = inputCourseDetails(numCourses)
    
    markdict = {}

    while True:  # Repeat the menu until the user decides to exit
        print("\nStudent Mark Management System")
        print("1. List Courses")
        print("2. List Students")
        print("3. Input Marks for a Course")
        print("4. Show Student Marks for a Course")
        print("5. Exit")
        
        choice = input("Enter (1-5): ")
        
        if choice == '1':
            ListAllCourses(courses)
        elif choice == '2':
            ListAllStudents(students)
        elif choice == '3':
            InputStudentMarks(students, courses, markdict)
        elif choice == '4':
            ShowStudentMarks(courses, markdict)
        elif choice == '5':
            print("Exit")
            break  # Exit the loop and terminate the program
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()  # Call the main function to start the program
