#!/usr/bin/env python

POINTS = ["A", "B", "C"]
REPLACES = {
    "X": {"A": "C", "B": "A", "C": "B"},
    "Y": {"A": "A", "B": "B", "C": "C"},
    "Z": {"A": "B", "B": "C", "C": "A"},
}


def solution() -> int:
    def count_points(round: str) -> int:
        points = POINTS.index(REPLACES[round[-1]][round[0]]) + 1

        if round[-1] == "Z":
            points += 6
        elif round[-1] == "Y":
            points += 3

        return points

    with open("../../inputs/02.txt") as input:
        return sum(map(count_points, input.read().split("\n")))


if __name__ == "__main__":
    result = solution()
    print(result)
