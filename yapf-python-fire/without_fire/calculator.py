from sys import argv


def add_two(x, y):
    return x + y


def add_three(x, y, z):
    return x + y + z


if __name__ == "__main__":
    if argv[1] == "add_2":
        print(add_two(int(argv[2]), int(argv[3])))
    elif argv[1] == "add_3":
        print(add_three(int(argv[2]), int(argv[3]), int(argv[4])))
