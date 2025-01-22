#!/usr/bin/env python


def solution() -> str:
    def parse_stacks(stacks: str) -> list[list[str]]:
        lines = stacks.split("\n")[:-1]
        length = len(lines[0]) // 4 + 1
        parsed_stacks = [[] for i in range(length)]

        for line in lines:
            for i in range(1, len(line), 4):
                if line[i] != " ":
                    parsed_stacks[i // 4].append(line[i])

        for stack in parsed_stacks:
            stack.reverse()

        return parsed_stacks

    def parse_procedures(procedures: str) -> list[list[int]]:
        parsed_procedures = []

        for procedure in procedures.split("\n"):
            [_, qty_, _, from_, _, to_] = procedure.split()

            parsed_procedures.append([int(qty_), int(from_), int(to_)])

        return parsed_procedures

    def move_crate(stacks: list[list[str]], qty_: int, from_: int, to_: int):
        moved = stacks[from_ - 1][-qty_:]
        stacks[from_ - 1] = stacks[from_ - 1][:-qty_]
        stacks[to_ - 1].extend(moved)

    with open("../../inputs/day05.txt") as input:
        [stacks, procedures] = input.read().split("\n\n")

        stacks = parse_stacks(stacks)
        procedures = parse_procedures(procedures)

        for procedure in procedures:
            move_crate(stacks, procedure[0], procedure[1], procedure[2])

    return "".join([stack[-1] for stack in stacks])


if __name__ == "__main__":
    result = solution()
    print(result)
