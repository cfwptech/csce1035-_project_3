# faculty.py

class Faculty:
    def __init__(self, faculty_id, name, department):
        self.faculty_id = faculty_id
        self.name = name
        self.department = department
        self.assigned_courses = []

    def assign_course(self, course_id):
        if course_id not in self.assigned_courses:
            self.assigned_courses.append(course_id)