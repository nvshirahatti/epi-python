N_PEGS = 3


# O(2^n) time | O(n) space | n: number of rings
def compute_tower_hanoi(n_rings: int) -> list:
    def compute_tower_hanoi_steps(n_rings_to_move, from_peg, to_peg, use_peg) -> None:
        if n_rings_to_move <= 0:
            return None
        compute_tower_hanoi_steps(n_rings_to_move - 1, from_peg, use_peg, to_peg)
        pegs[to_peg].append(pegs[from_peg].pop())
        sln.append([from_peg, to_peg])
        compute_tower_hanoi_steps(n_rings_to_move - 1, use_peg, to_peg, from_peg)

    sln = []
    pegs = [list(reversed(range(1, n_rings + 1)))] + [[] for _ in range(1, N_PEGS)]
    compute_tower_hanoi_steps(n_rings, 0, 1, 2)
    return sln


if __name__ == "__main__":
    n_rings = 6
    sln = compute_tower_hanoi(n_rings)
    # * (asterisk) to unpack list
    print(*sln, sep="\n")
