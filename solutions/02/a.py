#!/usr/bin/env python

WINS = ["C X", "A Y", "B Z"]
DRAWS = ["A X", "B Y", "C Z"]
POINTS = ["X", "Y", "Z"]


def solution() -> int:
    def count_points(round: str) -> int:
        points = POINTS.index(round[-1]) + 1

        if round in WINS:
            points += 6
        elif round in DRAWS:
            points += 3

        return points

    with open("../../inputs/02.txt") as input:
        return sum(map(count_points, input.read().split("\n")))


if __name__ == "__main__":
    result = solution()
    print(result)
