#!/usr/bin/env python


def solution() -> int:
    with open("../../inputs/08.txt") as input:
        rows = input.read().split("\n")
        len_rows, len_columns = len(rows), len(rows[0])
        visibles = 2 * (len_rows + len_columns - 2)

        for i in range(1, len_rows - 1):
            for j in range(1, len_columns - 1):
                current = rows[i][j]
                boundaries = [
                    max(list(rows[i][0:j])),
                    max(list(rows[i][j + 1 :])),
                    max([rows[k][j] for k in range(i)]),
                    max([rows[k][j] for k in range(i + 1, len_rows)]),
                ]

                if len(list(filter(lambda b: b < current, boundaries))) >= 1:
                    visibles += 1

        return visibles


if __name__ == "__main__":
    result = solution()
    print(result)
