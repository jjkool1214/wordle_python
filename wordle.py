import random

def create_data(filename):
    full_set = set()
    full_list = list()
    with filename as file:
        for line in file:
            full_set.add(line.strip())
            full_list.append(line.strip())
    return full_set, full_list

def check_valid(word):
    pass


def main():
    pass