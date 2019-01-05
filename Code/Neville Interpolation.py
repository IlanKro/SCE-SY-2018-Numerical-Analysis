def nevilleInter(points, x):
    """
    :param points: a list of points ie ((0,1),(1,2)) etc..
    :param x: the x in question of what the value is at this x
    :return: the value y at the given x
    """
    if len(points) < 2:
        return "Invalid points"

    p = [[0 for j in range(len(points))] for y in range(len(points))]
    for i in range(len(points)):
        p[i][i] = points[i][1]
        if i + 1 < len(points):
            if points[i + 1][0] <= points[i][0]:
                return "Invalid points"
    i = 0
    j = 1
    t = j
    while True:
        print("P{0},{1}=(({2} - x{1}) * p{0}{3} - ({2} -x{0}) * p{4}{1}/ (x{0} - x{1})=".format(i,j,x,j-1,i+1),end="")
        p[i][j] = ((x - points[j][0]) * p[i][j - 1] - (x - points[i][0]) * p[i + 1][j]) / (
            points[i][0] - points[j][0])
        print(p[i][j])
        if i == 0 and j == len(points) - 1:
            break
        if j == len(points) - 1:
            i = 0
            j = t + 1
            t = j
        else:
            i += 1
            j += 1
    return p[0][-1]


print(nevilleInter(((8.1, 16.9446), (8.3, 17.56492), (8.6, 18.50515), (8.7, 18.82091)),8.5))
