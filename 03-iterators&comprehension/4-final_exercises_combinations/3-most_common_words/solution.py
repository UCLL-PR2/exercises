def create_word_dict(file_name):
    with open(file_name, 'r') as f:
        word_list = f.read().split()
        word_list = [word.strip('.,?!-') for word in word_list]
        word_list = [word.lower() for word in word_list]
        word_list = list(filter(lambda x: x.isalpha(), word_list))
        word_dict = {word: word_list.count(word) for word in word_list}
    return word_dict

word_dict = create_word_dict('example.txt')
print(word_dict)

def get_top_10_words(word_dict):
    sorted_words = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
    top_10 = {k: v for k, v in sorted_words[:10]}
    return top_10

# top_10 = get_top_10_words(word_dict)
# print(top_10)


