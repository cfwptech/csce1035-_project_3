# student.py

class Student:
    def __init__(self, student_id, name, major):
        self.student_id = student_id
        self.name = name
        self.major = major
        self.enrolled_courses = []

    def enroll_in_course(self, course_id):
        if course_id not in self.enrolled_courses:
            self.enrolled_courses.append(course_id)

    def to_dict(self):
        return {
            'student_id': self.student_id,
            'name': self.name,
            'major': self.major,
            'enrolled_courses': ';'.join(self.enrolled_courses)
        }
