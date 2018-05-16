"""File Structure Coding Challenge."""

import os

route = os.listdir('./test_labels_renamed/')

lengths = []


def counter(route):
    """Iterate through dir, count lines, return list of list sorted by length."""
    for file in route:
        if file.endswith('.txt'):
            with open(os.path.join('./test_labels_renamed/', file)) as curr_file:
                total = 0
                for line in curr_file:
                    total += 1
        lengths.append([file, total])
    return sorted(lengths, key=lambda x: x[1], reverse=True)


if __name__ == '__main__':
    print(counter(route))
