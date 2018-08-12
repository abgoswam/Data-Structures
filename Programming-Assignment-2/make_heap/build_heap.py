# python3

class HeapBuilder:
    def __init__(self):
        self._swaps = []
        self._data = []

    def ReadData(self):
        n = int(input())
        self._data = [int(s) for s in input().split()]
        assert n == len(self._data)

    def WriteResponse(self):
        print(len(self._swaps))
        for swap in self._swaps:
            print(swap[0], swap[1])

    def SiftDown(self, i):
        i_left_idx = 2*i + 1
        i_right_idx = 2*i + 2

        n = len(self._data) - 1
        min_index = i
        if i_left_idx <= n and self._data[i_left_idx] < self._data[min_index]:
            min_index = i_left_idx

        if i_right_idx <= n and self._data[i_right_idx] < self._data[min_index]:
            min_index = i_right_idx

        if min_index == i:
            return
        else:
            self._swaps.append((i, min_index))
            self._data[i], self._data[min_index] = self._data[min_index], self._data[i]
            self.SiftDown(min_index)


    def GenerateSwaps(self):
        # The following naive implementation just sorts
        # the given sequence using selection sort algorithm
        # and saves the resulting sequence of swaps.
        # This turns the given array into a heap,
        # but in the worst case gives a quadratic number of swaps.
        #
        # TODO: replace by a more efficient implementation
        # for i in range(len(self._data)):
        #   for j in range(i + 1, len(self._data)):
        #     if self._data[i] > self._data[j]:
        #       self._swaps.append((i, j))
        #       self._data[i], self._data[j] = self._data[j], self._data[i]

        last_index = len(self._data) - 1
        if last_index % 2 == 0:
            n = (last_index - 2) // 2
        else:
            n = (last_index - 1) // 2

        for i in range(n, -1, -1):
            self.SiftDown(i)


    def Solve(self):
        self.ReadData()
        self.GenerateSwaps()
        self.WriteResponse()


if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
