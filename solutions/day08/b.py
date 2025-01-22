#!/usr/bin/env python


def solution() -> int:
    with open("../../inputs/day08.txt") as input:
        rows = input.read().split("\n")
        len_rows, len_columns = len(rows), len(rows[0])
        scores = []

        for i in range(1, len_rows - 1):
            for j in range(1, len_columns - 1):
                current = rows[i][j]
                boundaries = [
                    list(reversed(list(rows[i][0:j]))),
                    list(rows[i][j + 1 :]),
                    list(reversed([rows[k][j] for k in range(i)])),
                    [rows[k][j] for k in range(i + 1, len_rows)],
                ]

                score = 1

                for boundary in boundaries:
                    tree_count = 0

                    for idx, tree in enumerate(boundary):
                        tree_count += 1

                        if tree >= current:
                            break

                    score *= tree_count

                scores.append(score)

        return max(scores)


if __name__ == "__main__":
    result = solution()
    print(result)
