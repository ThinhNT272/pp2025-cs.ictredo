# Student Mark Management System

def input_number_of_students():
    return int(input("Enter number of students: "))

def input_student_info():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    dob = input("Enter student DoB (YYYY-MM-DD): ")
    return (student_id, name, dob)

def input_number_of_courses():
    return int(input("Enter number of courses: "))

def input_course_info():
    course_id = input("Enter course ID: ")
    name = input("Enter course name: ")
    return (course_id, name)

def input_course_marks(students, course_id):
    marks = {}
    print(f"Entering marks for course: {course_id}")
    for student_id, student_info in students.items():
        mark = float(input(f"Enter mark for {student_info['name']} (ID: {student_id}): "))
        marks[student_id] = mark
    return marks

def list_students(students):
    print("\nList of students:")
    for student_id, info in students.items():
        print(f"ID: {student_id}, Name: {info['name']}, DoB: {info['dob']}")

def list_courses(courses):
    print("\nList of courses:")
    for course_id, name in courses.items():
        print(f"ID: {course_id}, Name: {name}")

def show_marks_for_course(course_id, marks, students):
    print(f"\nMarks for course {course_id}:")
    if course_id not in marks:
        print("No marks available for this course.")
        return
    for student_id, mark in marks[course_id].items():
        student_name = students[student_id]['name']
        print(f"{student_name} (ID: {student_id}): {mark}")

# Main program
def main():
    students = {}
    courses = {}
    marks = {}

    # Input number of students and their details
    num_students = input_number_of_students()
    for _ in range(num_students):
        student_id, name, dob = input_student_info()
        students[student_id] = {'name': name, 'dob': dob}

    # Input number of courses and their details
    num_courses = input_number_of_courses()
    for _ in range(num_courses):
        course_id, name = input_course_info()
        courses[course_id] = name

    # Input marks for courses
    for course_id in courses:
        marks[course_id] = input_course_marks(students, course_id)

    # Listing options
    while True:
        print("\nOptions:")
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
            print("Invalid choice. Try again.")
