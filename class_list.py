def fill(my_first_list, my_second_list):
    if len(my_first_list) <= len(my_second_list):
        for _ in range(len(my_first_list), len(my_second_list)):
            my_first_list.append(0)
    else:
        for _ in range(len(my_second_list), len(my_first_list)):
            my_second_list.append(0)


def my_list_sum(my_first_list, my_second_list):
    first_sum = 0
    second_sum = 0
    for x in my_first_list:
        first_sum += x
    for x in my_second_list:
        second_sum += x
    return first_sum, second_sum


class MyList(list):
    def __add__(self, other):
        list_ex = MyList()
        self_copy = self.copy()
        other_copy = other.copy()
        fill(self_copy, other_copy)
        for x, y in zip(self_copy, other_copy):
            list_ex.append(x + y)
        return list_ex

    def __sub__(self, other):
        list_ex = MyList()
        self_copy = self.copy()
        other_copy = other.copy()
        fill(self_copy, other_copy)
        for x, y in zip(self_copy, other_copy):
            list_ex.append(x - y)
        return list_ex

    def __cmp__(self, other):
        my_tuple = sum(self, other)
        if my_tuple[0] > my_tuple[1]:
            return 1
        elif my_tuple[0] == my_tuple[1]:
            return 0
        else:
            return -1

    def __ne__(self, other):
        my_tuple = my_list_sum(self, other)
        return my_tuple[0] != my_tuple[1]

    def __eq__(self, other):
        my_tuple = my_list_sum(self, other)
        return my_tuple[0] == my_tuple[1]

    def __lt__(self, other):
        my_tuple = my_list_sum(self, other)
        return my_tuple[0] < my_tuple[1]

    def __gt__(self, other):
        my_tuple = my_list_sum(self, other)
        return my_tuple[0] > my_tuple[1]

    def __le__(self, other):
        my_tuple = my_list_sum(self, other)
        return my_tuple[0] <= my_tuple[1]

    def __ge__(self, other):
        my_tuple = my_list_sum(self, other)
        return my_tuple[0] >= my_tuple[1]
