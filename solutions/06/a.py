#!/usr/bin/env python


def solution() -> int:
    with open("../../inputs/06.txt") as input:
        count = 4
        signals = input.read()

        while True:
            if len(set(signals[count - 4 : count])) < 4:
                count += 1
                continue

            return count


if __name__ == "__main__":
    result = solution()
    print(result)
