# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# from sklearn.ensemble import RandomForestClassifier
from sklearn import datasets


def print_hi(name):
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    iris = datasets.load_iris()
    digits = datasets.load_digits()
    print(digits.data)


if __name__ == '__main__':
    print_hi('PyCharm')