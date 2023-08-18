#!/usr/bin/env python


def solution() -> int:
    with open("../../inputs/01.txt") as input:
        return max(
            [
                sum([int(number) for number in numbers.split("\n")])
                for numbers in input.read().split("\n\n")
            ]
        )


if __name__ == "__main__":
    result = solution()
    print(result)
