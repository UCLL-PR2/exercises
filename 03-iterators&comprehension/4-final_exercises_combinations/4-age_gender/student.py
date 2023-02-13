def read_data(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
        data = [line.split(",") for line in lines]
        return data

dictionary = {
    1: "A",
    2: "B",
    3: "C"
}
#Getting the keys
print(list(dictionary.keys()))
#Getting the values
print(list(dictionary.values()))
