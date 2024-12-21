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