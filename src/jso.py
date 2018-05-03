"""Module to count unique values from json file."""
from collections import Counter

import json


def count_unique():
    """Read in json, add to set, return len of set."""
    with open('test_json.json') as f:
        data = json.load(f)
    unique = set()
    for item in data:
        unique.add(item['status'])
    print(len(unique))


def top_users():
    """Read in json, use Counter to get total counts, print top five."""
    with open('test_json.json') as f:
        data = json.load(f)
    total_counts = Counter(k['user_id'] for k in data)
    for user, count in total_counts.most_common(5):
        print('{}: {}'.format(user, count))


def status_8951_average():
    """Find status 8951, ignore times that are null, get average of all times."""
    with open('test_json.json') as f:
        data = json.load(f)
    all_times = []
    for item in data:
        if item['status'] == 8951:
            if (item['end_time'] is not None) and (item['start_time'] is not None):
                all_times.append((item['end_time'] - item['start_time']))
    print(sum(all_times) // len(all_times))


def error_status_percentage():
    """Find status ending in 3, append to holder, use counter to find piece_id with more than two errors."""
    with open('test_json.json') as f:
        data = json.load(f)
    holder = []
    for item in data:
        if str(item['status'])[-1] == '3':
            holder.append(item)
    counts = Counter(k['piece_id'] for k in holder)
    new_counts = [x for x in counts if counts[x] >= 2]
    print(len(new_counts) / len(data))


if __name__ == '__main__':
    count_unique()
    top_users()
    status_8951_average()
    error_status_percentage()
