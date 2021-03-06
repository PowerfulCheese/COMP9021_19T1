# Randomly generates a grid with 0s and 1s, whose dimension is controlled by user input,
# as well as the density of 1s in the grid, and determines the size of the largest
# isosceles triangle, consisting of nothing but 1s and whose base can be either
# vertical or horizontal, pointing either left or right or up or down.
#
# Written by *** and Eric Martin for COMP9021


from random import seed, randint
import sys
from collections import defaultdict


def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(int(grid[i][j] != 0)) for j in range(len(grid))))


# 四个坐标转换函数

def N(i, j, l):
    return i, j


def S(i, j, l):
    """
    >>> S(0, 0, 5)
    (4, 4)
    >>> S(0, 4, 5)
    (4, 0)
    >>> S(4, 0, 5)
    (0, 4)
    >>> S(4, 4, 5)
    (0, 0)
    >>> S(2, 2, 5)
    (2, 2)
    >>> S(1, 2, 5)
    (3, 2)
    >>> S(2, 1, 5)
    (2, 3)
    >>> S(3, 2, 5)
    (1, 2)
    >>> S(2, 3, 5)
    (2, 1)
    """
    return l-1-i, l-1-j


def W(i, j, l):
    """
    >>> W(0, 0, 5)
    (4, 0)
    >>> W(0, 4, 5)
    (0, 0)
    >>> W(4, 0, 5)
    (4, 4)
    >>> W(4, 4, 5)
    (0, 4)
    >>> W(2, 2, 5)
    (2, 2)
    >>> W(1, 2, 5)
    (2, 1)
    >>> W(2, 1, 5)
    (3, 2)
    >>> W(3, 2, 5)
    (2, 3)
    >>> W(2, 3, 5)
    (1, 2)
    """
    return l-1-j, i


def E(i, j, l):
    """
    >>> E(0, 0, 5)
    (0, 4)
    >>> E(0, 4, 5)
    (4, 4)
    >>> E(4, 0, 5)
    (0, 0)
    >>> E(4, 4, 5)
    (4, 0)
    >>> E(2, 2, 5)
    (2, 2)
    >>> E(1, 2, 5)
    (2, 3)
    >>> E(2, 1, 5)
    (1, 2)
    >>> E(3, 2, 5)
    (2, 1)
    >>> E(2, 3, 5)
    (3, 2)
    """
    return j, l-1-i


def size_of_largest_isosceles_triangle():
    # 四个方向，计算四次，取最大值
    return max(size_in_one_attitude(i) for i in [N, W, E, S])


dict_triangle_size = defaultdict(lambda: 0)

# 其中一个方向的最大size
def size_in_one_attitude(converter):
    largest_size = 0
    for i in range(len(grid)):
        connected_nonzero = 0
        for j in range(len(grid)):

            # 还是存起来吧，要不热要调用两次
            p = converter(i, j, len(grid))

            if grid[p[0]][p[1]] != 0:
                connected_nonzero += 1
            else:
                connected_nonzero = 0
                continue
            # print(triangle_size_as_corner(i, j, connected_nonzero, converter), end=' ')
            size = triangle_size_as_corner(i, j, connected_nonzero, converter)
            if largest_size < size:
                largest_size = size
        # print()
    return largest_size


# 以某个点作为三角形的点，这个三角形最大的size
# c: 以这个点为基准，往左数，有几个1（包括这个点）
def triangle_size_as_corner(i, j, c, converter):
    # ul (upper left) 左上角
    ul = dict_triangle_size[converter(i-1, j-1, len(grid))]
    result = 1
    if (ul+1)*2-1 <= c:
        result = ul + 1
    else:
        result = (c-1)//2 + 1
    dict_triangle_size[converter(i, j, len(grid))] = result
    return result


try:
    # arg_for_seed, density = 0, 100
    arg_for_seed, density = (abs(int(x)) for x in input('Enter two integers: ').split())
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
grid = [[randint(0, density) for _ in range(10)] for _ in range(10)]
print('Here is the grid that has been generated:')
display_grid()
print('The largest isosceles triangle has a size of',
      size_of_largest_isosceles_triangle()
     )
