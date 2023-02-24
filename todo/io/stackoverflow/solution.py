from csv import DictReader
from collections import Counter


to_be_tested_function_names = []

def to_be_tested(func):
    to_be_tested_function_names.append(func.__name__)
    return func


# Ignore @to_be_tested, it's only purpose is to simplify testing
@to_be_tested
def age_categories(reader):
    return set(row['Age'] for row in reader)


@to_be_tested
def age_distribution(reader):
    counts = Counter(row['Age'] for row in reader)
    total_count = sum(counts.values())
    return {
        category: count / total_count * 100
        for category, count in counts.items()
    }


@to_be_tested
def learning_resources(reader):
    return {
        resource
        for row in reader
        for resource in row['LearnCode'].split(';')
    }


@to_be_tested
def school_percentage(reader):
    total_count = 0
    school_count = 0
    for row in reader:
        learning_resources = row['LearnCode'].lower()
        if 'school' in learning_resources:
            school_count += 1
        total_count += 1
    return school_count / total_count * 100


def count_values_in_list_column(reader, column):
    return Counter(
        value
        for row in reader
        for value in row[column].split(';')
    )

@to_be_tested
def most_used_vcs(reader):
    counts = count_values_in_list_column(reader, 'VersionControlSystem')
    total_count = sum(counts.values())
    vcs, count = counts.most_common(1)[0]
    return (vcs, count / total_count)


def order_values_by_frequency(counter):
    return [key for key, value in counter.most_common()]

@to_be_tested
def most_used_languages(reader):
    counts = count_values_in_list_column(reader, 'LanguageHaveWorkedWith')
    return order_values_by_frequency(counts)


@to_be_tested
def most_wanted_languages(reader):
    counts = count_values_in_list_column(reader, 'LanguageWantToWorkWith')
    return order_values_by_frequency(counts)


@to_be_tested
def most_used_by_country(reader):
    table = {}
    for row in reader:
        country = row['Country']
        languages = row['LanguageHaveWorkedWith'].split(';')
        table.setdefault(country, Counter()).update(languages)
    return {
        country: counter.most_common(1)[0][0]
        for country, counter in table.items()
    }


@to_be_tested
def average_number_of_languages_worked_with(reader):
    total = 0
    count = 0
    for row in reader:
        languages = row['LanguageHaveWorkedWith'].split(';')
        total += len(languages)
        count += 1
    return total / count


with open('survey.csv') as file:
    reader = DictReader(file)
    print(most_wanted_languages(reader))
