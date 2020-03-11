import argparse
from queue import Queue


class Graph:

    def __init__(self, adjacency_list):
        self._adjacency_list = adjacency_list
        self._count = len(self._adjacency_list)
        self._visited_peaks = [False for i in range(self._count)]

    def wide_walk(self, start_peak=0):
        queue = Queue()
        queue.put(start_peak)
        while not queue.empty():
            current_peak = queue.get()
            yield current_peak
            self._visited_peaks[current_peak] = True
            for peak in self._adjacency_list[current_peak]:
                if not self._visited_peaks[peak]:
                    queue.put(peak)

    def first_not_visited_peak(self):
        for i in range(self._count):
            if not self._visited_peaks[i]:
                return i
        return -1

    def connectivity_components(self):
        while self.first_not_visited_peak() != -1:
            peaks = list(self.wide_walk(self.first_not_visited_peak()))
            peaks.sort()
            yield peaks


def generate_argparser():
    parser = argparse.ArgumentParser(description='Dichotomy')
    parser.add_argument('-i', dest='input', type=str, help='Input file', default='input.txt')
    parser.add_argument('-o', dest='output', type=str, help='Output file', default='output.txt')
    return parser


def adjacency_list_from_file(file):
    count = int(file.readline())
    adjacency_list = [[int(j) - 1 for j in file.readline().split(' ') if int(j) != 0] for _ in range(count)]
    return adjacency_list


def main():
    parser = generate_argparser()
    args = parser.parse_args()
    try:
        with open(args.input) as input_file:
            adjacency_list = adjacency_list_from_file(input_file)
    except FileNotFoundError:
        print('File ' + args.input + 'not found.')
        return
    graph = Graph(adjacency_list)
    with open(args.output, 'w') as output_file:
        components = list(graph.connectivity_components())
        output_file.write(str(len(components)))
        for component in components:
            output_file.write('\n')
            for peak in component:
                output_file.write(str(peak + 1) + ' ')
            output_file.write('0')


if __name__ == '__main__':
    main()
