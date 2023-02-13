def read_data(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
        data = [line.split(",") for line in lines]
        return data

def create_dictionary(data):
    return {name: (int(age), gender) for name, age, gender in data}
    # return {i[0]:(i[1],i[2]) for i in data}

def older_than_30(data):
    return [(name, gender) for name, (age, gender) in data.items() if age > 30]

def all_ages(data):
    return list(map(lambda x: x[1][0], data.items()))

def gender_totals(data):
    male_total = sum(age for age, gender in data.values() if gender == "Male")
    female_total = sum(age for age, gender in data.values() if gender == "Female")
    return {"Male": male_total, "Female": female_total}

# data = read_data("example.txt")
# dictionary = create_dictionary(data)
# older_than_30_list = older_than_30(dictionary)
# all_ages_list = all_ages(dictionary)
# gender_totals_dict = gender_totals(dictionary)

# print(dictionary)
# print(older_than_30_list)
# print(all_ages_list)
# print(gender_totals_dict)
