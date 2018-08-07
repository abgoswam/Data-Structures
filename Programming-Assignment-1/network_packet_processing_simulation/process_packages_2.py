# python3

class Request:
    def __init__(self, arrival_time, process_time):
        self.arrival_time = arrival_time
        self.process_time = process_time

class Response:
    def __init__(self, dropped, start_time):
        self.dropped = dropped
        self.start_time = start_time

class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time_ = []

    def bin_search(self, t):
        # return index i  s.t. self.finish_time_ > t else None
        if len(self.finish_time_) == 0:
            return None

        if self.finish_time_[0] > t:
            return 0
        elif self.finish_time_[-1] <= t:
            return None
        else:
            l = 0
            r = len(self.finish_time_) - 1
            while True:
                i = l + (r - l) // 2
                if self.finish_time_[i-1] <= t < self.finish_time_[i]:
                    return i
                elif self.finish_time_[i] <= t:
                    l = i + 1
                else:
                    r = i

    def Process(self, request):
        # write your code here

        # process queue first -- only retain items in Q whose finish_time is past this requests arrival_time
        # self.finish_time_ = [item for item in self.finish_time_ if item > request.arrival_time]
        i_bin_search = self.bin_search(request.arrival_time)
        if i_bin_search is None:
            self.finish_time_ = []
        else:
            self.finish_time_ = self.finish_time_[i_bin_search:]

        if len(self.finish_time_) == 0:
            # no items in queue
            res = Response(False, request.arrival_time)
            self.finish_time_.append(request.arrival_time + request.process_time)
        elif len(self.finish_time_) >= self.size:
            # queue is full
            res = Response(True, -1)
        else:
            # there is space in the queue
            res = Response(False, self.finish_time_[-1])
            request_finish_time = self.finish_time_[-1] + request.process_time
            self.finish_time_.append(request_finish_time)

        return res


def ReadRequests(count):
    requests = []
    for i in range(count):
        arrival_time, process_time = map(int, input().strip().split())
        requests.append(Request(arrival_time, process_time))
    return requests


def ProcessRequests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.Process(request))
    return responses


def PrintResponses(responses):
    for response in responses:
        print(response.start_time if not response.dropped else -1)


# size, count = 1, 2
# requests = ReadRequests(count)
# buffer = Buffer(size)
# responses = ProcessRequests(requests, buffer)
# PrintResponses(responses)

if __name__ == "__main__":
    size, count = map(int, input().strip().split())
    requests = ReadRequests(count)

    buffer = Buffer(size)
    responses = ProcessRequests(requests, buffer)

    PrintResponses(responses)
