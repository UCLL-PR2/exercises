import re


def parse_time(string):
    match = re.fullmatch(r'(\d{2}):(\d{2}):(\d{2})(\.\d{3})?', string)

    if match:
        h, m, s, ms = match.groups('.000')
        ms = ms[1:]  # drop dot
        (int(h), int(m), int(s), int(ms))
    else:
        return None


# Alternative solution using noncapturing groups
def parse_time(string):
    # We need parentheses so that the ? applies to the whole fractional part, including the dot
    # but we aren't really interested in capturing the dot itself, we only want the three digits
    # The ?: means "this is a noncapturing group": it will still bundle things together,
    # but won't appear in the match.groups list.
    # You can of course solve the problem in many other ways, but sometimes we like the solution to offer something new
    match = re.fullmatch(r'(\d{2}):(\d{2}):(\d{2})(?:\.(\d{3}))?', string)

    if match:
        return tuple([int(x) for x in match.groups('0')])
    else:
        return None
