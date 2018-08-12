# python3

class PriorityQ:
    def __init__(self):
        self._data = []

    def insert(self, ft, worker):
        self._data.append([ft, worker])

    def sift_down(self, k):
        min_index = k
        left_child_idx = 2*k + 1
        right_child_idx = 2*k + 2

        if left_child_idx < len(self._data):
            if self._data[left_child_idx][0] < self._data[min_index][0]:
                min_index = left_child_idx
            elif self._data[left_child_idx][0] == self._data[min_index][0] and self._data[left_child_idx][1] < self._data[min_index][1]:
                min_index = left_child_idx

        if right_child_idx < len(self._data):
            if self._data[right_child_idx][0] < self._data[min_index][0]:
                min_index = right_child_idx
            elif self._data[right_child_idx][0] == self._data[min_index][0] and self._data[right_child_idx][1] < self._data[min_index][1]:
                min_index = right_child_idx

        if min_index == k:
            return
        else:
            self._data[k], self._data[min_index] = self._data[min_index], self._data[k]
            self.sift_down(min_index)

    def build_min_heap(self):
        last_index = len(self._data) - 1
        if last_index % 2 == 0:
            n = (last_index - 2) // 2
        else:
            n = (last_index - 1) // 2

        for i in range(n, -1, -1):
            self.sift_down(i)

    def get_next_worker(self):
        return self._data[0]

    def update_min(self, ft):
        self._data[0][0] = ft
        self.sift_down(0)


class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.jobs)):
            print(self.assigned_workers[i], self.start_times[i])

    def assign_jobs(self):
        # # TODO: replace this code with a faster algorithm.
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        # next_free_time = [0] * self.num_workers
        # for i in range(len(self.jobs)):
        #   next_worker = 0
        #   for j in range(self.num_workers):
        #     if next_free_time[j] < next_free_time[next_worker]:
        #       next_worker = j
        #   self.assigned_workers[i] = next_worker
        #   self.start_times[i] = next_free_time[next_worker]
        #   next_free_time[next_worker] += self.jobs[i]

        pq = PriorityQ()
        i = 0
        while i < self.num_workers and i < len(self.jobs):
            self.assigned_workers[i] = i
            self.start_times[i] = 0
            pq.insert(self.jobs[i], i)
            i += 1

        if i == len(self.jobs):
            # all jobs hav been assigned to workers, nothing much to do
            return

        pq.build_min_heap()
        while i < len(self.jobs):
            ft, worker = pq.get_next_worker()
            self.assigned_workers[i] = worker
            self.start_times[i] = ft
            pq.update_min(ft + self.jobs[i])
            i += 1

        return

    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()


# job_queue = JobQueue()
# job_queue.num_workers = 4
# job_queue.jobs = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
# job_queue.assign_jobs()
# job_queue.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()

