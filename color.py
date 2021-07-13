import random


def rand():
    a = random.randint(20, 240)
    return a


def color(color_list, num_):
    num = 0
    if len(color_list) == 0:
        new = [num_, (rand(), rand(), rand())]
        color_list.append(new)
    else:
        for colors in color_list:
            if num_ == colors[0]:
                return colors[1]
            else:
                if num == len(color_list) - 1:
                    new = [num_, (rand(), rand(), rand())]
                    color_list.append(new)
                else:
                    num += 1
    return color_list


def get_color(color_list, num):
    for colors in color_list:
        if num == colors[0]:
            return colors[1]
