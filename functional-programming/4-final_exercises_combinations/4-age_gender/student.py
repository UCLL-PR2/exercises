def read_data(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
        data = [line.split(",") for line in lines]
        return data
