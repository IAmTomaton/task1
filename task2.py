import argparse
from queue import Queue


class Graph:

    def __init__(self, matrix):
        self._matrix = matrix
        self._count = len(self._matrix)
        self._visited_points = [False for i in range(self._count)]

    def wide_walk(self):
        queue = Queue()
        queue.put(0)
        while not queue.empty():
            current_point = queue.get()
            print(current_point)
            self._visited_points[current_point] = True
            for point in range(self._count):
                if self._matrix[current_point][point] == 1 and not self._visited_points[point]:
                    queue.put(point)


def generate_argparser():
    parser = argparse.ArgumentParser(description='Dichotomy')
    parser.add_argument('-i', dest='input', type=str, help='Input file', default='input.txt')
    parser.add_argument('-o', dest='output', type=str, help='Output file', default='output.txt')
    return parser


def matrix_from_file(file):
    count = int(file.readline())
    matrix = [[int(j) for j in file.readline().split(' ')] for _ in range(count)]
    return matrix


def main():
    parser = generate_argparser()
    args = parser.parse_args()
    try:
        with open(args.input) as input_file:
            matrix = matrix_from_file(input_file)
    except FileNotFoundError:
        print('File ' + args.input + 'not found.')
        return
    graph = Graph(matrix)
    graph.wide_walk()


if __name__ == '__main__':
    main()
