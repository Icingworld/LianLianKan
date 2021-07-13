import random


# 判断相同数字个数是否为偶数
def check(matrix):
    size = matrix.shape
    father_list = []
    length = 0
    for i in range(0, size[0]):
        for j in range(0, size[1]):
            num = 0
            if matrix[i, j] == 0:
                pass
            else:
                if len(father_list) == 0:
                    list_new = [matrix[i, j], (i, j)]
                    father_list.append(list_new)
                else:
                    for lists in father_list:
                        if matrix[i, j] == lists[0]:
                            lists.append((i, j))
                            num += 1
                            break
                        else:
                            if num == len(father_list) - 1:
                                list_new = [matrix[i, j], (i, j)]
                                father_list.append(list_new)
                            else:
                                num += 1
    for list_ in father_list:
        # 列表长度为奇数，否则随机删掉一个
        if len(list_) % 2 == 1:
            pass
        else:
            index = random.randint(1, len(list_) - 1)
            matrix[list_[index]] = 0
            del list_[index]
    for list_ in father_list:
        # 总个数
        length += (len(list_) - 1)
    return matrix, father_list, length
