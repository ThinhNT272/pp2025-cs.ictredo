class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob

    def display(self):
        print(f"ID: {self.student_id}, Name: {self.name}, DoB: {self.dob}")


class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name

    def display(self):
        print(f"ID: {self.course_id}, Name: {self.name}")


class Mark:
    def __init__(self):
        self.marks = {}  # {course_id: {student_id: mark}}

    def input_marks(self, students, course_id):
        if course_id not in self.marks:
            self.marks[course_id] = {}
        print(f"Entering marks for course: {course_id}")
        for student in students:
            mark = float(input(f"Enter mark for {student.name} (ID: {student.student_id}): "))
            self.marks[course_id][student.student_id] = mark

    def show_marks(self, course_id, students):
        print(f"\nMarks for course {course_id}:")
        if course_id not in self.marks:
            print("No marks available for this course.")
            return
        for student in students:
            mark = self.marks[course_id].get(student.student_id, "N/A")
            print(f"{student.name} (ID: {student.student_id}): {mark}")


class StudentMarkSystem:
    def __init__(self):
        self.students = []  # List of Student objects
        self.courses = []   # List of Course objects
        self.marks = Mark()

    def input_students(self):
        num_students = int(input("Enter number of students: "))
        for _ in range(num_students):
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            dob = input("Enter student DoB (YYYY-MM-DD): ")
            self.students.append(Student(student_id, name, dob))

    def input_courses(self):
        num_courses = int(input("Enter number of courses: "))
        for _ in range(num_courses):
            course_id = input("Enter course ID: ")
            name = input("Enter course name: ")
            self.courses.append(Course(course_id, name))

    def list_students(self):
        print("\nList of students:")
        for student in self.students:
            student.display()

    def list_courses(self):
        print("\nList of courses:")
        for course in self.courses:
            course.display()

    def input_marks(self):
        course_id = input("Enter course ID to input marks: ")
        course_ids = [course.course_id for course in self.courses]
        if course_id not in course_ids:
            print("Invalid course ID!")
            return
        self.marks.input_marks(self.students, course_id)

    def show_marks(self):
        course_id = input("Enter course ID to view marks: ")
        self.marks.show_marks(course_id, self.students)

    def menu(self):
        while True:
            print("\nOptions:")
            print("1. Input students")
            print("2. Input courses")
            print("3. List students")
            print("4. List courses")
            print("5. Input marks for a course")
            print("6. Show marks for a course")
            print("7. Exit")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                self.input_students()
            elif choice == 2:
                self.input_courses()
            elif choice == 3:
                self.list_students()
            elif choice == 4:
                self.list_courses()
            elif choice == 5:
                self.input_marks()
            elif choice == 6:
                self.show_marks()
            elif choice == 7:
                break
            else:
                print("Invalid choice. Try again.")

if __name__ == "__main__":
    system = StudentMarkSystem()
    system.menu()
