# Input number of student
def input_number_of_students():
    return int(input("Enter number of students in a class: "))

#Input student information
def input_student_info():
    student_id = input("Enter student ID: ")
    student_name = input("Enter student name: ")
    student_dob = input("Enter student DoB (YYYY-MM-DD): ")
    return (student_id, student_name, student_dob)

# Input number of courses
def input_number_of_courses():
    return int(input("Enter number of courses: "))

# Input course information
def input_course_info():
    course_id = input("Enter course ID: ")
    course_name = input("Enter course name: ")
    return (course_id, course_name)

# Select a course, input  marks for student in this course
def input_course_marks(students, course_id):
    marks = {}
    print("Entering marks for course " + course_id + ": ")
    for student_id, student_info in students.items():
        mark = float(input("Enter mark for " + student_info["name"] + " (ID: " + student_id + "): "))
        marks[student_id] = mark
    return marks

# list students
def list_students(students):
    print("List of students: ")
    for student_id, student_info in students.items():
        print("ID: " + student_id + ", Name: " + student_info["name"] + ", DoB: " + student_info["dob"])

# list course
def list_courses(courses):
    print("List of courses: ")
    for course_id, course_name in courses.items():
        print("ID: " + course_id + ", Name: " + course_name)

# show mark of students in course
def show_marks_for_course(course_id, marks, students):
    print("Marks for course" + course_id)
    if course_id not in marks:
        print("No marks")
        return
    for student_id, student_mark in marks[course_id].items():
        student_name = students[student_id]["name"]
        print(student_name + " (ID: " + student_id + "): " + mark)

def main():
    students = {}
    courses = {}
    marks = {}

    number_of_students = input_number_of_students()
    for _ in range(number_of_students):
        student_id, student_name, student_dob = input_student_info()
        students[student_id] = {"name": student_name, "dob": student_dob} 
    
    number_of_courses = input_number_of_courses()
    for _ in range(number_of_courses):
        course_id, course_name = input_course_info()
        courses[course_id] = course_name

    for course_id in courses:
        marks[course_id] = input_course_marks(students, course_id)

    # Options for systems
    while True:
        print("1. List students")
        print("2. List courses")
        print("3. Show marks for a course")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            list_students(students)
        elif choice == 2:
            list_courses(courses)
        elif choice == 3:
            course_id = input("Enter course ID to view marks: ")
            show_marks_for_course(course_id, marks, students)
        elif choice == 4:
            break
        else:
            print("Wrong, try again.")

# Call main function
if __name__ == "__main__":
    main()