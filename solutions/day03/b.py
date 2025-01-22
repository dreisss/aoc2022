#!/usr/bin/env python


def solution() -> int:
    def count_priority(rucksacks: list[str]) -> int:
        [first, second, third] = [
            set(rucksacks[0]),
            set(rucksacks[1]),
            set(rucksacks[2]),
        ]

        return count_points(first.intersection(second).intersection(third).pop())

    def count_points(commom: str) -> int:
        ordinal = ord(commom)

        if ordinal >= 97:
            return ordinal - 96

        return ordinal - 64 + 26

    with open("../../inputs/day03.txt") as input:
        rucksacks = input.read().split("\n")
        return sum(
            map(
                count_priority,
                [rucksacks[i : i + 3] for i in range(0, len(rucksacks), 3)],
            )
        )


if __name__ == "__main__":
    result = solution()
    print(result)
