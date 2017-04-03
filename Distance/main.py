import numpy as N


def main():
    x = N.array([0, 1, 2, 3, 4])
    y = N.array([0, 1, 2, 3])
    pt = N.array([-2.3, 3.3])
    print(distance(x, y, pt))


def distance(firstList, secondList, originalPoint):
    ## Perform cartesian product and calculate the distance at the same time
    output = [((((xAxis - originalPoint[0]) ** 2) + ((yAxis - originalPoint[1]) ** 2)) ** 0.5) \
              for xAxis in firstList for yAxis in secondList]

    ## Reshape the array in a row wise order
    output = N.reshape(output, (secondList.size, firstList.size), order='F')
    return output


main()
