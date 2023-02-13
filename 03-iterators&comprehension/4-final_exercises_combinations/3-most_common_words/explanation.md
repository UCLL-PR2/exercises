# Exercises most common words - difficulty level: ***


Create a function **create_word_dict** that reads in a text file and create a dictionary where the keys are the words in the file, and the values are the number of times each word appears in the file.
- Use **open()** to read in the text file and a dictionary comprehension to create the initial dictionary.
- Use *split()* to break up the text into words, and strip() to remove leading and trailing punctuation from each word.
- Use *lower()* to convert each word to lowercase, so that "the" and "The" are treated as the same word.
- Use *filter()* and a lambda function to remove any words that are empty strings or contain only punctuation.

Create a function **get_top_10_words** that sorts the returend dictionary by function **create_word_dict** by values in descending order and create a new dictionary that contains only the top 10 most common words.
- Use a lambda function and the *sorted()* function to create a list of tuples, where each tuple contains a word and its count.
- Use a dictionary *comprehension* to create a new dictionary that contains only the top 10 tuples.


