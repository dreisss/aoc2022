#!/usr/bin/env python


def solution() -> int:
    def count_priority(rucksack: str) -> int:
        [first, second] = [
            set(rucksack[: len(rucksack) // 2]),
            set(rucksack[len(rucksack) // 2 :]),
        ]

        return count_points(first.intersection(second).pop())

    def count_points(commom: str) -> int:
        ordinal = ord(commom)

        if ordinal >= 97:
            return ordinal - 96

        return ordinal - 64 + 26

    with open("../../inputs/day03.txt") as input:
        return sum(map(count_priority, input.read().split("\n")))


if __name__ == "__main__":
    result = solution()
    print(result)
