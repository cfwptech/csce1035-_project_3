# utils.py

import csv
from student import Student
from faculty import Faculty
from course import Course


STUDENT_CSV = 'students.csv'
FACULTY_CSV = 'faculty.csv'
COURSES_CSV = 'courses.csv'

def save_student_to_csv(student):
    students = load_students_from_csv()
    students = [s for s in students if s.student_id != student.student_id]
    students.append(student)
    with open(STUDENT_CSV, 'w', newline='') as csvfile:
        fieldnames = ['student_id', 'name', 'major', 'enrolled_courses']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for s in students:
            writer.writerow(s.to_dict())

def load_students_from_csv():
    students = []
    try:
        with open(STUDENT_CSV, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                student = Student(row['student_id'], row['name'], row['major'])
                if row['enrolled_courses']:
                    student.enrolled_courses = row['enrolled_courses'].split(';')
                students.append(student)
    except FileNotFoundError:
        pass # if the file does not exist
    return students

def save_faculty_to_csv(faculty_member):
    faculty_list = load_faculty_from_csv() 
    faculty_list = [f for f in faculty_list if f.faculty_id != faculty_member.faculty_id]
    faculty_list.append(faculty_member)
    with open(FACULTY_CSV, 'w', newline='') as csvfile:
        fieldnames = ['faculty_id', 'name', 'department', 'assigned_courses']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for f in faculty_list:
            writer.writerow({
                'faculty_id': f.faculty_id,
                'name': f.name,
                'department': f.department,
                'assigned_courses': ';'.join(f.assigned_courses)
            })

def load_faculty_from_csv():
    faculty_list = []
    try:
        with open(FACULTY_CSV, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                faculty_member = Faculty(row['faculty_id'], row['name'], row['department'])
                if row['assigned_courses']:
                    faculty_member.assigned_courses = row['assigned_courses'].split(';')
                faculty_list.append(faculty_member)
    except FileNotFoundError:
        pass
    return faculty_list

def save_course_to_csv(course_obj):
    courses_list = load_courses_from_csv()
    courses_list = [c for c in courses_list if c.course_id != course_obj.course_id]
    courses_list.append(course_obj)
    with open(COURSES_CSV, 'w', newline='') as csvfile:
        fieldnames = ['course_id', 'course_name', 'faculty_id', 'enrolled_students']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for c in courses_list:
            writer.writerow({
                'course_id': c.course_id,
                'course_name': c.course_name,
                'faculty_id': c.faculty_id if c.faculty_id else '',
                'enrolled_students': ';'.join(c.enrolled_students)
            })

def load_courses_from_csv():
    courses = []
    try:
        with open(COURSES_CSV, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                course = Course(row['course_id'], row['course_name'])
                if row['faculty_id']:
                    course.set_faculty(row['faculty_id'])
                if row['enrolled_students']:
                    course.enrolled_students = row['enrolled_students'].split(';')
                courses.append(course)
    except FileNotFoundError:
        pass
    return courses


