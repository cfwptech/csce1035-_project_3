# course.py

class Course:
    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name
        self.faculty_id = None
        self.enrolled_students = []

    def set_faculty(self, faculty_id):
        self.faculty_id = faculty_id

    def enroll_student(self, student_id):
        if student_id not in self.enrolled_students:
            self.enrolled_students.append(student_id)