def word_count(string):
    if len(string) != 0:
        return len(string.split(' '))
    else:
        # Separate logic necessary for empty string because "".split(' ') yields ['']
        return 0
