def process_data(string_data):
    students = {}
    for item in string_data:
        name, age, *courses = item.split(',')
        students[name] = {
            'age': int(age),
            'courses': courses
        }
    return students


def average_age(data):
    total_age = 0
    num_students = 0
    for student in data.values():
        total_age += student['age']
        num_students += 1
    return total_age / num_students


# Alternative
def average_age(data):
    total_age = 0
    for num_students,student in enumerate(data.values()):
        total_age += student['age']
        num_students += 1
    return total_age / num_students


def courses(data):
    courses = set()
    for student in data.values():
        courses.update(student['courses'])
    return courses


def most_common_courses(data):
    course_counts = {}
    for student in data.values():
        for course in student['courses']:
            if course not in course_counts:
                course_counts[course] = 0
            course_counts[course] += 1
    max_count = max(course_counts.values())
    return {
        course
        for course in course_counts.keys()
        if course_counts[course] == max_count
    }

# Alternative solution
def most_common_courses(data):
    from collections import Counter
    counts = Counter((course for student in data.values() for course in student['courses']))
    max_count = max(counts.values())
    return {course for course in counts.keys() if counts[course] == max_count}
