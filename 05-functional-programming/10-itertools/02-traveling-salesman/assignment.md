# Traveling Salesman Problem

The [Traveling Salesman Problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem) (TSP) is a well known problem in the world of computer science.
The problem goes as follows: you are given a list of cities and the distances between them.
You are a traveling salesman starting in some given city.
You must then find the shortest tour that visits every city exactly once and then returns back to your starting city.

There is no known efficient algorithm to solve this problem: you can simply generate every possible path, compute its total distance, and return the path with the smallest total distance.

## Task

Write a function `find_shortest_path(distance, city_count)`:

* `distance` is a function that you can use to determine the distance between to cities.
  For example, `distance(0, 1)` returns the distance between cities `0` and `1`.
* `city_count` is the number of cities.
  The city numbers are `0`, `1`, ..., `city_count-1`.
* `find_shortest_path` should return a list of city indices representing the shortest possible tour.
  The path should always start and end in city `0`.

For example, say `city_count` is 4.
The possible tours are

* `[0, 1, 2, 3, 0]`
* `[0, 1, 3, 2, 0]`
* `[0, 2, 1, 3, 0]`
* `[0, 2, 3, 1, 0]`
* `[0, 3, 1, 2, 0]`
* `[0, 3, 2, 1, 0]`

Use `distance` to compute the total distance of each tour, and return the tour with the smallest total distance.

**Hint** Look for a useful function in [`itertools`](https://docs.python.org/3/library/itertools.html).
