import contextlib
import sys
import os


STUDENT_FILE = 'student.py'

def log(message):
    print(message, file=sys.stderr)


@contextlib.contextmanager
def inside_directory(path):
    previous_cwd = os.getcwd()
    os.chdir(path)
    yield
    os.chdir(previous_cwd)


def collect_student_paths(repository_directory):
    return {os.path.relpath(root, repository_directory) for root, _dirs, files in os.walk(repository_directory) if STUDENT_FILE in files}


def file_size(path):
    return os.path.getsize(path)


def show_help():
    log(f'''
You need to specify the two root directories of your repositories.
For example,

$ py {os.path.basename(__file__)} old-repo new-repo

This will copy student.py files from old-repo to new-repo.
    '''.strip())


if len(sys.argv) != 3:
    show_help()
    sys.exit(1)

source_directory = sys.argv[1]
target_directory = sys.argv[2]

log(f'Checking that {source_directory} exists')
if not os.path.isdir(source_directory):
    log(f'{source_directory} should be a directory')
    sys.exit(-1)

log(f'Checking that {target_directory} exists')
if not os.path.isdir(target_directory):
    log(f'{target_directory} should be a directory')
    sys.exit(-1)

log(f'Collecting all student.py files in {source_directory}')
source_student_paths = collect_student_paths(source_directory)
log(f'Found {len(source_student_paths)} paths')

log(f'Collecting all student.py files in {target_directory}')
target_student_paths = collect_student_paths(target_directory)
log(f'Found {len(target_student_paths)} paths')

student_paths = source_student_paths.intersection(target_student_paths)
log(f'Intersection counts {len(student_paths)} paths')

if len(student_paths) == 0:
    log('No common paths found! Are you sure you point to the same directory inside your repos?')
    sys.exit(1)


log(f'Generating shell script...')

for student_path in sorted(student_paths):
    source = os.path.join(source_directory, student_path, STUDENT_FILE).replace('\\', '/')
    target = os.path.join(target_directory, student_path, STUDENT_FILE).replace('\\', '/')

    if not os.path.isfile(source):
        log(f'Error: {source} is not a file')
        sys.exit(1)
    if not os.path.isfile(target):
        log(f'Error: {target} is not a file')
        sys.exit(1)

    source_size = file_size(source)
    target_size = file_size(target)
    copy_command = f'cp "{source}" "{target}"'

    if source_size < target_size:
        print(f'# WARNING: {source} is smaller than {target}')
        print(f'# {copy_command}')
    else:
        print(copy_command)


log('Finished successfully')
