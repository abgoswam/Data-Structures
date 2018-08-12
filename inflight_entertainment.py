import sys


def can_two_movies_fill_flight(flight_length, movie_lengths):
    print("flight length : {0}".format(flight_length))
    print("movie lengths : {0}".format(movie_lengths))

    movie_timings = {}
    for mov_len in movie_lengths:
        if (flight_length - mov_len) in movie_timings:
            return 1
        else:
            if mov_len in movie_timings:
                movie_timings[mov_len] += 1
            else:
                movie_timings[mov_len] = 1

    return 0


if __name__ == "__main__":
    text = sys.stdin.read()
    n, flight_length, *movie_lengths = list(map(int, text.split()))
    print(can_two_movies_fill_flight(flight_length, movie_lengths))

