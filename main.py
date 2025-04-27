# main.py

from student import Student
from faculty import Faculty
from course import Course
import utils

students = utils.load_students_from_csv()
faculty_list = utils.load_faculty_from_csv()
courses = utils.load_courses_from_csv()

def find_student(student_id):
    for s in students:
        if s.student_id == student_id:
            return s
    return None

def find_faculty(faculty_id):
    for f in faculty_list:
        if f.faculty_id == faculty_id:
            return f
    return None

def find_course(course_id):
    for c in courses:
        if c.course_id == course_id:
            return c
    return None

def add_student():
    sid = input("Enter student ID: ")
    name = input("Enter student name: ")
    major = input("Enter student major: ")
    if find_student(sid):
        print("Student ID already exists!")
    else:
        student = Student(sid, name, major)
        students.append(student)
        utils.save_student_to_csv(student)
        print("Student added.")

def add_faculty():
    fid = input("Enter faculty ID: ")
    name = input("Enter faculty name: ")
    dept = input("Enter faculty department: ")
    if find_faculty(fid):
        print("Faculty ID already exists!")
    else:
        new_faculty = Faculty(fid, name, dept)
        faculty_list.append(new_faculty)
        utils.save_faculty_to_csv(new_faculty)
        print("Faculty added.")

def add_course():
    cid = input("Enter course ID: ")
    name = input("Enter course name: ")
    if find_course(cid):
        print("Course ID already exists!")
    else:
        new_course = Course(cid, name)
        courses.append(new_course)
        utils.save_course_to_csv(new_course)  
        print("Course added.")

def assign_faculty():
    cid = input("Enter course ID: ")
    fid = input("Enter faculty ID: ")
    course = find_course(cid)
    faculty = find_faculty(fid)
    if course and faculty:
        course.set_faculty(fid)
        faculty.assign_course(cid)
        utils.save_faculty_to_csv(faculty) 
        utils.save_course_to_csv(course)   
        print("Faculty assigned to course.")
    else:
        print("Invalid course or faculty ID.")

def enroll_student():
    sid = input("Enter student ID: ")
    cid = input("Enter course ID: ")
    student = find_student(sid)
    course = find_course(cid)
    if student and course:
        student.enroll_in_course(cid)
        course.enroll_student(sid)
        utils.save_student_to_csv(student)
        print("Student enrolled in course.")
    else:
        print("Invalid student or course ID.")

def list_students():
    for s in students:
        print(f"{s.student_id} - {s.name} ({s.major}) Enrolled in: {', '.join(s.enrolled_courses)}")

def list_courses():
    for c in courses:
        faculty = find_faculty(c.faculty_id)
        faculty_name = faculty.name if faculty else "No faculty assigned"
        print(f"{c.course_id} - {c.course_name} | Taught by: {faculty_name}")

def course_enrollments():
    cid = input("Enter course ID: ")
    course = find_course(cid)
    if course:
        print(f"Students enrolled in {course.course_name}:")
        for sid in course.enrolled_students:
            student = find_student(sid)
            if student:
                print(f"{student.student_id} - {student.name}")
    else:
        print("Invalid course ID.")

def edit_student():
    sid = input("Enter the ID of the student to edit: ")
    student = find_student(sid)
    if not student:
        print("No student found with that ID.")
        return
    print(f"Editing {student.name}")
    new_name = input("Enter new name (leave blank to keep current): ")
    new_major = input("Enter new major (leave blank to keep current): ")
    if new_name:
        student.name = new_name
    if new_major:
        student.major = new_major
    utils.save_student_to_csv(student)
    print("Student updated.")

def edit_faculty():
    fid = input("Enter the ID of the faculty to edit: ")
    faculty = find_faculty(fid)
    if not faculty:
        print("No faculty member found with that ID.")
        return
    print(f"Editing {faculty.name}")
    new_name = input("Enter new name (leave blank to keep current): ")
    new_department = input("Enter new department (leave blank to keep current): ")
    if new_name:
        faculty.name = new_name
    if new_department:
        faculty.department = new_department
    utils.save_faculty_to_csv(faculty)
    print("Faculty updated.")

def edit_course():
    cid = input("Enter the ID of the course to edit: ")
    course = find_course(cid)
    if not course:
        print("No course found with that ID.")
        return
    print(f"Editing {course.course_name}")
    new_name = input("Enter new course name (leave blank to keep current): ")
    if new_name:
        course.course_name = new_name
    utils.save_course_to_csv(course)
    print("Course updated.")

def menu():
    while True:
        print("\n--- University Management System ---")
        print("1. Add Student")
        print("2. Add Faculty")
        print("3. Add Course")
        print("4. Assign Faculty to Course")
        print("5. Enroll Student in Course")
        print("6. List All Students")
        print("7. List All Courses")
        print("8. Show Students in a Course")
        print("9. Edit Student")
        print("10. Edit Faculty")
        print("11. Edit Course")
        print("12. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            add_faculty()
        elif choice == '3':
            add_course()
        elif choice == '4':
            assign_faculty()
        elif choice == '5':
            enroll_student()
        elif choice == '6':
            list_students()
        elif choice == '7':
            list_courses()
        elif choice == '8':
            course_enrollments()
        elif choice == '9':
            edit_student()
        elif choice == '10':
            edit_faculty()
        elif choice == '11':
            edit_course()
        elif choice == '12':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    menu()