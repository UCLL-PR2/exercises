from sys import version_info
from textwrap import dedent


print("If you see this message, it means Python is installed on your system")

minimum_version = (3, 6)
major = version_info.major
minor = version_info.minor
installed_version = (major, minor)


if installed_version >= minimum_version:
    print(f"You have Python version %d.%d which is good enough for this course" % (major, minor))
else:
    text = [
        'Sadly, Python tells me its version is %d.%d' % (major, minor),
        'You need version %d.%d or better' % minimum_version,
        '',
        'This could mean two things:',
        '* You have only this old version installed',
        "* You have a more recent version installed as well as an old one, and it's the old one that's being used to run this script",
        "If you're convinced you have a recent enough version installed, ask a lecturer for help",
        "Otherwise, download and install a more recent version of Python"
    ]

    for line in text:
        print(line)
