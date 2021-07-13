global x, y, x1_re, x2_re, y1_re, y2_re


def judge(matrix, x1, y1, x2, y2):
    global x, y, x1_re, x2_re, y1_re, y2_re
    size = matrix.shape
    if matrix[x1, y1] == matrix[x2, y2]:
        pass
    else:
        return False

    def what(par1, par2):
        if par1 < par2:
            a = [par1, par2]
        else:
            a = [par2, par1]
        return a

    x = what(x1, x2)
    y = what(y1, y2)
    if x1 == x2:
        if y[1] - y[0] == 1:
            return True
        else:
            for i in range(1, (y[1] - y[0])):
                if matrix[x1, y[0] + i] == 0:
                    if i == y[1] - y[0] - 1:
                        return True
                    else:
                        pass
                else:
                    pass
    if y1 == y2:
        if x[1] - x[0] == 1:
            return True
        else:
            for j in range(1, (x[1] - x[0])):
                if matrix[x[0] + j, y1] == 0:
                    if j == x[1] - x[0] - 1:
                        return True
                    else:
                        pass
                else:
                    pass
    for X in range(0, size[0]):
        x1_re = x2_re = False
        distance_x1 = abs(X - x1)
        distance_x2 = abs(X - x2)
        x1x = what(X, x1)
        x2x = what(X, x2)
        if distance_x1 == 0:
            x1_re = True
        elif distance_x1 == 1:
            if matrix[X, y1] == 0:
                x1_re = True
            else:
                continue
        else:
            for ii in range(1, distance_x1):
                if matrix[x1x[0] + ii, y1] == 0:
                    if ii == distance_x1 - 1:
                        if matrix[X, y1] == 0:
                            x1_re = True
                        else:
                            continue
                    else:
                        pass
                else:
                    continue
        if distance_x2 == 0:
            x2_re = True
        elif distance_x2 == 1:
            if matrix[X, y2] == 0:
                x2_re = True
            else:
                continue
        else:
            for ii in range(1, distance_x2):
                if matrix[x2x[0] + ii, y2] == 0:
                    if ii == distance_x1 - 1:
                        if matrix[X, y2] == 0:
                            x2_re = True
                        else:
                            continue
                    else:
                        pass
                else:
                    continue
        if x1_re is True and x2_re is True:
            distance_y1y2 = abs(y1 - y2)
            if distance_y1y2 == 1:
                return True
            else:
                for jj in range(1, distance_y1y2):
                    if matrix[X, y[0] + jj] == 0:
                        if jj == distance_y1y2 - 1:
                            return True
                        else:
                            pass
                    else:
                        continue
    for Y in range(0, size[1]):
        y1_re = y2_re = False
        distance_y1 = abs(Y - y1)
        distance_y2 = abs(Y - y2)
        y1y = what(Y, y1)
        y2y = what(Y, y2)
        if distance_y1 == 0:
            y1_re = True
        elif distance_y1 == 1:
            if matrix[x1, Y] == 0:
                y1_re = True
            else:
                continue
        else:
            for ii in range(1, distance_y1):
                if matrix[x1, y1y[0] + ii] == 0:
                    if ii == distance_y1 - 1:
                        if matrix[x1, Y] == 0:
                            y1_re = True
                        else:
                            continue
                    else:
                        pass
                else:
                    continue
        if distance_y2 == 0:
            y2_re = True
        elif distance_y2 == 1:
            if matrix[x2, Y] == 0:
                y2_re = True
            else:
                continue
        else:
            for ii in range(1, distance_y2):
                if matrix[x2, y2y[0] + ii] == 0:
                    if ii == distance_y2 - 1:
                        if matrix[x2, Y] == 0:
                            y2_re = True
                        else:
                            continue
                    else:
                        pass
                else:
                    continue
        if y1_re is True and y2_re is True:
            distance_x1x2 = abs(x1 - x2)
            if distance_x1x2 == 1:
                return True
            else:
                for jj in range(1, distance_x1x2):
                    if matrix[x[0] + jj, Y] == 0:
                        if jj == distance_x1x2 - 1:
                            return True
                        else:
                            pass
                    else:
                        continue
    return False
