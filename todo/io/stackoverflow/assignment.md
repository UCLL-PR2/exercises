# Stack Overflow Survey

Download the [Stack Overflow Annual Developer Survey results for 2022](https://info.stackoverflowsolutions.com/rs/719-EMH-566/images/stack-overflow-developer-survey-2022.zip).
For this series of exercise you will have to write code that analyzes this data.

Write the following functions.
The `reader` parameter will be a `csv.DictReader`.

## `age_categories(reader)`

The `Age` column does not contain actual ages, but ranges such as `25-34 years old`.
`age_categories(reader)` should return a set of all the answers given in this column.

## `age_distribution(reader)`

`age_distribution(reader)` should the distribution of the ages in percentages.
Say 3 people are `25-34 years old` and one `35-54 years old`, then the function should return `{'25-34 years old': 75, '35-54 years old': 1}`.

## `learning_resources(reader)`

The `LearnCode` column contains a _list_ of learning resources used by the respondent.
`learning_resources(reader)` should collect all possible learning resources.

## `school_percentage(reader)`

`school_percentage(reader)` returns the percentage of users that entered `School (i.e., University, College, etc)` in the `LearnCode` field.

## `most_used_vcs(reader)`

The `VersionControlSystem` contains a list of version control systems used by the respondent.
`most_used_vcs(reader)` must return a pair:

* The first element should be the actual VCS system used.
* The second element the percentage of respondents that have that VCS listed in their `VersionControlSystem` answer.

## `most_used_languages(reader)`

Return a list of all programming languages appearing in the `LanguageHaveWorkedWith` column.
The list must be ordered from most commonly used to least commonly used.

## `most_wanted_languages(reader)`

Return a list of all programming languages appearing in the `LanguageWantToWorkWith` column.
The list must be ordered from most commonly used to least commonly used.

Since this is so similar to `most_used_languages`, make sure to factor out the common code.

## `most_used_by_country(reader)`

Count how many times a language was used (`LanguageHaveWorkedWith`) by country (`Country`).
Return the most commonly used language by country as a `dict`.

## `average_number_of_languages_worked_with(reader)`

Count the average number of languages (`LanguageHaveWorkedWith`) used per respondent.
