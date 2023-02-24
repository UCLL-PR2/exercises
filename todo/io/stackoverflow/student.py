from collections import Counter


def age_categories(reader):
    return set(row['Age'] for row in reader)



def age_distribution(reader):
    counts = Counter(row['Age'] for row in reader)
    total_count = sum(counts.values())
    return {
        category: count / total_count * 100
        for category, count in counts.items()
    }



def learning_resources(reader):
    return {
        resource
        for row in reader
        for resource in row['LearnCode'].split(';')
    }



def school_percentage(reader):
    total_count = 0
    school_count = 0
    for row in reader:
        learning_resources = row['LearnCode'].lower()
        if 'school' in learning_resources:
            school_count += 1
        total_count += 1
    return school_count / total_count * 100



def most_used_vcs(reader):
    counts = Counter(
        vcs
        for row in reader
        for vcs in row['VersionControlSystem'].split(';')
    )
    total_count = sum(counts.values())
    vcs, count = counts.most_common(1)[0]
    return (vcs, count / total_count)



def most_used_languages(reader):
    counts = Counter(
        language
        for row in reader
        for language in row['LanguageHaveWorkedWith'].split(';')
    )
    return [language for language, _ in counts.most_common()]



def most_wanted_languages(reader):
    counts = Counter(
        language
        for row in reader
        for language in row['LanguageWantToWorkWith'].split(';')
    )
    return [language for language, _ in counts.most_common()]



def underused_languages(reader):
    used = Counter()
    wanted = Counter()
    for row in reader:
        used.update(row['LanguageHaveWorkedWith'].split(';'))
        wanted.update(row['LanguageWantToWorkWith'].split(';'))
    languages = set(used.keys()) | set(wanted.keys())
    return {
        language
        for language in languages
        if used[language] < wanted[language]
    } - {'NA'}



def most_used_by_country(reader):
    table = {}
    for row in reader:
        country = row['Country']
        languages = row['LanguageHaveWorkedWith']
        table.setdefault(country, Counter()).update(languages.split(';'))
    return {
        country: counter.most_common(1)[0][0]
        for country, counter in table.items()
    }
