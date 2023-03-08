import re

def parse_time(string):
    match = re.fullmatch(r'(\d{2}):(\d{2}):(\d{2})(?:\.(\d{3}))?', string)

    if match:
        parts = []
        for x in match.groups('0'):
            parts.append(int(x))
        return tuple(parts)
    else:
        return None
