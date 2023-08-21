#!/usr/bin/env python


def solution() -> int:
    def contains_other(ranges: str) -> bool:
        [first, second] = ranges.split(",")
        [first_0, first_1] = first.split("-")
        [second_0, second_1] = second.split("-")

        [first, second] = [
            set(range(int(first_0), int(first_1) + 1)),
            set(range(int(second_0), int(second_1) + 1)),
        ]

        return first.issubset(second) or second.issubset(first)

    with open("../../inputs/04.txt") as input:
        return len(list(filter(contains_other, input.read().split("\n"))))


if __name__ == "__main__":
    result = solution()
    print(result)
