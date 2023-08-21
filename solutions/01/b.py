#!/usr/bin/env python


def solution() -> int:
    with open("../../inputs/01.txt") as input:
        return sum(
            sorted(
                [
                    sum([int(number) for number in numbers.split("\n")])
                    for numbers in input.read().split("\n\n")
                ]
            )[-3:]
        )


if __name__ == "__main__":
    result = solution()
    print(result)
