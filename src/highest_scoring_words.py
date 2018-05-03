"""Given str of words, find highest scoring word if a=1, b=2, etc."""


def high(string):
    word_list = string.split()
    sums = []
    for word in word_list:
        sums.append(sum([ord(l) - 96 for l in word]))
    zipp = list(zip(word_list, sums))
    print(zipp)
    final_sort = sorted(zipp, key=lambda x: x[1])
    if final_sort[-2][1] == final_sort[-1][1]:
        return final_sort[-2][0]
    else:
        return final_sort[-1][0]
