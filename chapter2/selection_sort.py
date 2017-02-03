def find_small(lst):
    small = lst[0]
    small_index = 0
    for i in range(1, len(lst)):
        if lst[i] < small:
            small = lst[i]
            small_index = i
    return small_index


def selection_sort(lst):
    new_lst = []
    for i in range(len(lst)):
        small = find_small(lst)
        new_lst.append(lst.pop(small))
    return new_lst


a = [25, 100, 225, 14, 19, 12]
print(selection_sort(a))
