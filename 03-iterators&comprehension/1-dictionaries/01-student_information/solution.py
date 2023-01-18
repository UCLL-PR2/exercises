def process_data(data: list) -> dict:
    """
    Process a list of strings containing student information and return a dictionary
    with the following structure:
    {
        'John Smith': {
            'age': 20,
            'courses': ['Math', 'Physics']
        },
        'Jane Doe': {
            'age': 21,
            'courses': ['Biology', 'Chemistry']
        }
    }
    
    The input list is in the following format:
    ['John Smith,20,Math,Physics', 'Jane Doe,21,Biology,Chemistry']
    """
    students = {}
    for item in data:
        name, age, *courses = item.split(',')
        students[name] = {
            'age': int(age),
            'courses': courses
        }
    return students

def avg_age(data: dict) -> float:
    """
    Calculate the average age of the students in the input dictionary.
    """
    total_age = 0
    num_students = 0
    for student in data.values():
        total_age += student['age']
        num_students += 1
    return total_age / num_students

def courses(data: dict) -> list:
    """
    Return a list of all the courses taken by the students in the input dictionary.
    """
    courses = []
    for student in data.values():
        courses.extend(student['courses'])
    return courses

def most_common_course(data: dict) -> str:
    """
    Return the course that is taken by the most number of students. If there is a tie,
    return the first course that appears in the input dictionary.
    """
    course_counts = {}
    for student in data.values():
        for course in student['courses']:
            if course not in course_counts:
                course_counts[course] = 0
            course_counts[course] += 1
    return max(course_counts, key=course_counts.get)